# Tests rules and detector alert publishing

from src.domain.events import SecurityEvent
from src.security.rules import HighValueTransferRule, FailedLoginBurstRule
from src.security.detector import ThreatDetector
from src.alerts.subscribers import AlertSubscriber


class CaptureSubscriber(AlertSubscriber):
    # Captures alerts for testing

    def __init__(self) -> None:
        self.alerts: list[SecurityEvent] = []

    def notify(self, alert_event: SecurityEvent) -> None:
        self.alerts.append(alert_event)


def test_high_value_transfer_rule_triggers() -> None:
    rule = HighValueTransferRule(threshold=500.0)

    e = SecurityEvent(
        event_type="transfer_initiated",
        account_id="ACC-1",
        actor_id="user-1",
        metadata={"amount": 750.0},
    )

    result = rule.evaluate(e)
    assert result.triggered is True
    assert result.severity == "high"


def test_failed_login_burst_rule_triggers_after_threshold() -> None:
    rule = FailedLoginBurstRule(max_failures=3)

    e1 = SecurityEvent("login_failed", "ACC-1", "user-1", {})
    e2 = SecurityEvent("login_failed", "ACC-1", "user-1", {})
    e3 = SecurityEvent("login_failed", "ACC-1", "user-1", {})

    assert rule.evaluate(e1).triggered is False
    assert rule.evaluate(e2).triggered is False
    assert rule.evaluate(e3).triggered is True


def test_detector_publishes_alert_event() -> None:
    capture = CaptureSubscriber()

    detector = ThreatDetector(
        rules=[HighValueTransferRule(threshold=500.0)],
        subscribers=[capture],
    )

    e = SecurityEvent(
        event_type="transfer_initiated",
        account_id="ACC-9",
        actor_id="user-9",
        metadata={"amount": 999.0},
    )

    detector.handle(e)

    assert len(capture.alerts) == 1
    alert = capture.alerts[0]
    assert alert.event_type == "suspicious_activity_detected"
    assert alert.metadata.get("source_event") == "transfer_initiated"