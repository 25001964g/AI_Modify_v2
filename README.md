## User Guide
---------------------------------------------------------------
# Environment set up guide
Step 1: Install ollama(First time only)
Linux: curl -fsSL https://ollama.com/install.sh | sh
Windows: irm https://ollama.com/install.ps1 | iex

Step 2: Start server (Only for Virtual Environment)
ollama serve

Step 3: Add model to ollama (Need to add at first time)
add model: ollama pull [model_name] (expected llama3.2/ phi3.5(recommended))

Optional:
delete model: ollama rm [model_name]
view model list downloaded in ollama: ollama list

Library Required:
pandas: pip install pandas
----------------------------------------------------------------
# Testing file:
Baseline: python test_baseline.py
Baseline + Name Detection: python test_baseline_nameDetect.py
Baseline + Translator: python test_baseline_translator.py
Baseline + Validator: python test_baseline_validator.py
Full workflow: python test_combined_workflow.py

----------------------------------------------------------------
# Project File
Baseline: 
test_baseline.py

Harness1 (add format library): 
general_infomration.formatting.py
test_format.py

Harness2 (add name detection):
name_detection_component.name_detect.py
test_baseline_nameDetect.py

Harness3 (add translator): 
translator_component.order_translator.py
test_baseline_translator.py

Harness4 (add validator):
validator_component.order_extractor.py
validator_component.product_validator.py
test_baseline_validator.py

Full Workflow:
combined_component.c_format_order.py
combined_component.c_order_translator.py
combined_component.c_order_validator.py
test_combined_workflow.py

Sample Data:
email_data.py
general_information.product_list.py
general_information.status_list.py
--------------------------------------------------------------------