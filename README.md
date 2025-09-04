# Employee Management System (Console Edition)

## Overview
This command-line Employee Management System helps you **add, search, update, list, and delete** employee records entirely in memory.  
It was built to demonstrate mastery of Python control structures, data structures, and basic search algorithms under exam conditions.

## Key Features
- **CRUD operations** through an interactive text menu
- Input validation for **names, dates, salaries, and unique IDs**
- Dual-index search:  
  - O(1) **hash look-up** by full name  
  - O(*n*) **linear search** by identification number
- Clean, modular code in a single file (`sistema_empleados.py`)

## Data Structures & Algorithms
| Purpose                         | Structure / Algorithm | Big-O (average) |
|---------------------------------|-----------------------|-----------------|
| Primary storage                 | Python `dict`         | O(1) insert / get |
| Fast search by *full name*      | Secondary `dict` index | O(1) |
| Search by *ID number*           | Linear scan of values | O(n) |
| Duplicate-ID detection          | Set membership test   | O(1) |
| Input loops & menus             | `while` / `for`       | — |

Validation routines ensure:
1. **Date format** (DD/MM/YYYY) using `datetime.strptime`.
2. **Positive salary** via `float()` conversion.
3. **Unique IDs** by probing the main dictionary.
4. **Minimum length** for names.

---

## Features
- **Add** a new employee with validation of name, unique ID, salary and hire date.  
- **Search** employees by full name or identification number.  
- **Update** job title, department or salary for an existing record.  
- **Delete** an employee with confirmation.  
- **List** every employee currently stored in memory via a clear tabular view.  

---

## Requirements
* **Python 3.8+** (standard library only – no third-party packages).

---

## Quick Start

1) Clone or download the repository
2) Open a terminal inside the project folder

`python sistema_empleados.py`

You’ll be greeted by a menu like this:

    ==================================================
    EMPLOYEE MANAGEMENT SYSTEM

    1. Add new employee

    2. Search employee

    3. Update employee information

    4. Delete employee

    5. List all employees

    6. Exit


Follow the on-screen prompts.  
All data lives **only in RAM**; closing the program clears the records—this is intentional for the exam.

---

## Educational Context
This code was developed for the final exam in the *Design and Logic of Programming* course.

The objective was to prove competence in:

- Designing appropriate **data structures**
- Implementing **search & validation algorithms**
- Writing clean, well-documented Python code

---

## License
Released **for educational purposes only**.  
Feel free to study or adapt it, but it comes **without any warranty**.

