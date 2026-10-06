# ISRM v1.0 - Reproducible Validation

This directory contains executable validation assets for the internal ISRM v1.0 validation.

## Run

```bash
python validation/reference_validation.py
python validation/edge_case_validation.py
```

Python 3.x is sufficient; only the standard library is used.

Expected results:
- Reference implementations: 69 applicable PASS, 0 FAIL, 0 ERROR.
- Edge cases: 60 PASS, 0 FAIL, 0 ERROR.
- Randomized invariant testing: 50,000 iterations per tested invariant family, with zero observed violations in the published run.

The randomized families cover authority monotonicity, uncertainty non-creation/preservation, Candidate Action != Authorized Action, idempotency semantics and delegation intersection.

These are internal validation/falsification assets, not independent certification. They do not prove completeness, novelty, safety, security, legal compliance or suitability as a national or international standard.

Canonical ISRM v1.0: https://doi.org/10.5281/zenodo.23115842
