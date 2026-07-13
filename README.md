# Bedside

**A standard for AI agents that operate tools for smart, high-judgment non-experts — manners you can ship and test, not only write.**

Most agent docs answer: *What is this codebase?*  
**Bedside** answers: *How do you treat the human in the loop?*

---

## Three artifacts

Bedside is not a single essay. It is **three distinct layers** — each its own directory:

```text
┌──────────────────────────────────────────────────────────┐
│  1. Contract   human-readable rules                      │  contract/
├──────────────────────────────────────────────────────────┤
│  2. Surface    tools encode manners                      │  surface/
├──────────────────────────────────────────────────────────┤
│  3. Eval       manners cannot rot                        │  eval/
└──────────────────────────────────────────────────────────┘
```

| Layer | Path | Artifact | Primary adopters |
|-------|------|----------|------------------|
| **Contract** | [`contract/`](contract/) | Normative principles, anti-patterns, `AGENTS.md` stub | Agent authors |
| **Surface** | [`surface/`](surface/) | CLI/TUI patterns, step machines, fail-closed recovery | Tooling authors |
| **Eval** | [`eval/`](eval/) | Rubric R1–R9, scorecard, known-bad/good fixtures | Eval / CI authors |

Read them in order if you are new. Pin a tag/commit of this repo; do not soft-fork the principles.

---

## Who this is for

### The operator

**Smart and high-judgment** in their domain; **low literacy** in the agent's tools (Git, shells, ports, cloud consoles, agent UIs). They own judgment and confirmation — not shell folklore.

### Adopters

| Role | Start here |
|------|------------|
| Agent authors | [`contract/`](contract/) |
| Tooling authors | [`surface/`](surface/) (+ contract) |
| Eval / CI authors | [`eval/`](eval/) (+ contract) |

---

## What Bedside is not

- Not "be friendly" or generic politeness
- Not end-customer product UX (different persona)
- Not a second codebase map (`AGENTS.md` still owns layout and build rules)
- Not a demand that power users abandon shortcuts they already know

**Operator care for the host path** — setup, tools, deploys, recoveries — so a smart non-expert does not get stranded.

---

## Principles (summary)

Normative text lives in [`contract/`](contract/). Summary only:

1. Assume low ops literacy, high judgment  
2. Do not dump a wall of shell  
3. Prefer doing over instructing  
4. Human acts: explicit, one step, dumb-simple  
5. Own first-time setup from zero  
6. Own scary surfaces in plain language  
7. Confirm in their words before irreversible/physical steps  
8. Never leave them at a cliff  
9. Teach only what Day 2 requires  

---

## Adoption checklist

Claim "we follow Bedside" when:

- [ ] **Contract:** agent-visible pin/link to [`contract/`](contract/); principles non-negotiable on the operator path  
- [ ] **Contract:** domain notes for first-run + one scary surface; one Day-2 leave-behind  
- [ ] **Surface:** at least one verb, error path, or step machine encodes manners — **or** dated plan  
- [ ] **Eval:** ≥1 known-bad and ≥1 known-good against the [rubric](eval/) — **or** dated plan  

Layer-local checklists: [contract](contract/README.md#contract-adoption-this-layer-only) · [surface](surface/README.md#surface-checklist-this-layer-only) · [eval](eval/README.md#eval-checklist-this-layer-only)

---

## Domain packs

Principles are universal; examples are not. Domain packs add persona notes, first-run paths, scary-surface glossaries, verbs, and fixtures — they **do not** rewrite the nine principles.

**Illustration:** embedded / host-first metal in [silico](https://github.com/tig/silico) (Help the operator / bedside manners → generalized here).

Other pack shapes: cloud first-deploy, data/ML bootstrap, on-prem appliance bring-up.

---

## Repo layout

```text
README.md           # this index
LICENSE             # Apache-2.0
contract/           # layer 1 — normative rules
surface/            # layer 2 — product patterns
eval/               # layer 3 — rubric + fixtures
  fixtures/
    known-bad/
    known-good/
```

---

## Status

**v0 — three layer artifacts; no required runner package yet.**

Welcome: clearer principles, domain packs, runner sketches, more fixtures, `BEDSIDE.md` conventions.

Origin: operator-care practice extracted from [silico](https://github.com/tig/silico), made reusable.

---

## License

Apache-2.0. See [LICENSE](LICENSE).
