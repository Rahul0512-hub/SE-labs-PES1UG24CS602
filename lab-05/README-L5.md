# Lab 5: Static Code Analysis - Course Enrollment System

**Repository URL:** https://github.com/Rahul0512-hub/L5_52_course_enrollment_system
## About

This repository contains `course_enrollment_system.py`, a Python program that was analysed with three static analysis tools (Pylint, Bandit and Flake8) and then cleaned up by fixing the issues they reported.

## Files

| File / Folder | Description |
|---|---|
| `course_enrollment_system.py` | The cleaned and updated program |
| `reports/before/` | Pylint, Bandit and Flake8 reports before the fixes |
| `reports/after/` | Pylint, Bandit and Flake8 reports after the fixes |
| `Lab5_Issues_Table.docx` | Table of the issues found and how they were fixed |

## How to run

```bash
python3 -m venv venv
source venv/bin/activate
pip install pylint bandit flake8
python course_enrollment_system.py
```

## How to run the analysis

```bash
pylint course_enrollment_system.py
bandit -r course_enrollment_system.py
flake8 course_enrollment_system.py
```

## Name

Rahul Devendra Kagawad
PES1UG24CS602