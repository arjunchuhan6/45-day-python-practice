# Python Program 10: Recreate an environment from requirements.txt

# Create a new environment named recreated_env:
# python -m venv recreated_env

# Activate the new environment in PowerShell:
# .\recreated_env\Scripts\Activate.ps1

# Install the saved dependencies:
# python -m pip install -r requirements.txt

# Explanation:
# python -m venv creates a clean, isolated environment.
# requirements.txt contains the package names and versions from the old environment.
# pip install -r reads that file and installs the same dependencies.

# You can check the recreated packages with:
# python -m pip list

print("Program 10: Recreated an environment from requirements.txt")
