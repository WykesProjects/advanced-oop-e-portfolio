# Defines detection rules used to identify suspicious activity.
# Each rule is a strategy that can be added without changing the detector.

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.events import SecurityEvent


@dataclass(frozen=True)
class RuleResult:
    triggered: bool
    reason: str = ""
    severity: str = "low"


class DetectionRule(ABC):
    # Strategy interface for detection rules

    @abstractmethod
    def evaluate(self, event: SecurityEvent) -> RuleResult:
        raise NotImplementedError


class HighValueTransferRule(DetectionRule):
    # Flags transfers above a configured threshold

    def __init__(self, threshold: float) -> None:
        self._threshold = threshold

    def evaluate(self, event: SecurityEvent) -> RuleResult:
        if event.event_type != "transfer_initiated":
            return RuleResult(triggered=False)

        amount = float(event.metadata.get("amount", 0.0))
        if amount >= self._threshold:
            return RuleResult(
                triggered=True,
                reason=f"High value transfer: {amount}",
                severity="high",
            )
        return RuleResult(triggered=False)


class FailedLoginBurstRule(DetectionRule):
    # Flags repeated failed logins within a time window (count based)

    def __init__(self, max_failures: int) -> None:
        self._max_failures = max_failures
        self._failures: dict[str, int] = {}

    def evaluate(self, event: SecurityEvent) -> RuleResult:
        if event.event_type != "login_failed":
            return RuleResult(triggered=False)

        key = f"{event.account_id}:{event.actor_id}"
        self._failures[key] = self._failures.get(key, 0) + 1

        if self._failures[key] >= self._max_failures:
            return RuleResult(
                triggered=True,
                reason=f"Repeated failed login attempts: {self._failures[key]}",
                severity="medium",
            )

        return RuleResult(triggered=False)