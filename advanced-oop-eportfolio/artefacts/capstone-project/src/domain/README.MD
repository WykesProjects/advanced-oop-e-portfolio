This package defines the core domain concepts used throughout the capstone system. It contains the foundational models that represent security-related activity in a consistent and validated form.

The primary responsibility of this layer is to model security events in a way that is independent of detection logic, storage, or alerting mechanisms. By isolating domain concepts, the system ensures that higher-level components operate on well-defined and trustworthy data structures.

Key responsibilities of this package include:
    •	Representing security events with validated attributes
    •	Enforcing basic data integrity and invariants
    •	Providing a stable interface used by detection rules, audit logging, and alerting components

This separation aligns with object-oriented design principles by keeping domain logic cohesive and preventing cross-cutting concerns from leaking into core models.
