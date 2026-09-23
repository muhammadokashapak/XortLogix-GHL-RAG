import os
import re
import gc
import json
import time
import hashlib
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field

# ==========================================
# 1. DATA STRUCTURES
# ==========================================

@dataclass
class QueryAnalysis:
    raw_query: str
    cleaned_query: str
    intent: str
    objective: str
    core_entities: List[str] = field(default_factory=list)
    topics: List[str] = field(default_factory=list)
    output_type: str = "general_explanation"
    expanded_queries: List[str] = field(default_factory=list)
    is_conversational: bool = False
    is_complex: bool = False
    is_out_of_scope: bool = False

@dataclass
class RetrievedChunk:
    chunk_id: str
    content: str
    score: float = 0.0
    source: str = "ghl_knowledge_base"
    match_type: str = "vector"
    metadata: Dict[str, Any] = field(default_factory=dict)


# ==========================================
# 2. QUERY UNDERSTANDING & INTENT ENGINE
# ==========================================

class QueryUnderstandingEngine:
    """
    Analyzes user query to determine:
    1. Intent (frontend_customization, job_posting_analysis, technical_troubleshooting,
       system_architecture, business_strategy, comparison_evaluation, factual_lookup, conversational, out_of_scope)
    2. Core Entities & Concepts
    3. Output Type & Formatting Goals
    4. Adaptive Query Expansion (sub-queries for complex inputs)
    """

    GREETING_PATTERNS = {
        "hi", "hello", "hey", "hey there", "hello there", "greetings",
        "good morning", "good afternoon", "good evening", "good day",
        "aoa", "assalam o alaikum", "assalam-o-alaikum", "assalamu alaikum",
        "salam", "slaam", "wsalam", "how are you", "how are you?",
        "how r u", "who are you", "who are you?", "what can you do",
        "what can you do?", "help", "help me", "hi bot", "hello bot"
    }

    INTENT_OPENER_PATTERNS = {
        "i want to learn one thing", "i want to learn something", "i want to learn",
        "i want to learn ghl", "i have a question", "can i ask a question",
        "can i ask something", "i want to ask something", "can you help me",
        "i need help", "help me", "can you teach me", "teach me",
        "tell me about yourself", "how does this work", "help me with ghl",
        "i need some help", "i need assistance"
    }

    OUT_OF_SCOPE_KEYWORDS = {
        "recipe", "cooking", "how to bake", "cake", "chocolate", "pizza",
        "weather in", "forecast", "cricket score", "football match", "fifa",
        "hollywood", "bollywood", "celebrity", "movie review", "horoscope",
        "astrology", "gaming tips", "playstation", "minecraft", "gta 5"
    }

    @classmethod
    def analyze(cls, query: str, user_name: str = "User", history: List[Dict[str, Any]] = None) -> QueryAnalysis:
        raw_text = query.strip()
        cleaned_text = raw_text.lower().rstrip('.!?')
        words = cleaned_text.split()
        word_count = len(words)

        # 1. Check for Conversational Openers & Greetings
        if cleaned_text in cls.GREETING_PATTERNS or (
            any(cleaned_text.startswith(p) for p in ["i want to learn", "can you teach me", "i want to ask", "can i ask", "i have a question"])
            and word_count <= 7
        ) or cleaned_text in cls.INTENT_OPENER_PATTERNS:
            return QueryAnalysis(
                raw_query=raw_text,
                cleaned_query=cleaned_text,
                intent="conversational_greeting",
                objective="Acknowledge user warmly and offer GHL assistance.",
                core_entities=["GoHighLevel"],
                topics=["Introduction", "Assistance"],
                output_type="conversational_reply",
                expanded_queries=[],
                is_conversational=True,
                is_complex=False
            )

        # 2. Check for Strict Out-of-Scope Topics (Non-GHL)
        if any(kw in cleaned_text for kw in cls.OUT_OF_SCOPE_KEYWORDS):
            if not any(ghl_term in cleaned_text for ghl_term in ["ghl", "gohighlevel", "crm", "workflow", "funnel", "pipeline", "dom", "mutationobserver", "rest_api_call"]):
                return QueryAnalysis(
                    raw_query=raw_text,
                    cleaned_query=cleaned_text,
                    intent="out_of_scope",
                    objective="Politely decline out-of-scope question and state GHL domain expertise.",
                    core_entities=[],
                    topics=["Off-Topic"],
                    output_type="out_of_scope_notice",
                    expanded_queries=[],
                    is_conversational=False,
                    is_complex=False,
                    is_out_of_scope=True
                )

        # 3. Detect Front-End Custom Development, DOM Handling & Script Injection
        frontend_signals = [
            "mutationobserver", "routechangeevent", "checkforformula404", "formula404",
            "rest_api_call", "contactsdetails", "rolespermission", "custom js",
            "custom css", "dashboard theme", "dom monitoring", "custom widget",
            "custom script", "dynamic dom", "spa architecture", "frontend customization"
        ]
        is_frontend = any(sig in cleaned_text for sig in frontend_signals)

        if is_frontend:
            entities = cls._extract_entities(raw_text)
            expanded = [
                "GoHighLevel frontend customization MutationObserver routeChangeEvent",
                "GHL custom JS formula404 rest_api_call dashboard widgets",
                "GoHighLevel custom dashboard CSS theme dark mode styling"
            ]
            return QueryAnalysis(
                raw_query=raw_text,
                cleaned_query=cleaned_text,
                intent="frontend_customization",
                objective="Provide complete, production-ready GoHighLevel frontend customization code (JavaScript MutationObserver, SPA routeChangeEvent, script injection, internal rest_api_call, and custom CSS theme styling).",
                core_entities=entities,
                topics=["Frontend Customization", "Dynamic DOM", "SPA Route Handling", "Custom CSS Theme", "REST API Helpers"],
                output_type="frontend_customization_blueprint",
                expanded_queries=expanded,
                is_conversational=False,
                is_complex=True
            )

        # 4. Detect Blog / Article Proofreading & GHL Feasibility Review
        blog_signals = [
            "proofread", "proof read", "proofreading", "review this blog", "review this article",
            "check this blog", "check this article", "proofread this blog", "proofread this article",
            "proofread my blog", "proofread my article", "review my blog", "review my article",
            "blog post", "article review"
        ]
        is_blog = any(sig in cleaned_text for sig in blog_signals) or (
            ("blog" in cleaned_text or "article" in cleaned_text) and 
            any(w in cleaned_text for w in ["proofread", "review", "check", "accurate", "native", "customly", "custom", "possible"])
        )

        if is_blog:
            entities = cls._extract_entities(raw_text)
            expanded = [
                f"{e} GoHighLevel native features capabilities" for e in entities[:2]
            ] + ["GoHighLevel native features vs custom development", "GoHighLevel workflows and capabilities"]
            return QueryAnalysis(
                raw_query=raw_text,
                cleaned_query=cleaned_text,
                intent="blog_article_proofreading",
                objective="Proofread the blog or article for technical accuracy, verify whether all mentioned features are possible natively in GoHighLevel or require custom development, correct terminology, and provide constructive feedback.",
                core_entities=entities,
                topics=["Blog Proofreading", "Technical Accuracy", "Native vs Custom Feasibility", "GHL Feature Verification"],
                output_type="blog_proofreading_and_feasibility",
                expanded_queries=expanded[:3],
                is_conversational=False,
                is_complex=True
            )

        # 5. Detect Direct Native vs Custom Feasibility Inquiry
        native_signals = [
            "is it possible natively", "possible natively", "natively possible", "natively in ghl",
            "can ghl do this natively", "can gohighlevel do this natively", "native or custom",
            "do it customly", "do this customly", "natively vs custom", "native vs custom",
            "can this be done natively", "is this supported natively", "native feature or custom",
            "kya ye natively possible hai", "natively ho sakta hai", "natively ho skta hai",
            "natively support", "supported natively", "ghl native", "natively kar sakte", "natively ho sakta"
        ]
        is_native_check = any(sig in cleaned_text for sig in native_signals)

        if is_native_check:
            entities = cls._extract_entities(raw_text)
            expanded = [
                f"{e} GoHighLevel native feature capability" for e in entities[:2]
            ] + ["GoHighLevel native features", "GoHighLevel custom code API limitations"]
            return QueryAnalysis(
                raw_query=raw_text,
                cleaned_query=cleaned_text,
                intent="native_feasibility_check",
                objective="Evaluate and answer definitively whether the requested feature is possible natively in GoHighLevel, possible via a native workaround, or strictly requires custom development.",
                core_entities=entities,
                topics=["Native Feasibility", "Native vs Custom", "Workarounds", "Custom Development"],
                output_type="native_feasibility_verdict",
                expanded_queries=expanded[:3],
                is_conversational=False,
                is_complex=True
            )

        # 6. Detect Job Postings, RFPs & Hiring Requirements
        job_signals = [
            "growth & campaign specialist", "campaign specialist", "specialist",
            "we are looking for", "responsibilities", "what you will be responsible for",
            "primary objectives", "compensation", "how to apply", "first 90-day",
            "ideal candidate", "bonus skills", "not a good fit", "results we expect",
            "client acquisition", "agent acquisition", "hiring", "job description"
        ]
        job_matches = sum(1 for signal in job_signals if signal in cleaned_text)
        is_job_posting = job_matches >= 2 or (
            any(s in cleaned_text for s in ["growth & campaign specialist", "job description", "we are looking for"]) 
            and word_count > 40
        )

        if is_job_posting:
            entities = cls._extract_entities(raw_text)
            expanded = [
                "GoHighLevel marketing campaigns lead generation funnels",
                "automated SMS email nurturing workflows appointment booking",
                "client acquisition agent recruiting pipeline setup",
                "campaign tracking reporting metrics conversion rate"
            ]
            return QueryAnalysis(
                raw_query=raw_text,
                cleaned_query=cleaned_text,
                intent="job_posting_analysis",
                objective="Analyze company needs, required technical/marketing skills, expected KPIs, candidate evaluation criteria, and formulate a winning application strategy.",
                core_entities=entities,
                topics=["Campaign Strategy", "Funnel Building", "Lead Generation", "Automations", "Client Acquisition", "Recruiting Funnel"],
                output_type="job_analysis_and_strategy",
                expanded_queries=expanded,
                is_conversational=False,
                is_complex=True
            )

        # 5. Detect Technical Troubleshooting & Error Debugging
        troubleshoot_signals = [
            "error", "failed", "not working", "issue", "bug", "500", "404", "403",
            "troubleshoot", "why is my", "webhook failing", "trigger not firing",
            "contact not added", "email not sending", "sms failed", "broken", "fix"
        ]
        is_troubleshooting = any(sig in cleaned_text for sig in troubleshoot_signals) and (
            "workflow" in cleaned_text or "ghl" in cleaned_text or "trigger" in cleaned_text or
            "webhook" in cleaned_text or "pipeline" in cleaned_text or "integration" in cleaned_text or word_count > 15
        )

        if is_troubleshooting:
            entities = cls._extract_entities(raw_text)
            expanded = [
                f"{e} troubleshooting configuration fix" for e in entities[:2]
            ] or ["workflow trigger error troubleshooting", "webhook integration setup"]
            return QueryAnalysis(
                raw_query=raw_text,
                cleaned_query=cleaned_text,
                intent="technical_troubleshooting",
                objective="Identify root cause, probable failure points, and provide verified step-by-step resolution in GoHighLevel.",
                core_entities=entities,
                topics=["Troubleshooting", "Error Resolution", "Workflows", "Triggers"],
                output_type="troubleshooting_guide",
                expanded_queries=expanded[:3],
                is_conversational=False,
                is_complex=True
            )

        # 6. Detect System / Workflow Architecture
        architecture_signals = [
            "how to build", "how to setup", "how to create a workflow", "how to integrate",
            "step by step", "architecture", "pipeline setup", "multi-step",
            "client onboarding", "booking funnel", "appointment system", "automation system"
        ]
        is_architecture = any(sig in cleaned_text for sig in architecture_signals) or (
            word_count > 30 and ("workflow" in cleaned_text or "funnel" in cleaned_text or "automation" in cleaned_text)
        )

        if is_architecture:
            entities = cls._extract_entities(raw_text)
            expanded = [
                f"{e} workflow automation setup" for e in entities[:2]
            ] + ["GoHighLevel workflow triggers and actions", "pipeline stage automations"]
            return QueryAnalysis(
                raw_query=raw_text,
                cleaned_query=cleaned_text,
                intent="system_architecture",
                objective="Provide an executive, end-to-end technical blueprint with triggers, actions, custom values, and pipeline automations.",
                core_entities=entities,
                topics=["System Architecture", "Workflow Automation", "Funnels", "Pipelines"],
                output_type="architecture_blueprint",
                expanded_queries=expanded[:3],
                is_conversational=False,
                is_complex=True
            )

        # 7. Detect Comparison / Evaluation
        if any(k in cleaned_text for k in ["difference between", " vs ", "versus", "compare", "which is better"]):
            entities = cls._extract_entities(raw_text)
            return QueryAnalysis(
                raw_query=raw_text,
                cleaned_query=cleaned_text,
                intent="comparison_evaluation",
                objective="Compare and contrast features, benefits, use cases, and limitations.",
                core_entities=entities,
                topics=["Comparison", "Evaluation"],
                output_type="comparative_breakdown",
                expanded_queries=[f"{e} overview features" for e in entities[:2]],
                is_conversational=False,
                is_complex=False
            )

        # 8. Default: Factual Lookup or General Technical Query
        is_complex = word_count > 30
        entities = cls._extract_entities(raw_text)
        expanded = [cleaned_text[:120]] if not is_complex else [
            cleaned_text[:120],
            f"{entities[0]} GoHighLevel feature setup" if entities else "GoHighLevel features"
        ]

        return QueryAnalysis(
            raw_query=raw_text,
            cleaned_query=cleaned_text,
            intent="factual_lookup" if not is_complex else "general_technical",
            objective="Provide accurate technical explanation based on official GoHighLevel documentation.",
            core_entities=entities,
            topics=["Technical Support"],
            output_type="direct_concise" if not is_complex else "detailed_technical",
            expanded_queries=expanded[:2],
            is_conversational=False,
            is_complex=is_complex
        )

    @classmethod
    def _extract_entities(cls, text: str) -> List[str]:
        entities = []
        known_keywords = [
            "MutationObserver", "routeChangeEvent", "Formula404", "rest_api_call",
            "contactsdetails", "rolesPermission", "Custom CSS", "Custom JavaScript",
            "Dashboard Theme", "Custom Widgets", "Custom Data Displays", "SPA Architecture",
            "Workflow", "Workflows", "Trigger", "Triggers", "Action", "Actions",
            "Custom Values", "Custom Fields", "Funnel", "Funnels", "Landing Page",
            "Form", "Forms", "Survey", "Surveys", "Calendar", "Calendars",
            "Pipeline", "Pipelines", "Opportunity", "Opportunities", "Webhook", "Webhooks",
            "REST API", "API", "OAuth", "OAuth 2.0", "Access Token", "Refresh Token", "Scopes",
            "Sub-account", "Sub-accounts", "Snapshot", "Snapshots", "Private Integration"
        ]
        text_lower = text.lower()
        for kw in known_keywords:
            if kw.lower() in text_lower and kw not in entities:
                entities.append(kw)
        return entities[:8]


# ==========================================
# 3. HYBRID RETRIEVAL & RERANKING
# ==========================================

class HybridRetriever:
    """
    Executes hybrid search (Semantic Vector via FastEmbed ONNX + Keyword token matching)
    and combines results across original query and expanded sub-queries using Reciprocal Rank Fusion (RRF).
    """

    @classmethod
    def search(cls, analysis: QueryAnalysis, chroma_col, embed_model, top_k: int = 5) -> List[RetrievedChunk]:
        if not chroma_col:
            return []

        search_queries = []
        search_queries.append(analysis.raw_query[:300].strip())

        if analysis.is_complex and analysis.expanded_queries:
            search_queries.extend(analysis.expanded_queries[:3])

        all_candidates: Dict[str, Dict[str, Any]] = {}
        rrf_k = 60

        batch_inputs = [f"search_query: {q}" for q in search_queries if q]
        query_embs = []
        if embed_model and batch_inputs:
            for q_text in batch_inputs:
                try:
                    if hasattr(embed_model, 'embed'):
                        embs = list(embed_model.embed([q_text]))
                        if embs:
                            e_item = embs[0]
                            query_embs.append(e_item.tolist() if hasattr(e_item, 'tolist') else list(e_item))
                    elif hasattr(embed_model, 'encode'):
                        emb = embed_model.encode(q_text)
                        query_embs.append(emb.tolist() if hasattr(emb, 'tolist') else list(emb))
                except Exception as e_emb:
                    print(f"⚠️ Query embedding note for '{q_text[:30]}...': {e_emb}")

        for q_idx, query_emb in enumerate(query_embs):
            try:
                res = chroma_col.query(query_embeddings=[query_emb], n_results=min(top_k * 2, 6))
                if res and res.get('documents') and len(res['documents']) > 0:
                    docs = res['documents'][0]
                    metas = res['metadatas'][0] if res.get('metadatas') else [{}] * len(docs)
                    ids = res['ids'][0] if res.get('ids') else [hashlib.md5(d.encode('utf-8')).hexdigest() for d in docs]
                    distances = res['distances'][0] if res.get('distances') else [0.5] * len(docs)

                    for rank, (doc_id, doc_text, meta, dist) in enumerate(zip(ids, docs, metas, distances)):
                        if not doc_text or len(doc_text.strip()) < 20:
                            continue
                        if doc_id not in all_candidates:
                            all_candidates[doc_id] = {
                                'id': doc_id,
                                'content': doc_text,
                                'meta': meta or {},
                                'vector_score': 1.0 / (1.0 + float(dist)),
                                'rrf_score': 0.0,
                                'keyword_score': 0.0,
                                'query_hits': 0
                            }
                        all_candidates[doc_id]['rrf_score'] += 1.0 / (rrf_k + rank + 1)
                        all_candidates[doc_id]['query_hits'] += 1
            except Exception as e_q:
                print(f"⚠️ Vector search query note: {e_q}")

        # Keyword matching
        keyword_targets = analysis.core_entities[:3]
        for kw in keyword_targets:
            if len(kw) < 3:
                continue
            try:
                kw_res = chroma_col.get(where_document={"$contains": kw}, limit=3)
                if kw_res and kw_res.get('documents'):
                    kw_docs = kw_res['documents']
                    kw_ids = kw_res.get('ids', [hashlib.md5(d.encode('utf-8')).hexdigest() for d in kw_docs])
                    kw_metas = kw_res.get('metadatas', [{}] * len(kw_docs))
                    for rank, (doc_id, doc_text, meta) in enumerate(zip(kw_ids, kw_docs, kw_metas)):
                        if doc_id not in all_candidates:
                            all_candidates[doc_id] = {
                                'id': doc_id,
                                'content': doc_text,
                                'meta': meta or {},
                                'vector_score': 0.5,
                                'rrf_score': 0.0,
                                'keyword_score': 0.0,
                                'query_hits': 0
                            }
                        all_candidates[doc_id]['keyword_score'] += 0.3
                        all_candidates[doc_id]['rrf_score'] += 1.0 / (rrf_k + rank + 1)
            except Exception:
                pass

        gc.collect()

        if not all_candidates:
            return []

        ranked_chunks: List[RetrievedChunk] = []
        for cand in all_candidates.values():
            composite_score = (cand['rrf_score'] * 2.0) + (cand['vector_score'] * 0.5) + (cand['keyword_score'] * 0.3)
            content_lower = cand['content'].lower()
            entity_matches = sum(1 for e in analysis.core_entities if e.lower() in content_lower)
            composite_score += (entity_matches * 0.1)

            ranked_chunks.append(RetrievedChunk(
                chunk_id=cand['id'],
                content=cand['content'],
                score=round(composite_score, 4),
                source=cand['meta'].get('source', 'GoHighLevel Official Documentation'),
                metadata=cand['meta']
            ))

        ranked_chunks.sort(key=lambda x: x.score, reverse=True)

        seen_hashes = set()
        deduped: List[RetrievedChunk] = []
        for c in ranked_chunks:
            c_hash = hashlib.md5(c.content[:150].strip().lower().encode('utf-8')).hexdigest()
            if c_hash not in seen_hashes:
                seen_hashes.add(c_hash)
                deduped.append(c)
                if len(deduped) >= top_k:
                    break

        return deduped


# ==========================================
# 4. CONTEXT ASSEMBLER & LATEX SANITIZER
# ==========================================

class ContextAssembler:
    @classmethod
    def assemble(
        cls,
        analysis: QueryAnalysis,
        chunks: List[RetrievedChunk],
        user_name: str = "User",
        history: List[Dict[str, Any]] = None
    ) -> Tuple[str, List[str]]:
        if not chunks:
            return "Standard GoHighLevel Knowledge Base (No specific chunk matches).", []

        context_blocks = []
        source_labels = []

        for idx, chunk in enumerate(chunks, 1):
            src = chunk.metadata.get('title') or chunk.source or f"Documentation Section {idx}"
            source_labels.append(src)
            context_blocks.append(f"--- DOCUMENT EXCERPT {idx} [{src}] ---\n{chunk.content.strip()}")

        assembled_str = "\n\n".join(context_blocks)
        return assembled_str, list(dict.fromkeys(source_labels))


def clean_latex_artifacts(text: str) -> str:
    """Sanitizes raw LaTeX / KaTeX math notation and arrow commands into clean, readable plain text / unicode."""
    if not text:
        return text or ""

    # 1. LaTeX Arrow Commands -> Clean Unicode Arrows
    text = re.sub(r'\\(rightarrow|longrightarrow|to|mapsto|implies)\b', '→', text)
    text = re.sub(r'\\(leftarrow|longleftarrow)\b', '←', text)
    text = re.sub(r'\\(Rightarrow|Longrightarrow)\b', '⇒', text)
    text = re.sub(r'\\(Leftarrow|Longleftarrow)\b', '⇐', text)
    text = re.sub(r'\\(leftrightarrow|longleftrightarrow)\b', '↔', text)
    text = re.sub(r'\\(Leftrightarrow|Longleftrightarrow)\b', '⇔', text)
    text = re.sub(r'\\(uparrow|Uparrow)\b', '↑', text)
    text = re.sub(r'\\(downarrow|Downarrow)\b', '↓', text)

    # 2. LaTeX Comparison & Math operators
    text = re.sub(r'\\ge\b', '>=', text)
    text = re.sub(r'\\le\b', '<=', text)
    text = re.sub(r'\\geq\b', '>=', text)
    text = re.sub(r'\\leq\b', '<=', text)
    text = re.sub(r'\\neq\b', '!=', text)
    text = re.sub(r'\\ne\b', '!=', text)
    text = re.sub(r'\\times\b', '*', text)
    text = re.sub(r'\\approx\b', '≈', text)
    text = re.sub(r'\\pm\b', '±', text)
    text = re.sub(r'\\cdot\b', '*', text)
    text = re.sub(r'\\textbf\{([^{}]+)\}', r'**\1**', text)
    text = re.sub(r'\\text\{([^{}]+)\}', r'\1', text)
    text = re.sub(r'\\mathrm\{([^{}]+)\}', r'\1', text)
    text = re.sub(r'\\mathbf\{([^{}]+)\}', r'\1', text)
    text = re.sub(r'\\mathit\{([^{}]+)\}', r'\1', text)
    text = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1 / \2)', text)
    text = re.sub(r'\\(min|max|log|ln|sin|cos|tan|sum|prod|int|sqrt)\b', r'\1', text)

    # 3. Clean inline/block math delimiters
    def _replace_double_dollar(m):
        inner = m.group(1).strip()
        if '\n' in inner:
            return f"\n```\n{inner}\n```\n"
        return f"`{inner}`"

    text = re.sub(r'\$\$([\s\S]+?)\$\$', _replace_double_dollar, text)
    text = re.sub(r'\$([^\$\n]+?)\$', r'`\1`', text)
    text = text.replace('$$', '')
    return text


# ==========================================
# 5. INTENT-AWARE PROMPT BUILDER
# ==========================================

class IntentAwarePromptBuilder:
    @classmethod
    def build_prompt(
        cls,
        analysis: QueryAnalysis,
        context_str: str,
        user_name: str = "there",
        is_first_message: bool = True,
        history_summary: str = ""
    ) -> str:
        first_name = user_name.split()[0].capitalize() if user_name else "there"

        base_header = f"""You are a senior XortLogix High Level Technical Consultant & Solutions Architect.
User's Name: {first_name}
Is Opening Conversation: {is_first_message}
User Detected Intent: {analysis.intent}
Primary Objective: {analysis.objective}
"""

        if analysis.intent == "frontend_customization":
            intent_guidance = """
MISSION & ADAPTIVE STRUCTURE FOR GOHIGHLEVEL FRONTEND CUSTOMIZATION & SCRIPTS:
The user is building or requesting GoHighLevel frontend customizations (JavaScript, CSS, DOM lifecycle handlers, SPA events, external script loaders, or REST API calls).

Provide an authoritative, copy-paste ready technical blueprint structured as follows:

### 1. 🎯 Architecture & Execution Strategy
- Explain the Single Page Application (SPA) lifecycle in GoHighLevel: why DOM elements render dynamically and require dynamic observers instead of static onload scripts.
- Explain the role of `MutationObserver` (with debouncing), `routeChangeEvent` detection (e.g. for `contactsdetails`), external script injection (`checkforformula404`), and internal REST API helpers (`rest_api_call`).

### 2. ⚡ Complete Production JavaScript Blueprint
- Provide 100% complete, fully commented, bug-free JavaScript code wrapped in an IIFE.
- Include:
  * Dynamic script loader for external helpers / Formula404.
  * Debounced `MutationObserver` on `document.querySelector("body")` with `{ childList: true, subtree: true }`.
  * `routeChangeEvent` and history state listener to trigger route-specific handlers (like `contactsdetails`).
  * `rolesPermission()` function performing dynamic DOM injection / role-based UI modifications.
  * Internal `rest_api_call` helper for fetching live contact or pipeline data.

### 3. 🎨 Custom Dashboard Theme & White-Label CSS (If Applicable)
- High-specificity CSS targeting `#sidebar-v2`, `.hl_header`, `.card`, and custom buttons with `!important` to reliably override native HighLevel theme styling.

### 4. 📍 Injection & Setup Instructions
- Clearly specify where to paste the code:
  * Agency Level: Agency Settings → Company → Custom JS / Custom CSS.
  * Sub-Account Level: Settings → Custom Code or Funnel Step Settings.
- Testing and verification steps in the browser console.
"""

        elif analysis.intent == "blog_article_proofreading":
            intent_guidance = """
MISSION & ADAPTIVE STRUCTURE FOR GOHIGHLEVEL BLOG & ARTICLE PROOFREADING:
The user has provided a blog post, article, or content draft related to GoHighLevel (or requested proofreading for one).
Your job is to proofread the content, verify its technical accuracy against GoHighLevel's actual architecture and features, and evaluate whether each capability mentioned is possible NATIVELY in GHL or requires CUSTOM development.

Provide a thorough, well-structured review:

### 1. 📝 Overall Proofreading & Accuracy Verdict
- Summarize the quality, clarity, and technical correctness of the article.
- Note any outdated information (e.g. referencing deprecated API v1, legacy Triggers/Campaigns instead of Workflows, or inaccurate limits).

### 2. ⚖️ Native vs. Custom Feasibility Breakdown
Examine every claim, feature, or workflow strategy mentioned in the article and clearly classify it:
* 🟢 **Possible Natively in GHL:**
  - Detail the native feature, trigger, action, or setting (e.g. Workflows, Form/Survey Builder, Membership, Calendars, Pipelines, LC Email/Phone).
  - Note any specific native constraints or prerequisites (e.g. required sub-account settings).
* 🟡 **Native Workaround (No Code):**
  - If it's not a single 1-click feature, explain how it can be achieved natively without writing code (e.g. using If/Else branches, tags, custom fields, wait steps).
* 🟠 **Requires Custom Development:**
  - Clearly explain why native GoHighLevel cannot handle this out-of-the-box.
  - Describe the exact custom technical approach needed (e.g. Custom Code workflow action, Webhooks, REST API v2, OAuth marketplace apps, or frontend Custom JS/CSS via MutationObserver).
* 🔴 **Strictly Unsupported / Violates Platform Boundaries:**
  - Highlight any claims that are technically impossible or violate GHL terms, carrier compliance (A2P 10DLC), or security limits.

### 3. ✍️ Content & Terminology Corrections
- Highlight specific sentences, grammatical issues, or confusing passages that need rewriting.
- Standardize GHL terminology (e.g. "Sub-account" vs "child account", "Workflows" vs "Campaigns", "Location ID").

### 4. 💡 Pro Suggestions to Enhance the Article
- Suggest 2–3 actionable points, diagrams, or real-world tips that would make the article significantly more valuable and authoritative to readers.
"""

        elif analysis.intent == "native_feasibility_check":
            intent_guidance = """
MISSION & ADAPTIVE STRUCTURE FOR NATIVE VS. CUSTOM FEASIBILITY INQUIRY:
The user is asking whether a specific feature, workflow, or business requirement is possible NATIVELY in GoHighLevel or requires CUSTOM development (e.g., "is it possible natively?", "kya ye natively possible hai?").

Deliver a direct, definitive answer formatted clearly:

### 1. 🎯 Direct Feasibility Verdict
State the feasibility upfront immediately:
- 🟢 **YES — 100% Natively Supported** (Out-of-the-box standard GHL feature)
- 🟡 **YES — Via Native Workaround** (Possible natively using smart workflow logic / tags / custom fields without code)
- 🟠 **NO — Requires Custom Development** (Native GHL cannot do this alone; requires API v2, Webhooks, Custom Code actions, or Custom JS/CSS)
- 🔴 **NO — Not Supported in GoHighLevel** (Beyond platform capabilities or violates compliance)

### 2. ⚙️ How to Implement Natively (If Native or Workaround)
- State the exact navigation path: (e.g., Automations → Workflows → Add New Workflow).
- Detail the exact triggers, actions, and conditions required.
- Mention any native limitations or required GHL subscription tier.

### 3. 🛠️ Custom Implementation Strategy (If Custom Development is Required)
- Explain exactly what technical limitation exists natively.
- Outline the technical solution:
  * Backend API / Webhook (sending data to external service or Custom Code action in workflow).
  * REST API v2 (with appropriate endpoints and scopes).
  * Frontend injection (Custom JS / CSS with MutationObserver for UI changes).
- Provide sample code or payload structure where helpful.

### 4. 💡 Recommendation
- Give practical advice on whether the native route or the custom route is best for long-term scalability and maintenance.
"""

        elif analysis.intent == "job_posting_analysis":
            intent_guidance = """
MISSION & ADAPTIVE STRUCTURE FOR JOB DESCRIPTION & PROPOSAL GENERATION:
The user provided a Job Posting / Client Opportunity for GoHighLevel.
Produce a professional, concise, client-facing job proposal (target 500-750 words) that demonstrates understanding, answers client questions directly, and presents a practical technical approach.

Structure:
- **Opening:** Briefly show understanding of the client's core goal (e.g. headless/decoupled SaaS or automated GHL system) and establish relevant experience.
- **Relevant GHL Experience:** Highlight real, verified GHL projects (e.g. custom AI voice receptionist, API v2 integrations, webhooks, custom dashboards). Use placeholders like `[ADD ACTUAL PROJECT]` for any specific details to be supplied.
- **Answers to Client Questions:** Answer every client question directly with concrete technical honesty (differentiating native GHL vs custom UI/API, practical tech recommendations like Next.js/Node/FastAPI/Postgres/Redis, and honest demo placeholders `[ADD PORTFOLIO LINK]`).
- **Proposed Architecture:** Concise explanation of Frontend → Backend/API Layer → GoHighLevel.
- **Closing:** Confident, collaborative sign-off offering to discuss workflows and technical milestones.
"""

        elif analysis.intent == "technical_troubleshooting":
            intent_guidance = """
MISSION & ADAPTIVE STRUCTURE FOR TECHNICAL TROUBLESHOOTING:
Diagnose and resolve the issue systematically:
### 1. 🔍 Problem Diagnosis & Likely Root Causes
### 2. 🛠️ Step-by-Step Resolution
### 3. 🟡 Workarounds & Third-Party Fallbacks (If Applicable)
### 4. ✅ Verification & Testing Steps
"""

        elif analysis.intent == "system_architecture":
            intent_guidance = """
MISSION & ADAPTIVE STRUCTURE FOR SYSTEM / WORKFLOW ARCHITECTURE:
Provide an executive, ready-to-implement technical blueprint:
### 1. 🏗️ System Architecture Overview
### 2. ⚡ Step-by-Step GoHighLevel Configuration
### 3. 🛡️ Failsafes & Edge-Case Handling
"""

        elif analysis.intent == "business_strategy":
            intent_guidance = """
MISSION & ADAPTIVE STRUCTURE FOR GROWTH STRATEGY:
Provide actionable, high-ROI marketing & automation strategy covering funnels, nurturing, and KPIs.
"""

        elif analysis.intent == "comparison_evaluation":
            intent_guidance = """
MISSION & ADAPTIVE STRUCTURE FOR FEATURE / TOOL COMPARISON:
Compare and contrast features, benefits, use cases, and concrete recommendations.
"""

        elif analysis.intent == "factual_lookup":
            intent_guidance = """
MISSION FOR DIRECT FACTUAL QUERY:
Deliver a direct, crisp, and concise answer immediately without unnecessary boilerplate.
"""

        else:
            intent_guidance = """
MISSION FOR GENERAL TECHNICAL QUERY:
Start with a clear status banner (🟢 Native Feature / 🟡 Native Workaround / 🟠 Custom Development Required / ℹ️ Technical Overview). If the user asks whether something is possible natively, state the native vs custom feasibility upfront decisively. Then provide a clear, actionable guide synthesized from documentation.
"""

        rules = """
CORE CONSULTING & EXPERT PRINCIPLES:
1. FRONTEND JAVASCRIPT & DOM EXACTNESS:
   - HighLevel is an SPA. Scripts MUST use `MutationObserver` on `body` with debouncing (100-150ms) to avoid CPU spikes.
   - Listen to `routeChangeEvent` for instant tab and route transitions (e.g. `contactsdetails`).
   - Dynamic script loaders must be idempotent (e.g. check `typeof init_formula_404 === 'undefined'`).
   - REST API calls from frontend must handle errors and parse response objects safely.
2. STRICT CODE QUALITY (NO PLACEHOLDERS OR PSEUDOCODE):
   - Every script must be 100% complete, executable, and copy-paste ready.
   - Zero abbreviations (`...` or `# logic goes here`).
3. ABSOLUTELY NO RAW LATEX, ARROW COMMANDS, OR MATH DELIMITERS:
   - NEVER output LaTeX commands or delimiters (e.g. NEVER output \\rightarrow, \\leftarrow, \\Rightarrow, \\to, $$...$$, $...$, \\text{...}, \\ge, \\le, \\times, \\frac{...}{...}).
   - For sequential navigation steps or workflow transitions (e.g. Funnels → Select Funnel → Settings), ALWAYS use clean unicode arrow '→' or '->' (NEVER \\rightarrow).
4. GREETINGS & TONE:
   - First message: Greet politely by name ({first_name}).
   - Subsequent messages: Direct, professional, and crisp answers. Avoid arrogant or hyperbolic language.
5. PROPOSAL GENERATION & FACTUAL ACCURACY:
   - NEVER HALLUCINATE CANDIDATE EXPERIENCE: Never invent candidate experience, project counts, portal numbers, metrics, or client names.
   - Use clean placeholders such as `[ADD ACTUAL PROJECT]` or `[ADD PORTFOLIO LINK]` for unsupplied info.
   - Do NOT include internal meta-commentary like `[CANDIDATE INPUT REQUIRED]` or `[STRICT SOURCE SEPARATION]`.
6. NATIVE VS CUSTOM FEASIBILITY RESPONSES:
   - When asked whether something is possible natively in GoHighLevel (e.g. "is it possible natively?", "kya ye natively possible hai?"), ALWAYS give a direct feasibility verdict upfront:
     * 🟢 Natively Supported (out-of-the-box)
     * 🟡 Native Workaround (achievable natively using workflow logic, tags, custom fields without code)
     * 🟠 Requires Custom Development (needs REST API v2, Webhook, Custom Code workflow action, or Custom JS/CSS)
     * 🔴 Unsupported (strictly outside GHL platform boundaries)
   - Never be vague or leave the user guessing. Clearly explain the native steps if possible, or the exact technical method if custom development is required.
   - If the user asks in Urdu / Roman Urdu (e.g. "kya ye natively possible hai", "us k hisaab se jawab de"), respond naturally in the user's conversational tone while maintaining full technical accuracy.
"""

        full_prompt = f"""{base_header}
{intent_guidance}

{rules}

==================================================
KNOWLEDGE BASE CONTEXT:
==================================================
{context_str}

==================================================
USER QUERY:
==================================================
{analysis.raw_query}

ANSWER:"""

        return full_prompt


# ==========================================
# 6. MASTER RAG ENGINE ORCHESTRATOR
# ==========================================

class RAGEngine:
    @classmethod
    def process_query(
        cls,
        user_query: str,
        chroma_col,
        embed_model,
        user_name: str = "there",
        is_first_message: bool = True,
        top_k: int = 5,
        history: List[Dict[str, Any]] = None
    ) -> Tuple[QueryAnalysis, str, List[str]]:
        start_t = time.time()

        # 1. Query Understanding & Intent Analysis
        analysis = QueryUnderstandingEngine.analyze(user_query, user_name=user_name, history=history)
        print(f"🧠 [RAG Engine] Detected Intent: {analysis.intent} | Output Type: {analysis.output_type} | Complex: {analysis.is_complex}")
        if analysis.expanded_queries:
            print(f"🔍 [RAG Engine] Expanded Queries ({len(analysis.expanded_queries)}): {analysis.expanded_queries}")

        # 2. Conversational Fast-Path
        if analysis.is_conversational:
            return analysis, "", []

        # 3. Hybrid Retrieval & Reranking
        retrieved_chunks = HybridRetriever.search(
            analysis=analysis,
            chroma_col=chroma_col,
            embed_model=embed_model,
            top_k=top_k
        )
        print(f"📦 [RAG Engine] Retrieved Chunks: {len(retrieved_chunks)} | Retrieval Latency: {round((time.time() - start_t)*1000, 1)}ms")

        # 4. Context Assembly
        context_str, source_labels = ContextAssembler.assemble(
            analysis=analysis,
            chunks=retrieved_chunks,
            user_name=user_name,
            history=history
        )

        # 5. Intent-Aware Prompt Construction
        prompt = IntentAwarePromptBuilder.build_prompt(
            analysis=analysis,
            context_str=context_str,
            user_name=user_name,
            is_first_message=is_first_message
        )

        return analysis, prompt, source_labels
