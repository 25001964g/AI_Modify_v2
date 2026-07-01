# Project Overview
# Background:

# Proposed Workflow (Pending):
Email -> LLM Processor -> order management system (OMS)

### LLM:
-> Retrieval -> Scan Order -> Draft order (json) -> Modifier -> Second Draft order (json) -> Order Status Check (Pending) + Security Check(Pending) -> 
Retrieval: Format, Status list, product list
Modifier: Modify First Draft output with validator


Harness:
1. Output Format
2. Order Verifier (item status check and name detection)
3. Order Status Check (For auto processing or require human checking) (Pending)
4. Security Check (Pending)

## Order processor
V0:
Baseline

V1.1 (V0 + Retrieval):
- V0
- Product list
- Status list
- Formatting

V1.2 (V1.1 + order validation check):
- V1
- order extractor
- order validator
- name detect

V1.3 (V1.2 + order process controller):
Pending

Testing Procedure:
1. V0
2. V1.1:
3. V1.2:
4. V1.2 without V1.1:
5. V1.3 :
6. V1.3 without V1.2:

## Security check
V2.1 (V0 + Retrieval):
Pending

V2.2 (V2.1 + checking/verfifier):
Pending

Testing procedure:
V2.1:
V2.2:
V2.2 without V2.1
