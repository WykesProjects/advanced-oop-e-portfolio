This package is responsible for handling alert generation within the capstone project. Alerts are raised when predefined security rules or thresholds are triggered by incoming events.

The alerting logic is intentionally separated from detection and auditing to ensure a clear division of responsibilities. This allows alert mechanisms to be modified or extended without affecting how events are detected or logged.

Key responsibilities of this package include:
    •	Receiving evaluated security findings from the detection layer
    •	Generating human-readable alerts with severity levels
    •	Persisting alerts for review and operational visibility

This separation supports scalability and future extensibility, such as integrating external notification systems or dashboards.
