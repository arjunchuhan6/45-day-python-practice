#update this code create 10 python file inside current folder with name program_1.py to program_10.py
import os

for i in range(1, 11):
    filename = f"program_{i}.py"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f'''# Python Program {i}

print("This is Python program {i}")
''')

print("10 Python files created successfully!")