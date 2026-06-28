# Environment set up guide
Step 1: Install ollama(First time only)
Linux: curl -fsSL https://ollama.com/install.sh | sh
Window: irm https://ollama.com/install.ps1 | iex

Step 2: Start server
ollama serve

Step 3: Add model to ollama (Need to add at first time)
add model: ollama pull [model_name] (expected llama3.2)

Optional:
delete model: ollama rm [model_name]
view model list downloaded in ollama: ollama list
