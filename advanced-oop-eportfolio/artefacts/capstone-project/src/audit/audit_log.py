# Writes security events to an append-only audit log.
# Redacts common sensitive fields before writing.

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from src.domain.events import SecurityEvent


class AuditLog:
    # Simple file-based audit log for security events

    def __init__(self, path: Path) -> None:
        self._path = path
        self._path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event: SecurityEvent) -> None:
        # Appends a single event as a JSON line
        safe_event = self._redact(asdict(event))
        with self._path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(safe_event, default=str) + "\n")

    def _redact(self, data: dict[str, Any]) -> dict[str, Any]:
        # Redacts sensitive metadata fields
        redacted = dict(data)
        metadata = dict(redacted.get("metadata", {}))

        for key in ["password", "token", "secret", "card_number", "cvv", "pin"]:
            if key in metadata:
                metadata[key] = "[REDACTED]"

        redacted["metadata"] = metadata
        return redacted