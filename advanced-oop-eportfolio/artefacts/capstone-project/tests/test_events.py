# Tests validation on SecurityEvent

import pytest

from src.domain.events import SecurityEvent, ValidationError


def test_event_requires_event_type() -> None:
    with pytest.raises(ValidationError):
        SecurityEvent(event_type="", account_id="ACC-1", actor_id="user-1")


def test_event_requires_account_id() -> None:
    with pytest.raises(ValidationError):
        SecurityEvent(event_type="login_failed", account_id="", actor_id="user-1")


def test_event_requires_actor_id() -> None:
    with pytest.raises(ValidationError):
        SecurityEvent(event_type="login_failed", account_id="ACC-1", actor_id="")


def test_event_accepts_valid_input() -> None:
    e = SecurityEvent(
        event_type="login_failed",
        account_id="ACC-1",
        actor_id="user-1",
        metadata={"attempt": 1},
    )
    assert e.event_type == "login_failed"
    assert e.account_id == "ACC-1"
    assert e.actor_id == "user-1"