# Contributing

Contributions are welcome. This list is generated from `gen_readme.py`, so please edit the structured entries there and run:

```bash
python3 gen_readme.py
python3 gen_readme.py --check
```

## Entry Criteria

- Prefer real, installable, public projects over blog-only announcements.
- Link the canonical upstream repository, not an unmaintained fork.
- Keep descriptions factual, one sentence long, and specific about what the tool does.
- Add `⚠️` when the project has a restrictive, non-commercial, unclear, or missing license.
- Add `🔬` for papers, benchmarks, datasets, and research frameworks.
- Use `🟠` for commercial products that still provide meaningful open components.

## Entry Format

```markdown
- **[name](repo-url)** 🟢/🔬/🟠/⚠️ — One-line description. *(maintainer/org)* <stars badge> <last-commit badge>
  - **Sources:** [upstream A](url) · [upstream B](url)
  - **Related:** [sibling tool](url) · [related project](url)
```

The badges are generated automatically by `gen_readme.py`; do not paste badge Markdown by hand in the source data.
