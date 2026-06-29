## User Guide
# Environment set up guide
Step 1: Install ollama(First time only)
Linux: curl -fsSL https://ollama.com/install.sh | sh
Windows: irm https://ollama.com/install.ps1 | iex

Step 2: Start server (Only for github codespace)
ollama serve

Step 3: Add model to ollama (Need to add at first time)
add model: ollama pull [model_name] (expected llama3.2/ phi3.5(recommended))

Optional:
delete model: ollama rm [model_name]
view model list downloaded in ollama: ollama list
----------------------------------------------------------------
# Project File
Baseline: 
test_baseline.py

Harness1 (add format library): 
formatting.py
test_format.py

Harness2 (add order validator): 
order_validator.py
test_validation.py

Harness3 (add name detection):
name_detect.py
test_customer_name.py

Sample Data:
email_data.py
product_list.py
status_list.py

test
