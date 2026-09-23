import sqlite3
import os
import secrets
import hashlib
import json
import urllib.request
import urllib.error
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load Environment Variables
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=ENV_PATH, override=True)

TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL", "libsql://xortlogix-bot-muhammadokashapak.aws-ap-south-1.turso.io").strip()
TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN", "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3ODY4OTAzODMsImlkIjoiMDFhMDBhZjUtZmMwMS03ZjI0LWExNTgtOWI3ZDlmMjlkM2IzIiwia2lkIjoiUWlmb2V4WFFfQ0JtaFNiQjdOTmw3NjZRZ1A4U3RYVUhYemlnVHNqUXVfQSIsInJpZCI6IjQyNDQ1YTA4LWVlMTMtNGY2Ni04OTkxLTcwNjBhYTY3NTkxZSJ9.uPZH8yqTpcToziU_8rCJBwv1jc8iMGTtZeBevshvSx7VllLJ5otOMN5hhstRerZZr9uufUsl5Y2Pumv5S8nqAw").strip()

USE_TURSO = bool(TURSO_DATABASE_URL and TURSO_AUTH_TOKEN)

# Fallback local sqlite path
IS_VERCEL = bool(os.getenv("VERCEL"))
if IS_VERCEL:
    LOCAL_DB_PATH = "/tmp/ghl_database.db"
else:
    LOCAL_DB_PATH = os.path.join(BASE_DIR, "ghl_database.db")


# --- Turso Cloud Client Engine ---

def _turso_format_arg(val):
    if val is None:
        return {"type": "null"}
    elif isinstance(val, int):
        return {"type": "integer", "value": str(val)}
    elif isinstance(val, float):
        return {"type": "float", "value": val}
    elif isinstance(val, bool):
        return {"type": "integer", "value": "1" if val else "0"}
    else:
        return {"type": "text", "value": str(val)}

def _query_turso(sql: str, params=None):
    http_url = TURSO_DATABASE_URL.replace("libsql://", "https://").rstrip("/") + "/v2/pipeline"
    stmt = {"sql": sql}
    if params:
        stmt["args"] = [_turso_format_arg(p) for p in params]
    
    payload = {
        "requests": [
            {"type": "execute", "stmt": stmt},
            {"type": "close"}
        ]
    }
    
    req = urllib.request.Request(
        http_url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {TURSO_AUTH_TOKEN}",
            "Content-Type": "application/json"
        }
    )
    
    with urllib.request.urlopen(req, timeout=12) as resp:
        data = json.loads(resp.read().decode("utf-8"))
        result = data["results"][0]
        if result["type"] == "error":
            raise Exception(result["error"]["message"])
        
        exec_res = result["response"]["result"]
        cols = [c["name"] for c in exec_res.get("cols", [])]
        rows = []
        for raw_row in exec_res.get("rows", []):
            row_dict = {}
            for col_name, cell in zip(cols, raw_row):
                c_type = cell.get("type")
                if c_type == "null":
                    row_dict[col_name] = None
                elif c_type == "integer":
                    row_dict[col_name] = int(cell.get("value", 0))
                elif c_type == "float":
                    row_dict[col_name] = float(cell.get("value", 0.0))
                else:
                    row_dict[col_name] = cell.get("value", "")
            rows.append(row_dict)
        return rows, exec_res.get("affected_row_count", 0)

# --- Universal Database Runner ---

def db_query(sql: str, params=None, fetchone=False, fetchall=False, commit=False):
    if USE_TURSO:
        try:
            rows, affected = _query_turso(sql, params)
            if fetchone:
                return rows[0] if rows else None
            if fetchall:
                return rows
            return affected
        except Exception as e:
            # Fallback to local if Turso fails or unreachable
            print(f"[Turso Error, falling back to local SQLite]: {e}")

    # Local SQLite Fallback
    conn = sqlite3.connect(LOCAL_DB_PATH, timeout=30)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(sql, tuple(params))
        else:
            cursor.execute(sql)
        
        if fetchone:
            res = cursor.fetchone()
            return dict(res) if res else None
        elif fetchall:
            res = cursor.fetchall()
            return [dict(r) for r in res]
        else:
            if commit:
                conn.commit()
            return cursor.rowcount
    finally:
        if commit:
            conn.commit()
        conn.close()


# --- Security & Password Helpers ---

def hash_password(password: str, salt_hex: str = None):
    if salt_hex is None:
        salt_hex = secrets.token_hex(16)
    salt_bytes = bytes.fromhex(salt_hex)
    pwd_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt_bytes, 100000)
    return pwd_hash.hex(), salt_hex

def verify_password(password: str, salt_hex: str, expected_hash_hex: str):
    computed_hash_hex, _ = hash_password(password, salt_hex)
    return secrets.compare_digest(computed_hash_hex, expected_hash_hex)


# --- Database Schema Initialization ---

def init_db():
    queries = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS sessions (
            session_token TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            created_at TEXT NOT NULL,
            expires_at TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS conversations (
            id TEXT PRIMARY KEY,
            user_id TEXT NOT NULL,
            title TEXT NOT NULL,
            is_pinned INTEGER DEFAULT 0,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS messages (
            id TEXT PRIMARY KEY,
            conversation_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            sources_json TEXT,
            attachments_json TEXT,
            created_at TEXT NOT NULL
        );
        """
    ]
    for q in queries:
        db_query(q, commit=True)

    # Migrate existing messages table if attachments_json is missing
    try:
        cols = db_query("PRAGMA table_info(messages);", fetchall=True)
        col_names = [c.get('name') for c in cols] if cols else []
        if col_names and 'attachments_json' not in col_names:
            db_query("ALTER TABLE messages ADD COLUMN attachments_json TEXT;", commit=True)
    except Exception:
        pass

    # Seed Default User if database is empty
    try:
        if not get_user_by_email("sara@example.com"):
            create_user("Sara Khan", "sara@example.com", "Password123")
    except Exception:
        pass


# --- User Operations ---

def create_user(name: str, email: str, password: str):
    email_clean = email.strip().lower()
    name_clean = name.strip()
    
    existing = db_query("SELECT id FROM users WHERE email = ?", [email_clean], fetchone=True)
    if existing:
        raise ValueError("An account with this email address already exists.")

    user_id = f"user_{secrets.token_hex(12)}"
    pwd_hash, salt = hash_password(password)
    now_str = datetime.utcnow().isoformat()

    db_query(
        "INSERT INTO users (id, name, email, password_hash, salt, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
        [user_id, name_clean, email_clean, pwd_hash, salt, now_str, now_str],
        commit=True
    )
    return {"id": user_id, "name": name_clean, "email": email_clean}

def authenticate_user(email: str, password: str):
    email_clean = email.strip().lower()
    user_row = db_query("SELECT * FROM users WHERE email = ?", [email_clean], fetchone=True)

    if not user_row:
        return None

    if verify_password(password, user_row['salt'], user_row['password_hash']):
        return {"id": user_row['id'], "name": user_row['name'], "email": user_row['email']}
    return None

def get_user_by_email(email: str):
    email_clean = email.strip().lower()
    return db_query("SELECT * FROM users WHERE email = ?", [email_clean], fetchone=True)

def get_user_by_id(user_id: str):
    return db_query("SELECT id, name, email, created_at FROM users WHERE id = ?", [user_id], fetchone=True)

def update_user_name(user_id: str, new_name: str):
    name_clean = new_name.strip()
    if not name_clean:
        raise ValueError("Name cannot be empty.")
    now_str = datetime.utcnow().isoformat()
    db_query("UPDATE users SET name = ?, updated_at = ? WHERE id = ?", [name_clean, now_str, user_id], commit=True)
    return get_user_by_id(user_id)

def update_password(user_id: str, old_password: str, new_password: str):
    user_row = db_query("SELECT * FROM users WHERE id = ?", [user_id], fetchone=True)
    if not user_row:
        raise ValueError("User not found")
    
    if not verify_password(old_password, user_row['salt'], user_row['password_hash']):
        raise ValueError("Current password is incorrect")

    pwd_hash, salt = hash_password(new_password)
    now_str = datetime.utcnow().isoformat()
    db_query("UPDATE users SET password_hash = ?, salt = ?, updated_at = ? WHERE id = ?",
             [pwd_hash, salt, now_str, user_id], commit=True)
    return True


# --- Session Operations ---

def create_session(user_id: str, days=30):
    session_token = f"sess_{secrets.token_hex(32)}"
    now = datetime.utcnow()
    expires = now + timedelta(days=days)

    db_query(
        "INSERT INTO sessions (session_token, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)",
        [session_token, user_id, now.isoformat(), expires.isoformat()],
        commit=True
    )
    return session_token

def get_user_from_session(session_token: str):
    if not session_token:
        return None
    
    row = db_query("""
        SELECT u.id, u.name, u.email, s.expires_at 
        FROM sessions s
        JOIN users u ON s.user_id = u.id
        WHERE s.session_token = ?
    """, [session_token], fetchone=True)

    if not row:
        return None

    # Check expiration
    expires_at = datetime.fromisoformat(row['expires_at'])
    if datetime.utcnow() > expires_at:
        delete_session(session_token)
        return None

    return {"id": row['id'], "name": row['name'], "email": row['email']}

def delete_session(session_token: str):
    if not session_token:
        return
    db_query("DELETE FROM sessions WHERE session_token = ?", [session_token], commit=True)


# --- Conversation & Message Operations ---

def create_conversation(user_id: str, title: str = "New Chat"):
    # Reuse existing empty draft conversation if available
    existing_empty = db_query("""
        SELECT c.id, c.title, c.is_pinned, c.created_at, c.updated_at
        FROM conversations c
        LEFT JOIN messages m ON c.id = m.conversation_id
        WHERE c.user_id = ?
        GROUP BY c.id
        HAVING COUNT(m.id) = 0
        ORDER BY c.created_at DESC
        LIMIT 1
    """, [user_id], fetchone=True)

    if existing_empty:
        return {
            "id": existing_empty['id'],
            "user_id": user_id,
            "title": existing_empty['title'],
            "is_pinned": bool(existing_empty['is_pinned']),
            "created_at": existing_empty['created_at'],
            "updated_at": existing_empty['updated_at']
        }

    conv_id = f"conv_{secrets.token_hex(12)}"
    now_str = datetime.utcnow().isoformat()
    
    db_query(
        "INSERT INTO conversations (id, user_id, title, is_pinned, created_at, updated_at) VALUES (?, ?, ?, 0, ?, ?)",
        [conv_id, user_id, title, now_str, now_str],
        commit=True
    )
    return {"id": conv_id, "user_id": user_id, "title": title, "is_pinned": 0, "created_at": now_str, "updated_at": now_str}

def get_user_conversations(user_id: str):
    rows = db_query("""
        SELECT c.id, c.title, c.is_pinned, c.created_at, c.updated_at,
               COUNT(m.id) as message_count
        FROM conversations c
        LEFT JOIN messages m ON c.id = m.conversation_id
        WHERE c.user_id = ?
        GROUP BY c.id
        HAVING message_count > 0
        ORDER BY c.is_pinned DESC, c.updated_at DESC
    """, [user_id], fetchall=True) or []

    result = []
    for r in rows:
        result.append({
            "id": r['id'],
            "title": r['title'],
            "is_pinned": bool(r['is_pinned']),
            "created_at": r['created_at'],
            "updated_at": r['updated_at'],
            "message_count": r['message_count']
        })
    return result

def get_conversation_details(conv_id: str, user_id: str):
    conv = db_query("SELECT * FROM conversations WHERE id = ? AND user_id = ?", [conv_id, user_id], fetchone=True)
    if not conv:
        return None

    messages_rows = db_query("""
        SELECT id, role, content, sources_json, attachments_json, created_at
        FROM messages
        WHERE conversation_id = ?
        ORDER BY created_at ASC
    """, [conv_id], fetchall=True) or []

    messages = []
    for m in messages_rows:
        att_data = []
        if m.get('attachments_json'):
            try:
                att_data = json.loads(m['attachments_json'])
            except Exception:
                att_data = []
        messages.append({
            "id": m['id'],
            "role": m['role'],
            "content": m['content'],
            "sources": json.loads(m['sources_json']) if m.get('sources_json') else [],
            "attachments": att_data,
            "created_at": m['created_at']
        })

    return {
        "id": conv['id'],
        "title": conv['title'],
        "is_pinned": bool(conv['is_pinned']),
        "created_at": conv['created_at'],
        "updated_at": conv['updated_at'],
        "messages": messages
    }

def get_conversation_messages(conv_id: str, user_id: str):
    details = get_conversation_details(conv_id, user_id)
    return details['messages'] if details else []

def add_message(conv_id: str, user_id: str, role: str, content: str, sources=None, attachments=None):
    # Verify ownership
    conv = db_query("SELECT id, title FROM conversations WHERE id = ? AND user_id = ?", [conv_id, user_id], fetchone=True)
    if not conv:
        raise ValueError("Conversation not found or access denied")

    cnt_row = db_query("SELECT COUNT(*) as cnt FROM messages WHERE conversation_id = ?", [conv_id], fetchone=True)
    msg_count_before = cnt_row['cnt'] if cnt_row else 0

    msg_id = f"msg_{secrets.token_hex(12)}"
    now_str = datetime.utcnow().isoformat()
    sources_json = json.dumps(sources) if sources else None
    attachments_json = json.dumps(attachments) if attachments else None

    db_query(
        "INSERT INTO messages (id, conversation_id, role, content, sources_json, attachments_json, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
        [msg_id, conv_id, role, content, sources_json, attachments_json, now_str],
        commit=True
    )

    # Auto generate smart title ONLY on the VERY FIRST message of the conversation
    new_title = conv['title']
    if role == 'user' and (msg_count_before == 0 or conv['title'] == "New Chat" or not conv['title']):
        raw_query = content.strip()
        if not raw_query and attachments:
            first_att = attachments[0].get('name', 'File Attachment')
            new_title = f"Uploaded: {first_att}"
        else:
            words = raw_query.split()
            if len(words) > 6:
                new_title = " ".join(words[:6]) + "..."
            else:
                new_title = raw_query
        new_title = new_title[:45]

    db_query("UPDATE conversations SET title = ?, updated_at = ? WHERE id = ?", [new_title, now_str, conv_id], commit=True)

    return {
        "id": msg_id,
        "conversation_id": conv_id,
        "role": role,
        "content": content,
        "sources": sources or [],
        "attachments": attachments or [],
        "created_at": now_str,
        "conversation_title": new_title
    }

def rename_conversation(conv_id: str, user_id: str, new_title: str):
    now_str = datetime.utcnow().isoformat()
    affected = db_query(
        "UPDATE conversations SET title = ?, updated_at = ? WHERE id = ? AND user_id = ?",
        [new_title.strip(), now_str, conv_id, user_id],
        commit=True
    )
    return (affected or 0) > 0

def toggle_pin_conversation(conv_id: str, user_id: str):
    row = db_query("SELECT is_pinned FROM conversations WHERE id = ? AND user_id = ?", [conv_id, user_id], fetchone=True)
    if not row:
        return False
    
    new_pin = 0 if row['is_pinned'] else 1
    db_query("UPDATE conversations SET is_pinned = ? WHERE id = ? AND user_id = ?", [new_pin, conv_id, user_id], commit=True)
    return bool(new_pin)

def delete_conversation(conv_id: str, user_id: str):
    conv = db_query("SELECT id FROM conversations WHERE id = ? AND user_id = ?", [conv_id, user_id], fetchone=True)
    if not conv:
        return False
    db_query("DELETE FROM messages WHERE conversation_id = ?", [conv_id], commit=True)
    db_query("DELETE FROM conversations WHERE id = ? AND user_id = ?", [conv_id, user_id], commit=True)
    return True

def get_all_users():
    users = db_query("SELECT id, name, email, created_at FROM users", fetchall=True) or []
    result = []
    for u in users:
        msgs = db_query("SELECT COUNT(*) as count FROM messages m JOIN conversations c ON m.conversation_id = c.id WHERE c.user_id = ?", [u['id']], fetchone=True)
        result.append({
            "id": u['id'],
            "name": u['name'],
            "email": u['email'],
            "created_at": u['created_at'],
            "message_count": msgs['count'] if msgs else 0
        })
    return result

def delete_user(user_id: str):
    affected = db_query("DELETE FROM users WHERE id = ?", [user_id], commit=True)
    return (affected or 0) > 0

# Initialize DB on module load
init_db()
