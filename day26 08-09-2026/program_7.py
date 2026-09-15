# Python Program 7: Freeze dependencies

# Activate the virtual environment first:
# .\.venv\Scripts\Activate.ps1

# Display all installed packages with their exact versions:
# python -m pip freeze

# Save the dependency list into requirements.txt:
# python -m pip freeze > requirements.txt

# Explanation:
# pip freeze creates a snapshot of the current environment.
# Each package is shown in package==version format.
# This snapshot helps recreate the same environment later.

print("Program 7: Freeze dependencies with 'python -m pip freeze'")
