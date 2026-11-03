# Student Management System

A beginner-friendly, console-based Student Management System developed in Python using Object-Oriented Programming (OOP).

## Features

- Add a student
- Display all student records
- Search for a student using roll number
- Update a student's marks
- Delete a student record
- Calculate the average of three subject marks
- Validate marks and prevent duplicate roll numbers

## OOP Concepts Used

1. **Class and Objects:** `Student` and `StudentManagementSystem` are classes. Individual student records are objects of the `Student` class.
2. **Constructor:** The `__init__()` method initializes student details and the management system.
3. **Encapsulation:** The marks are stored in the private attribute `__marks`.
4. **Methods:** Functions such as `display()`, `update_marks()` and `calculate_average()` define the behaviour of objects.

## Requirements

- Python 3
- No external libraries are required.

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python student_management.py
   ```

## Project Structure

```text
student-management-system/
├── student_management.py
├── README.md
└── sample_output.txt
```

## Data Storage Note

Student records are stored in a Python list while the program is running. The records are not saved permanently; they are cleared when the program exits.

## Author

Add your name here.
