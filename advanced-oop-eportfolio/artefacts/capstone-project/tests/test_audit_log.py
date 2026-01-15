# Tests audit log writing and redaction

import tempfile
from pathlib import Path

from src.audit.audit_log import AuditLog
from src.domain.events import SecurityEvent


def test_audit_log_appends_line() -> None:
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "audit.log"
        log = AuditLog(path)

        e = SecurityEvent(
            event_type="login_failed",
            account_id="ACC-1",
            actor_id="user-1",
            metadata={"attempt": 1},
        )

        log.append(e)
        content = path.read_text(encoding="utf-8").strip()
        assert content != ""


def test_audit_log_redacts_sensitive_fields() -> None:
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "audit.log"
        log = AuditLog(path)

        e = SecurityEvent(
            event_type="login_attempt",
            account_id="ACC-1",
            actor_id="user-1",
            metadata={"password": "secret-value", "token": "abc"},
        )

        log.append(e)
        content = path.read_text(encoding="utf-8")

        assert "secret-value" not in content
        assert "abc" not in content
        assert "[REDACTED]" in content