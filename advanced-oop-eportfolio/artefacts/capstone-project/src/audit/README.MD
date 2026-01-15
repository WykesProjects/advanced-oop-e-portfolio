This package is responsible for audit logging within the capstone system. It provides a central mechanism for recording security events in a structured and consistent manner.

The audit layer ensures that all significant actions and events can be traced after execution, supporting accountability, forensic analysis, and compliance requirements. It is deliberately isolated from detection and alerting logic to maintain a clear separation of responsibilities.

Key responsibilities of this package include:
    •	Persisting security events in an append-only audit log
    •	Ensuring audit records are consistent, timestamped, and tamper-resistant in structure
    •	Decoupling event recording from detection and alert generation

By treating audit logging as a first-class concern, this package reinforces secure coding practices and demonstrates how non-functional requirements such as traceability and accountability can be addressed through object-oriented design.
