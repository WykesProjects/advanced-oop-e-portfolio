This directory contains the core implementation of the capstone system. The code is organised using a modular, layered structure to support maintainability, scalability, and secure design.

The implementation is divided into focused packages that separate responsibilities and reduce coupling between components. Domain models and event definitions are kept independent from infrastructure concerns such as logging and alert delivery. Security logic is encapsulated within dedicated modules, allowing detection rules to evolve without changes to unrelated components.

Directory overview
domain contains core entities and validated security event models used throughout the system.
audit contains append-only audit logging with redaction to prevent sensitive data from being recorded.
security contains detection rules and the threat detector, applying a strategy-based approach for extensible rule evaluation.
alerts contains alert subscribers that receive suspicious activity notifications, supporting an observer style approach for multiple alert outputs.

This structure supports testing and refactoring by keeping behaviours isolated and encouraging clear interfaces between modules.
