# Python Program 2: Activate a virtual environment

# First, make sure the .venv folder was created by Program 1.
# Run this command in PowerShell from your project folder:
# .\.venv\Scripts\Activate.ps1

# Explanation:
# .\              means the path starts in the current folder.
# .venv\          is the virtual environment folder.
# Scripts\        contains the environment's command-line scripts.
# Activate.ps1    activates the environment in PowerShell.

# After activation, PowerShell usually shows (.venv) before the prompt.
# This means python and pip now use the project's virtual environment.

# You can verify the active environment with:
# python -c "import sys; print(sys.executable)"

print("Program 2: Activate the environment with '.\\.venv\\Scripts\\Activate.ps1'")