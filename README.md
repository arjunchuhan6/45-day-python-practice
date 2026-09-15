# 45-Day Python Practice

A structured Python learning repository containing 450 practice questions across 45 days. The course moves from Python fundamentals to object-oriented programming, files, databases, APIs, Git, FastAPI, testing, and a final project.

## What You Will Practice

- Python syntax, variables, operators, input, and strings
- Conditions, loops, functions, and comprehensions
- Lists, tuples, sets, and dictionaries
- File handling, CSV, JSON, and exception handling
- Object-oriented programming and modules
- Virtual environments and package management
- SQLite and SQL fundamentals
- HTTP, APIs, FastAPI, CRUD, authentication, and testing
- Git and GitHub workflows
- Project planning, debugging, documentation, and deployment preparation

## Repository Structure

Each dated directory contains the exercises for one practice day. Directory names preserve the original study dates and revision labels.

```text
45-Day Python Practice/
|-- day1 .../                  # Python fundamentals
|-- day8 .../                  # Lists, tuples, sets, and dictionaries
|-- day15 .../                 # Functions, files, and exceptions
|-- day22 .../                 # OOP and intermediate Python
|-- day29 .../                 # SQL, databases, APIs, and Git
|-- day36 .../                 # FastAPI and backend development
|-- day43 .../                 # Final project challenge
|-- 45-Day_Python_Practice_450_Questions.docx
`-- README.md
```

The exact folder names include dates, for example `day34 15-09-2026`. Open the folder for the day you are studying and run its Python files individually.

## Requirements

- Python 3.10 or newer
- Git
- A code editor such as VS Code
- Optional: a GitHub account for remote backup and collaboration

Check your installations on Windows:

```powershell
py --version
git --version
```

If `py` is unavailable, use `python` in its place.

## Clone and Use the Repository

### 1. Clone the repository

Replace the URL with the actual GitHub URL after the repository has been published.

```powershell
git clone https://github.com/arjunchuhan6/<repository>.git
cd <repository>
```

### 2. Create a virtual environment

A virtual environment keeps project packages separate from your global Python installation.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run PowerShell as your normal user and use:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Then activate the environment again.

### 3. Run a practice program

Use the relative path in quotes because folder names contain spaces.

```powershell
py ".\day1 14-08-26\1.py"
py ".\day34 15-09-2026\program_1.py"
```

You can also open the repository in VS Code:

```powershell
code .
```

### 4. Install optional packages

Most early exercises use Python's standard library. For the FastAPI section, install the required tools inside the virtual environment:

```powershell
py -m pip install --upgrade pip
py -m pip install fastapi uvicorn
```

Save installed packages when a project begins using external dependencies:

```powershell
py -m pip freeze > requirements.txt
```

### 5. Update your local copy

```powershell
git pull
```

## Recommended Daily Workflow

1. Read the day's topic before writing code.
2. Solve all 10 questions without copying a solution.
3. Run each file and test normal, boundary, and invalid input.
4. Refactor repeated logic into functions where appropriate.
5. Write a short note about what you learned.
6. Commit completed work with a clear message.

Example Git workflow:

```powershell
git status
git add .
git commit -m "Complete day 1 Python exercises"
git push
```

## 45-Day Roadmap

### Days 1-7: Python Fundamentals

| Day | Topic | Questions |
|---|---|---:|
| 1 | Python basics: output, variables, types, arithmetic, and f-strings | 1-10 |
| 2 | Operators and input: conversion, salary, interest, and calculators | 11-20 |
| 3 | Strings: length, indexing, slicing, case, replacement, and formatting | 21-30 |
| 4 | Conditions: comparisons, eligibility, grades, and login logic | 31-40 |
| 5 | `for` loops: ranges, tables, sums, powers, and factorials | 41-50 |
| 6 | `while` loops: input loops, totals, countdowns, and guessing | 51-60 |
| 7 | Revision: core problems and a Number Guessing Game | 61-70 |

**Milestone:** Complete the Number Guessing Game.

### Days 8-14: Collections

| Day | Topic | Questions |
|---|---|---:|
| 8 | Lists: creation, indexing, updates, insertion, removal, and reversing | 71-80 |
| 9 | List methods: sorting, searching, counting, totals, and averages | 81-90 |
| 10 | Tuples and sets: unpacking, conversion, uniqueness, union, and intersection | 91-100 |
| 11 | Dictionaries: keys, values, items, updates, deletion, and `get()` | 101-110 |
| 12 | Nested data: student and employee records | 111-120 |
| 13 | List and dictionary comprehensions | 121-130 |
| 14 | Contact Management System | 131-140 |

**Milestone:** Build a Contact Management System.

### Days 15-21: Functions, Files, and Exceptions

| Day | Topic | Questions |
|---|---|---:|
| 15 | Functions: parameters, return values, and reusable calculators | 141-150 |
| 16 | Function arguments: defaults, keywords, `*args`, and `**kwargs` | 151-160 |
| 17 | Lambda, `map()`, `filter()`, `zip()`, and `enumerate()` | 161-170 |
| 18 | Text files: read, write, append, search, and a Notes application | 171-180 |
| 19 | CSV and JSON data | 181-190 |
| 20 | Exceptions: `try`, `except`, `else`, `finally`, `raise`, and custom errors | 191-200 |
| 21 | Expense Tracker | 201-210 |

**Milestone:** Build an Expense Tracker that saves data to JSON.

### Days 22-28: OOP and Intermediate Python

| Day | Topic | Questions |
|---|---|---:|
| 22 | Classes, objects, attributes, methods, and student management | 211-220 |
| 23 | Constructors, default values, display methods, and update methods | 221-230 |
| 24 | Inheritance, encapsulation, polymorphism, and class design | 231-240 |
| 25 | Built-in modules, custom modules, and packages | 241-250 |
| 26 | Virtual environments, `pip`, and `requirements.txt` | 251-260 |
| 27 | Iterators, generators, decorators, and regular expressions | 261-270 |
| 28 | Bank Management System | 271-280 |

**Milestone:** Build a Bank Management System with validation, transaction history, JSON storage, and error handling.

### Days 29-35: SQL, Databases, APIs, and Git

| Day | Topic | Questions |
|---|---|---:|
| 29 | SQL basics: databases, tables, CRUD, columns, and records | 281-290 |
| 30 | SQL filtering: `WHERE`, logical operators, `LIKE`, ordering, limits, and aggregates | 291-300 |
| 31 | Advanced SQL: grouping, aggregate functions, and joins | 301-310 |
| 32 | Python with SQLite: parameterized queries and database classes | 311-320 |
| 33 | HTTP and APIs: methods, status codes, JSON responses, and errors | 321-330 |
| 34 | Git and GitHub: initialization, branches, commits, remotes, and pushes | 331-340 |
| 35 | Student Management System with Python and SQLite | 341-350 |

**Milestones:** Create a Student Management System and publish the project with Git and GitHub.

### Days 36-42: FastAPI and Backend Development

| Day | Topic | Questions |
|---|---|---:|
| 36 | FastAPI basics, routes, JSON responses, server execution, and Swagger | 351-360 |
| 37 | Path parameters, query parameters, searching, filtering, and validation | 361-370 |
| 38 | CRUD endpoints with SQLite | 371-380 |
| 39 | Validation, custom errors, status codes, and database errors | 381-390 |
| 40 | Authentication, authorization, password hashing, tokens, and protected routes | 391-400 |
| 41 | Unit tests, API tests, README writing, and endpoint documentation | 401-410 |
| 42 | Employee backend project with registration, CRUD, database, and authentication | 411-420 |

**Milestone:** Complete a documented employee REST API.

### Days 43-45: Final Challenge

| Day | Topic | Questions |
|---|---|---:|
| 43 | Plan and develop the final project: database, models, routes, CRUD, validation, and authentication | 421-430 |
| 44 | Improve the final project: debugging, structure, type hints, tests, docs, and GitHub release | 431-440 |
| 45 | Final assessment covering Python, data structures, functions, databases, and a Student Management System | 441-450 |

**Final outcome:** Build and document a complete Python application with a database, validation, error handling, tests, and a clean Git history.

## Project Milestones

- **Day 7:** Number Guessing Game
- **Day 14:** Contact Management System
- **Day 21:** Expense Tracker
- **Day 28:** Bank Management System
- **Day 35:** Student Management System
- **Day 42:** Employee REST API
- **Day 45:** Final Python assessment and project review

## Progress Tracking

Use this checklist to track the major milestones:

- [ ] Days 1-7: Python fundamentals completed
- [ ] Day 7: Number Guessing Game completed
- [ ] Days 8-14: Collections completed
- [ ] Day 14: Contact Management System completed
- [ ] Days 15-21: Functions, files, and exceptions completed
- [ ] Day 21: Expense Tracker completed
- [ ] Days 22-28: OOP and intermediate Python completed
- [ ] Day 28: Bank Management System completed
- [ ] Days 29-35: SQL, SQLite, APIs, and Git completed
- [ ] Day 35: Student Management System completed
- [ ] Days 36-42: FastAPI and backend development completed
- [ ] Day 42: Employee REST API completed
- [ ] Days 43-45: Final project and assessment completed

## Contribution and Practice Notes

This repository is primarily a personal learning workspace. When revisiting an exercise, prefer improving the existing solution, adding input validation, writing tests, and recording what changed in the commit message.

Keep secrets, virtual environments, cache folders, and generated files out of Git. A typical `.gitignore` should include `.venv/`, `__pycache__/`, and local database files when they are not part of an exercise.

## Author

Created and maintained by **Arjun Chuhan**.

- GitHub: [@arjunchuhan6](https://github.com/arjunchuhan6)
- Focus: Python practice, backend development, databases, APIs, and continuous learning

## License

This repository is intended for educational and personal practice use.

Copyright (c) 2026 arjunchuhan6. All rights reserved.
