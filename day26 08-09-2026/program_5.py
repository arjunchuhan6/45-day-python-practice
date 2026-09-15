# Python Program 5: Create requirements.txt

# Activate the virtual environment first:
# .\.venv\Scripts\Activate.ps1

# Save all installed packages and their exact versions:
# python -m pip freeze > requirements.txt

# Explanation:
# pip freeze lists packages installed in the active environment.
# The > symbol sends that list into a file.
# requirements.txt stores package names and versions for this project.

# Example contents:
# requests==2.32.5
# urllib3==2.5.0

print("Program 5: Create requirements.txt with 'python -m pip freeze > requirements.txt'")
