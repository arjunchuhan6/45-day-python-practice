from io import TextIOWrapper
import os

folder = "Day40 21-09-2026"
os.makedirs(folder, exist_ok=True)

for i in range(1, 11):
    filename: str = os.path.join(folder, f"program_{i}.py")

    with open(filename, "w", encoding="utf-8") as file: TextIOWrapper:
        file.write(f'''# Python Program {i}''')

print("10 Python files created successfully!")
print("Location:", os.path.abspath(folder))