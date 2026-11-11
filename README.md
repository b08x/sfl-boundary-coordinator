# SFL Boundary Coordinator

R.U.T.H. (Records Uncertainty, Traces History) coordinates evidence-backed boundary analysis and SFL documentation review. OpenGAP is the canonical format. The root coordinates 11 specialists: six original analytical/satirical advisors, an evidence broker, a documentation author, and three independent metafunction judges. Only the author edits authorized document deliverables.

The hybrid workflow uses explicit delegation for scoping, retrieval, advisors and authoring, followed by a fixed blind-audit → evidence → cross-examination → gate-check DAG for each immutable candidate. Two repair rounds maximum; satire requires explicit request. Audit mode does not edit the candidate.

## Validate

Python 3 with jsonschema and PyYAML is required for repository checks. Packet tools require jsonschema only.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/validate_repository.py
.venv/bin/python -m unittest discover -s tests -v
```

Vendored upstream schemas are pinned to OpenGAP commit `d7a8e2edb54b942d6b4635cdd8b919ebd23e5da5`. Manifests, workflows, tools and skills are checked offline against that revision.

With a separately installed OpenGAP CLI (upstream package `@open-gitagent/opengap`, package version inspected: 0.5.0):

```bash
opengap validate -d .
opengap validate -d . --compliance
opengap export -f claude-code -d .
opengap export -f openai -d .
```

Run CLI validation for each child directory as well. CLI/export and live model execution require target-host verification; local schema validation does not establish adapter behavior.

## Runtime setup

Read [the host contract](docs/host-contract.md) before execution. Configure a read-only codebase-memory MCP server for the broker; no endpoint, credentials or index are bundled. Packet helpers are portable script tools in `tools/`, with the original stdio MCP server retained in `scripts/review_mcp.py`. Host binds document I/O and lifecycle operations, enforces fresh tool-free judge sessions, and maps workflow outputs. Models use host/session selection as in the source plugin.

See [duties and delegation](DUTIES.md), [migration decisions](docs/migration.md), and [review protocol](references/review-protocol.md). `migration/antigravity/` retains the source plugin as provenance, with private design-source attribution redacted and is excluded from active role discovery. The packet helper checks consistency when called; empirical verification and runtime permissions remain separate obligations.
