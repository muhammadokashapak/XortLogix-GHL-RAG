import os
import sys

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from rag_engine import QueryUnderstandingEngine, IntentAwarePromptBuilder, RAGEngine

print("=" * 70)
print("🚀 TESTING GHL FRONTEND CUSTOMIZATION & RAG INTENT ENGINE")
print("=" * 70)

# Test 1: Frontend Customization & Reference Script
print("\n[TEST 1] Testing Frontend Customization & Reference Script...")
frontend_query = """// Code advise // Mutationobserver in which i monitor the dome so i if any change in dome so he can tell me and if i find my changable place so i can apply my code
let target = document.querySelector("body");
let observer = new MutationObserver(() => { rolesPermission() })
let config = { childList: true, subtree: true, }
observer.observe(target, config)
// this is basically when any route change so he can tell me routeChangeEvent
window.addEventListener('routeChangeEvent', (() => { let location = window.location.href.includes("contactsdetails"); }));
async function checkforformula404(callback = function () { }) { var formula404 = document.createElement('script'); formula404.id = 'formulaloadedf404'; formula404.src = "https://scripts.jdfunnel.com/script.php?id=webworker_init404formula"; formula404.onload = async function () { callback(); }; if (typeof init_formula_404 === 'undefined') { document.head.append(formula404); } else { callback(); } }
checkforformula404(async () => {
});
await rest_api_call("contacts/0YMWokxfopxwxDT8KD9A","GET")"""

analysis_1 = QueryUnderstandingEngine.analyze(frontend_query, user_name="Okasha")
print(f"Detected Intent: {analysis_1.intent}")
print(f"Core Entities: {analysis_1.core_entities}")
print(f"Output Type: {analysis_1.output_type}")
print(f"Expanded Queries: {analysis_1.expanded_queries}")

assert analysis_1.intent == "frontend_customization", f"Expected frontend_customization, got {analysis_1.intent}"
assert any("mutationobserver" in e.lower() for e in analysis_1.core_entities) or "MutationObserver" in analysis_1.core_entities
assert analysis_1.is_complex is True

# Test Prompt Generation
prompt_1 = IntentAwarePromptBuilder.build_prompt(analysis_1, "Sample Context with MutationObserver and routeChangeEvent", user_name="Okasha")
assert "MISSION & ADAPTIVE STRUCTURE FOR GOHIGHLEVEL FRONTEND CUSTOMIZATION" in prompt_1
assert "rolesPermission()" in prompt_1 or "rolesPermission" in prompt_1
print("✅ Test 1 Passed! Frontend Customization successfully recognized and structured.")

# Test 2: Standard API / Architecture Query
print("\n[TEST 2] Testing Architecture Query...")
arch_query = "How to build an automated appointment booking workflow with triggers, pipeline stages and SMS reminders in GoHighLevel?"
analysis_2 = QueryUnderstandingEngine.analyze(arch_query, user_name="Okasha")
assert analysis_2.intent == "system_architecture", f"Expected system_architecture, got {analysis_2.intent}"
print(f"✅ Test 2 Passed! Intent: {analysis_2.intent}")

# Test 3: Simple Factual Query
print("\n[TEST 3] Testing Factual Query...")
fact_query = "What is the base URL for GoHighLevel REST API v2?"
analysis_3 = QueryUnderstandingEngine.analyze(fact_query, user_name="Okasha")
assert analysis_3.intent == "factual_lookup", f"Expected factual_lookup, got {analysis_3.intent}"
print(f"✅ Test 3 Passed! Intent: {analysis_3.intent}")

print("\n" + "=" * 70)
print("🎉 ALL TEST SUITES PASSED SUCCESSFULLY!")
print("=" * 70)
