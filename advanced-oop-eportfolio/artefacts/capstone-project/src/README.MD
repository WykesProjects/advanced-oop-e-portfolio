This directory contains the core implementation of the Cyber Alert capstone system.
The code is organised using a modular structure to support clarity, testability, and
secure software design principles.

The implementation is divided into focused packages that separate responsibilities
and reduce coupling between components. Core domain concepts, such as security events,
are kept independent from supporting concerns such as auditing and alert notification.
This separation allows individual components to evolve without requiring changes to
unrelated parts of the system.

Directory overview:

domain/
Contains core domain definitions, including validated security event models used
throughout the system.

audit/
Provides append-only audit logging for security events. This module is responsible
for recording system activity in a consistent and auditable format.

security/
Contains detection rules and the threat detector. Rule evaluation logic is encapsulated
to allow new detection behaviour to be introduced without modifying the event
processing flow.

alerts/
Contains alert subscriber implementations that receive notifications when suspicious
activity is detected. This supports multiple alert outputs without coupling them to
detection logic.

This structure supports unit testing and incremental refactoring by keeping behaviour
isolated behind clear module boundaries and well-defined interfaces.
