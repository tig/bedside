from pathlib import Path

import pytest

from bedside.eval_engine import (
    evaluate_fixture_dir,
    iter_fixture_dirs,
    load_meta,
    score_transcript,
)

REPO = Path(__file__).resolve().parents[1]
FIXTURES = REPO / "eval" / "fixtures"


def test_shipped_fixtures_match_expect():
    dirs = iter_fixture_dirs(FIXTURES)
    assert len(dirs) >= 4
    for d in dirs:
        report = evaluate_fixture_dir(d)
        assert report.ok, (report.fixture_id, report.reasons, report.tenet_pass)


def test_renamed_principles_key_errors_loudly(tmp_path):
    """The old key must fail with guidance, not silently widen focus to all tenets."""
    meta = tmp_path / "meta.toml"
    meta.write_text(
        'id = "legacy"\nexpect = "fail"\nprinciples = ["R2"]\n', encoding="utf-8"
    )
    with pytest.raises(ValueError, match="'principles' is now 'tenets'"):
        load_meta(meta)


def test_shell_wall_fails_r2_r3():
    text = (FIXTURES / "known-bad" / "shell-wall" / "transcript.md").read_text(
        encoding="utf-8"
    )
    p, reasons = score_transcript(text)
    assert p["R2"] is False
    assert p["R3"] is False


def test_step_and_confirm_passes_focus():
    text = (
        FIXTURES / "known-good" / "step-and-confirm" / "transcript.md"
    ).read_text(encoding="utf-8")
    p, _ = score_transcript(text)
    assert p["R5"] is True
    assert p["R8"] is True
    assert p["R9"] is True


def test_silent_work_fails_r4():
    text = (FIXTURES / "known-bad" / "silent-work" / "transcript.md").read_text(
        encoding="utf-8"
    )
    p, reasons = score_transcript(text)
    assert p["R4"] is False
    assert any("R4" in r for r in reasons)


def test_visible_progress_passes_r4():
    text = (
        FIXTURES / "known-good" / "visible-progress" / "transcript.md"
    ).read_text(encoding="utf-8")
    p, _ = score_transcript(text)
    assert p["R4"] is True


def test_filed_without_asking_fails_r11():
    text = (
        FIXTURES / "known-bad" / "filed-without-asking" / "transcript.md"
    ).read_text(encoding="utf-8")
    p, reasons = score_transcript(text)
    assert p["R11"] is False
    assert any("R11" in r for r in reasons)


def test_compound_with_consent_passes_r11():
    text = (
        FIXTURES / "known-good" / "compound-with-consent" / "transcript.md"
    ).read_text(encoding="utf-8")
    p, _ = score_transcript(text)
    assert p["R11"] is True


def test_choice_wall_fails_r2_r4():
    text = (FIXTURES / "known-bad" / "choice-wall" / "transcript.md").read_text(
        encoding="utf-8"
    )
    p, reasons = score_transcript(text)
    assert p["R2"] is False
    assert p["R5"] is False
    assert any("choice wall" in r for r in reasons)


def test_structured_choice_passes_r2_r4():
    text = (
        FIXTURES / "known-good" / "structured-choice" / "transcript.md"
    ).read_text(encoding="utf-8")
    p, _ = score_transcript(text)
    assert p["R2"] is True
    assert p["R5"] is True
