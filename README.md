# Student Management System V1.0

A beginner-friendly Python Student Management System that allows users to add, view, search, update, and delete student records. The project also uses file handling to save student data permanently in a text file.

## 📌 Project Overview

The Student Management System is a console-based Python project created to practice and demonstrate fundamental Python programming concepts.

The program stores student records using lists and dictionaries and provides a menu-driven interface for managing those records.

Student data is saved in student.txt, allowing records to remain available even after the program is closed.

## ✨ Features

- Add a new student
- View all student records
- Search for a student using their roll number
- Update student information
- Delete a student record
- Automatically load existing records when the program starts
- Save updated records to a text file
- Input validation for the main menu
- Menu-driven console interface

## 🛠️ Technologies Used

- Python
- Lists
- Dictionaries
- Functions
- if-elif-else
- for and while loops
- break and return
- String methods
- File handling
- Text file storage

## 📂 Project Structure

Student-Management-System/
│
├── student_management.py
├── student.txt
└── README.md

## 📋 Student Record Format

Each student is stored in the following format:

Roll,Name,Age,Branch,Marks

Example:

101,Moksh,19,CSE,95
102,Rahul,20,ECE,89

## 🚀 How to Run

1. Make sure Python is installed on your computer.
2. Clone or download this repository.
3. Open the project folder in your terminal or VS Code.
4. Run the Python program using:

python student_management.py

5. Use the menu to manage student records.

## 🎮 Menu Options

1. Add Student
2. View All Students
3. View Student
4. Update Student
5. Delete Student
6. Exit

### 1. Add Student

Allows the user to enter:

- Roll number
- Name
- Age
- Branch
- Marks

The new record is added to the student list and saved to the file.

### 2. View All Students

Displays all currently stored student records along with the total number of students.

### 3. View Student

Searches for a student using their roll number and displays their complete record if found.

### 4. Update Student

Allows the user to update:

- Name
- Age
- Branch
- Marks

The roll number is kept unchanged.

### 5. Delete Student

Searches for a student using their roll number and removes the selected record from the student list and saved file.

### 6. Exit

Closes the Student Management System.

## 💾 File Handling

The project uses a text file to provide basic data persistence.

### Loading

When the program starts:

student.txt
     ↓
Read each line
     ↓
strip()
     ↓
split(",")
     ↓
Create dictionary
     ↓
Add dictionary to students list

### Saving

Whenever student data is changed:

students list
     ↓
Take each dictionary
     ↓
Convert it into a comma-separated string
     ↓
Write to student.txt

The file is opened in "w" mode when saving so that the file contains the latest version of the student records instead of repeatedly appending duplicate records.

## 🧠 Concepts Practiced

This project helped practice several important Python concepts:

- Variables
- User input
- Lists
- Dictionaries
- Indexing
- Loops
- Conditional statements
- Functions and parameters
- Returning values
- break
- return
- String manipulation
- split()
- strip()
- open()
- Reading files
- Writing files
- Closing files
- Basic CRUD operations

## 🔮 Future Improvements

Possible improvements for future versions:

- Add stronger input validation
- Prevent duplicate roll numbers
- Validate age and marks as numbers
- Add confirmation before deleting a student
- Improve the search system
- Use with open() for safer file handling
- Use a cleaner data-storage format such as CSV or JSON
- Add sorting by marks, name, or roll number
- Add a graphical user interface
- Add database support

## 📈 Version

Version: V1.0

### Current Status

✅ Add Student
✅ View All Students
✅ Search Student
✅ Update Student
✅ Delete Student
✅ File Loading
✅ File Saving
✅ Menu System

## 👨‍💻 Author

Moksh

This project was created as part of my Python learning and project-building practice.
