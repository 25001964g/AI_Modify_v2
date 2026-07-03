# Project Overview
# Background:
Assume that a B2B company will receive email order. In this project, we try to help the sales team to extract the the order required information and verify the information correctness, and then we will export the result via json format to send the data to Order Management System, Database or csv for daily order operation. Therefore, the project try to reduce the workload of administration work for the sales team.

# Proposed Workflow:
See Workflow.png
![alt text](Workflow.png)

### LLM:
-> Retrieval -> Scan Order -> Draft order (json) -> Modifier -> Verified order ->
Retrieval: Format, Status list, product list
Modifier: Modify First Draft output with validator

Harness:
1. Output Format: To help the LLM to perform designed format for order processing.
2. Order Verifier: To verify and modify the formatted output.
2.1: Name detection: To help the LLM to check what should be the customer name.
2.2: Translator/Extractor: To help the LLM to translate and extract correct information for .
2.3: Validator: To help the LLM to match data via dataframe, especially classifying the status.

Test Procedure:
1. Baseline
2. Baseline + Format
3. Baseline + Name detection
4. Baseline + Extractor
5. Baseline + Validator
6. Combined Workflow

Expected Output:
1. follow the structure of general_information.formatting.py
2. product_name should be in English

