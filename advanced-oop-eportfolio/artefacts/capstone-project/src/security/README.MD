This package contains the core security logic of the capstone project. It is responsible for evaluating security events against defined rules and determining whether those events represent suspicious or high-risk behaviour.

The security layer encapsulates rule evaluation and decision-making logic, keeping it independent from event generation, auditing, and alert delivery. This design supports flexibility and makes it easier to evolve detection strategies over time.

Key responsibilities of this package include:
    •	Defining and applying security rules
    •	Evaluating events based on risk and behaviour patterns
    •	Producing structured findings for downstream alerting

This approach aligns with secure-by-design principles and promotes maintainable, testable security logic.
