# Runs detection rules over incoming events and publishes alerts to subscribers.

from __future__ import annotations

from src.domain.events import SecurityEvent
from src.security.rules import DetectionRule
from src.alerts.subscribers import AlertSubscriber


class ThreatDetector:
    # Applies rule strategies and notifies alert subscribers when triggered

    def __init__(self, rules: list[DetectionRule], subscribers: list[AlertSubscriber]) -> None:
        self._rules = rules
        self._subscribers = subscribers

    def handle(self, event: SecurityEvent) -> None:
        # Evaluates each rule against the event
        for rule in self._rules:
            result = rule.evaluate(event)

            if result.triggered:
                alert = SecurityEvent(
                    event_type="suspicious_activity_detected",
                    account_id=event.account_id,
                    actor_id=event.actor_id,
                    metadata={
                        "source_event": event.event_type,
                        "reason": result.reason,
                        "severity": result.severity,
                    },
                )

                for subscriber in self._subscribers:
                    subscriber.notify(alert)