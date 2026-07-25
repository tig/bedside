from pathlib import Path

from bedside.eval_engine import evaluate_fixture_dir, iter_fixture_dirs, score_transcript

REPO = Path(__file__).resolve().parents[1]
FIXTURES = REPO / "eval" / "fixtures"


def test_shipped_fixtures_match_expect():
    dirs = iter_fixture_dirs(FIXTURES)
    assert len(dirs) >= 4
    for d in dirs:
        report = evaluate_fixture_dir(d)
        assert report.ok, (report.fixture_id, report.reasons, report.tenet_pass)


def test_legacy_principles_key_still_read(tmp_path):
    """Fixtures written against the pre-tenets key keep working after a re-vendor."""
    d = tmp_path / "known-bad" / "legacy"
    d.mkdir(parents=True)
    (d / "meta.toml").write_text(
        'id = "legacy"\nexpect = "fail"\nprinciples = ["R2", "R3"]\n', encoding="utf-8"
    )
    (d / "transcript.md").write_text(
        (FIXTURES / "known-bad" / "shell-wall" / "transcript.md").read_text(
            encoding="utf-8"
        ),
        encoding="utf-8",
    )
    report = evaluate_fixture_dir(d)
    assert report.focus == ["R2", "R3"]
    assert report.ok


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
