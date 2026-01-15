# Demo runner for the capstone monitoring system

from pathlib import Path

from src.domain.events import SecurityEvent
from src.audit.audit_log import AuditLog
from src.alerts.subscribers import ConsoleAlertSubscriber, FileAlertSubscriber
from src.security.rules import HighValueTransferRule, FailedLoginBurstRule
from src.security.detector import ThreatDetector


def main() -> None:
    # Audit log writes events to an append-only file
    audit = AuditLog(Path("audit.log"))

    # Subscribers receive alerts (Observer pattern)
    console_alert = ConsoleAlertSubscriber()
    file_alert = FileAlertSubscriber(Path("alerts.log"))

    # Rules are interchangeable strategies (Strategy pattern)
    rules = [
        HighValueTransferRule(threshold=500.0),
        FailedLoginBurstRule(max_failures=3),
    ]

    detector = ThreatDetector(
        rules=rules,
        subscribers=[console_alert, file_alert],
    )

    events = [
        SecurityEvent(
            event_type="transfer_initiated",
            account_id="ACC-001",
            actor_id="user-123",
            metadata={"amount": 750.0, "destination_account": "ACC-900"},
        ),
        SecurityEvent(
            event_type="login_failed",
            account_id="ACC-001",
            actor_id="user-123",
            metadata={},
        ),
        SecurityEvent(
            event_type="login_failed",
            account_id="ACC-001",
            actor_id="user-123",
            metadata={},
        ),
        SecurityEvent(
            event_type="login_failed",
            account_id="ACC-001",
            actor_id="user-123",
            metadata={},
        ),
    ]

    for event in events:
        audit.append(event)
        detector.handle(event)


if __name__ == "__main__":
    main()