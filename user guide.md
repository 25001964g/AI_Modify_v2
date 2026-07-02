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
Baseline + Extractor: python test_baseline_extractor.py
Baseline + Validator: python test_baseline_validator.py
Full workflow: python order_full_modifier.py
----------------------------------------------------------------
# Project File
Baseline: 
test_baseline.py

Harness1 (add format library): 
formatting.py
test_format.py

Harness2 (add name detection):
name_detect.py
test_baseline_nameDetect.py

Harness3 (add extractor): 
order_extractor_plain.py
test_baseline_extractor.py

Harness4 (add validator):
order_extractor.py
product_validator.py
test_baseline_validator.py

Full Workflow:
order_full_modifier.py

Sample Data:
email_data.py
product_list.py
status_list.py
--------------------------------------------------------------------