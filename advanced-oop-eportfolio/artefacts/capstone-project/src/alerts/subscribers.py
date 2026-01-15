# Alert subscribers receive suspicious activity notifications.
# This supports the Observer pattern by allowing multiple outputs.

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from src.domain.events import SecurityEvent


class AlertSubscriber(ABC):
    # Observer interface for receiving alert events

    @abstractmethod
    def notify(self, alert_event: SecurityEvent) -> None:
        raise NotImplementedError


class ConsoleAlertSubscriber(AlertSubscriber):
    # Sends alerts to the console for demonstration purposes

    def notify(self, alert_event: SecurityEvent) -> None:
        print(
            f"ALERT: {alert_event.metadata.get('reason', '')} "
            f"account={alert_event.account_id} actor={alert_event.actor_id} "
            f"severity={alert_event.metadata.get('severity', 'low')}"
        )


class FileAlertSubscriber(AlertSubscriber):
    # Writes alerts to a file as an additional channel

    def __init__(self, path: Path) -> None:
        self._path = path
        self._path.parent.mkdir(parents=True, exist_ok=True)

    def notify(self, alert_event: SecurityEvent) -> None:
        line = (
            f"{alert_event.occurred_at} "
            f"{alert_event.account_id} "
            f"{alert_event.actor_id} "
            f"{alert_event.metadata.get('severity', 'low')} "
            f"{alert_event.metadata.get('reason', '')}\n"
        )
        with self._path.open("a", encoding="utf-8") as f:
            f.write(line)