## Student Gradebook & Course Manager

**Name: Sara Nazari**
Project Title: Student Gradebook & Course Manager

## Overview
I developed this project for my Python programming final. The main goal was to build a clean, terminal-based application to manage the academic workflow for students, including courses, assessments, and grades.

## What This Program Does
- Student Management: I can add, view, search, update, and delete student records.
- Course & Enrollment: Allows creating courses and enrolling students.
- Assessments & Grades: I can define quizzes, exams, or projects and record grades for enrolled students.
- Reporting: It automatically calculates averages and generates reports for each student.

## Classes I Created
- Student — stores student ID, name, email, and enrolled courses.
- Course — stores course code, name, enrolled students, and assessments.
- Assessment — parent class for graded work (title, max score, percentage calculation).
- Quiz, Exam, Project — child classes of Assessment with their own display and feedback logic.
- Gradebook — connects everything: manages students, courses, grades, and reports.

## Technical Implementation (OOP)
I focused on clean Object-Oriented Programming (OOP) to make the code maintainable:

- Encapsulation: Used in the Student class to protect the 'student_id' attribute (private attribute with a getter).
- Inheritance: I created an Assessment base class with child classes (Quiz, Exam, Project).
- Method Overriding: I customized the 'display_info' and'grade_message' methods in each child class to handle specific feedback differently.

## Creative Features
- **Dashboard:** A simple summary view of the total number of students and courses.
- **Letter Grades:** I added logic to convert numerical averages into letter grades (A-F) to make reports more readable.

## How to Run
Simply run the following command in your terminal:
python main.py