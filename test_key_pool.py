import time
from app import gemini_key_pool, app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_key_pool():
    print("Testing Multi-Key Polling & Failover Pool...")
    
    # 1. Check loaded keys
    gemini_key_pool.reload_keys()
    assert len(gemini_key_pool.keys) >= 3, f"Expected at least 3 keys, found {len(gemini_key_pool.keys)}"
    print(f"✅ Loaded {len(gemini_key_pool.keys)} API keys in the polling pool.")

    # 2. Check round-robin polling rotation
    k1 = gemini_key_pool.get_candidate_keys()[0]
    k2 = gemini_key_pool.get_candidate_keys()[0]
    k3 = gemini_key_pool.get_candidate_keys()[0]
    print(f"Key 1: {k1[:12]}...")
    print(f"Key 2: {k2[:12]}...")
    print(f"Key 3: {k3[:12]}...")
    assert k1 != k2, "Keys should rotate on successive requests!"
    print("✅ Round-robin polling rotation verified across requests!")

    # 3. Test Rate-Limit Failover / Cooldown shifting
    target_key = k1
    gemini_key_pool.mark_rate_limited(target_key, cooldown_seconds=10)
    candidates_after_limit = gemini_key_pool.get_candidate_keys()
    
    # The rate-limited key should NOT be primary candidate; it must be shifted to backup
    assert candidates_after_limit[0] != target_key, "Rate-limited key must not be primary candidate!"
    assert target_key in candidates_after_limit, "Rate-limited key should remain in backup candidates"
    print("✅ Instant failover & cooldown shifting verified! Exhausted keys shift to backup immediately.")

    # 4. Test Key Pool Status Endpoint
    res = client.get("/api/key-pool/status")
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    status_data = res.json()
    print("Pool status:", status_data)
    assert status_data["total_keys"] >= 3
    print("✅ /api/key-pool/status endpoint verified successfully!")

    print("\n🎉 ALL KEY POOLING & FAILOVER TESTS PASSED!")

if __name__ == "__main__":
    test_key_pool()
