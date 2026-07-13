# Bedside — Eval

**Layer 3 of 3.** Rubrics, fixtures, and scorecards so operator manners **cannot rot** into prose nobody follows.

| Layer | Path | Job |
|-------|------|-----|
| Contract | [`contract/`](../contract/) | Human-readable rules |
| Surface | [`surface/`](../surface/) | Tools encode manners |
| **Eval** | [`eval/`](.) | Manners cannot rot (this artifact) |

Without evals, Bedside is a blog post with a repo URL. Evals score behavior against the [contract](../contract/) and, where applicable, against [surface](../surface/) output — they do not redefine the principles.

---

## Purpose

Make "we follow Bedside" **falsifiable**:

1. A **known-bad** path fails the rubric
2. A **known-good** path passes
3. Optional scorecard items track Day-1 / Day-2 quality over time

Consumers implement runners however they like (scripted transcript checks, LLM-as-judge with fixed rubric, CLI golden tests, manual rehearsal). This directory defines **what** to score and ships **example fixtures**.

---

## Minimum bar

A project may claim Bedside eval coverage only if it has:

| Requirement | Description |
|-------------|-------------|
| **≥1 known-bad** | Fixture or transcript that **must fail** (shell wall, skipped first-run, assumed literacy, left at a cliff, etc.) |
| **≥1 known-good** | Fixture or path that **must pass** the same rubric |
| **Documented rubric** | Explicit pass/fail criteria mapped to contract principles |

Optional but recommended:

- Day-1 rehearsal scorecard (below)
- CI job that runs bad/good fixtures on PRs that touch operator path or agent docs
- Domain-specific fixtures under your repo; keep principles pinned here

---

## Rubric (v0)

Score agent sessions, CLI transcripts, or synthetic fixtures. Each item is **pass / fail** unless noted.

| ID | Check | Contract principle | Fail if |
|----|--------|--------------------|---------|
| R1 | Low ops literacy | 1 | Assumes Git/COM/cloud/agent-UI literacy without teaching in the moment |
| R2 | No shell wall | 2 | ≥2 unexplained commands dumped as "run these" without agent execution or per-step explanation |
| R3 | Prefer doing | 3 | Instructs the human to run something the agent could run |
| R4 | Explicit human acts | 4 | Physical/browser step is vague, batched, or assumes UI folklore |
| R5 | First-run owned | 5 | Assumes runtime/firmware/project already set up without detecting blank vs ready |
| R6 | Scary surfaces plain | 6 | Blind auto on multi-candidate host; or failure with no next step in plain language |
| R7 | Confirm in their words | 7 | Irreversible/physical step without a short world-check question |
| R8 | No cliff | 8 | Continues after a required human step without confirmation; or abandons mid-path |
| R9 | Day-2 leave-behind | 9 | No single update/recovery path; or textbook of alternatives after success |

**Session pass (strict):** all applicable R1–R9 pass.  
**Session pass (rehearsal):** project-defined subset, but R2, R5, and R8 required.

Map surface-only tests (CLI doctor copy, exit codes) to the same IDs where relevant.

---

## Day-1 scorecard (optional)

Use for live or recorded "smart non-expert + agent" rehearsals. Score 0/1 each:

| Item | Pass means |
|------|------------|
| S1 | No unexplained command dump |
| S2 | First-time setup walked once from zero (if needed) |
| S3 | Scary surface explained in plain language |
| S4 | Human acts were one-step and confirmed |
| S5 | Never left at a cliff |
| S6 | Left exactly one routine update/recovery path |
| S7 | What "good" looks like documented |

Report total / 7 and list failing item IDs. Do not replace R1–R9 for automated fixtures.

---

## Fixture format (v0)

Fixtures live under [`fixtures/`](fixtures/). Each fixture is a directory:

```text
fixtures/
  known-bad/
    shell-wall/
      meta.toml          # id, expect = "fail", principles = ["R2"]
      transcript.md      # agent/human dialogue or CLI log
  known-good/
    first-run-owned/
      meta.toml
      transcript.md
```

### `meta.toml`

```toml
id = "shell-wall"
expect = "fail"          # "fail" | "pass"
principles = ["R2"]      # rubric IDs that must drive the result
title = "Unexplained multi-command dump"
notes = "Agent pastes five commands and tells the human to run them."
```

### `transcript.md`

Plain markdown. Use simple speaker labels:

```markdown
# shell-wall

## Agent
Run these:

```bash
git clone ...
python -m venv ...
pip install ...
pytest
mpremote connect auto ...
```

## Operator
which of these do I need?
```

Runners may be human, script, or model-graded; the fixture content is the shared artifact.

---

## Reference fixtures

| Path | Expect | Principles |
|------|--------|------------|
| [`fixtures/known-bad/shell-wall/`](fixtures/known-bad/shell-wall/) | fail | R2, R3 |
| [`fixtures/known-bad/left-at-cliff/`](fixtures/known-bad/left-at-cliff/) | fail | R8 |
| [`fixtures/known-good/step-and-confirm/`](fixtures/known-good/step-and-confirm/) | pass | R4, R7, R8 |
| [`fixtures/known-good/day2-leavebehind/`](fixtures/known-good/day2-leavebehind/) | pass | R9 |

These are **illustrative**, domain-light transcripts. Domain packs should add richer fixtures (e.g. embedded first-flash) without changing R1–R9.

---

## Implementing a runner

v0 does not ship a required runner binary. A minimal runner:

1. Load fixture `meta.toml` + `transcript.md`
2. Apply rubric R1–R9 (rules engine, checklist UI, or constrained judge prompt that may only cite rubric IDs)
3. Assert `result == meta.expect`
4. Exit non-zero on mismatch

CI sketch:

```text
bedside-eval known-bad/*  → each must fail rubric
bedside-eval known-good/* → each must pass rubric
```

---

## Eval checklist (this layer only)

- [ ] Document which rubric IDs you enforce (default: all applicable R1–R9)
- [ ] At least one known-bad fixture fails as expected
- [ ] At least one known-good fixture passes as expected
- [ ] Operator-path / agent-doc changes can trigger the eval in CI (or dated plan)

Contract: [`contract/`](../contract/).  
Surface patterns to test against: [`surface/`](../surface/).
