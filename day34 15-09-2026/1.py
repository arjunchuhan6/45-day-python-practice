import os

folder = "Day34 15-09-2026"
os.makedirs(folder, exist_ok=True)

for i in range(1, 11):
    filename = os.path.join(folder, f"program_{i}.py")

    with open(filename, "w", encoding="utf-8") as file:
        file.write(f'''# Python Program {i}

print("This is Python program {i}")
''')

print("10 Python files created successfully!")
print("Location:", os.path.abspath(folder))