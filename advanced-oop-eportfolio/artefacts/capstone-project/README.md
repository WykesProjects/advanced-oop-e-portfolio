Capstone Project

This directory contains the capstone implementation for the Advanced Object-Oriented Design and Programming module.

The capstone demonstrates the application of advanced object-oriented design principles, design patterns, and secure coding practices in a realistic system context. The focus is on modular design, clear separation of responsibilities, extensibility, and testability.

How to run the application
From the capstone-project directory:

python3 -m src.app

This will execute the application and generate audit and alert logs based on example security events.

How to run the tests
From the capstone-project directory:

python3 -m pytest

Individual test files can also be run if required:

python3 -m pytest tests/test_events.py
python3 -m pytest tests/test_audit_log.py
python3 -m pytest tests/test_rules_and_detector.py

All tests are designed to validate core behaviour, including event handling, rule evaluation, alert generation, and audit logging.
