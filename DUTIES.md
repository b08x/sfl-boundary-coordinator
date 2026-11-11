# Segregation of duties

The canonical machine-readable policy is `agent.yaml` → `compliance.segregation_of_duties`. Do not maintain a second policy copy here. Strict validation checks role assignments; session, credential and tool isolation are host obligations, not guarantees conferred by YAML. Judges approve only the current revision. Coordinator aggregates, author composes, broker retrieves.

| Agent | Duty | Host capability |
|---|---|---|
| `sfl-boundary-claim-examiner` | advisor | supplied material |
| `sfl-boundary-docs-ideational-judge` | checker | inline packet only |
| `sfl-boundary-docs-interpersonal-judge` | checker | inline packet only |
| `sfl-boundary-docs-textual-judge` | checker | inline packet only |
| `sfl-boundary-documentation-author` | maker | scoped document I/O |
| `sfl-boundary-evidence-auditor` | advisor | supplied material |
| `sfl-boundary-evidence-broker` | retriever | read-only codebase-memory |
| `sfl-boundary-mechanism-tracer` | advisor | supplied material |
| `sfl-boundary-modality-calibrator` | advisor | supplied material |
| `sfl-boundary-relational-editor` | advisor | supplied material |
| `sfl-boundary-satirical-reframer` | advisor | supplied material |

All models use host/session selection: manifests omit model preferences to preserve source `model: inherit` intent without inventing an OpenGAP model identifier.
