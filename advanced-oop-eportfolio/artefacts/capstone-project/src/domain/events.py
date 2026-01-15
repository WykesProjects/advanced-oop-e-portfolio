# Defines a simple security event model used across the system.

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


class ValidationError(ValueError):
    # Raised when invalid event data is provided
    pass


@dataclass(frozen=True)
class SecurityEvent:
    # Represents a single security-related action in the system

    event_type: str
    account_id: str
    actor_id: str
    metadata: dict[str, Any] = field(default_factory=dict)
    occurred_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        # Basic validation to ensure required fields are present
        if not self.event_type.strip():
            raise ValidationError("event_type is required")
        if not self.account_id.strip():
            raise ValidationError("account_id is required")
        if not self.actor_id.strip():
            raise ValidationError("actor_id is required")