# Host contract

These definitions describe an agent system; they do not install a scheduler.

1. Load each role's files. Resolve shared schemas and references at the repository root and pass complete contracts inline. Judges get no filesystem tools. Child skills are local copies so standalone role discovery resolves them.
2. Bind coordinator delegation and local packet tools. Resolve script paths relative to tools/, regardless of current working directory. Alternatively bind scripts/review_mcp.py as stdio MCP, using an absolute Python interpreter and script path. Its names are prepare_blind, prepare_cross, check_final; hyphenated OpenGAP tool aliases are separate script entry points.
3. Bind only broker read-only codebase-memory tools listed in its PROMPT.md. Supply exact project/revision, coverage and query pagination. No graph server or index is installed. Bind author scoped document I/O only. Advisors use supplied text or authorized read-only files. All other shell/network/write privileges stay disabled.
4. Start NEW judge sessions at every phase and revision. Three blind judgments must finish before peer findings or standalone broker evidence are shared. A fresh packet in an old conversation is not isolation.
5. Before review-candidate, coordinator retrieves planning evidence, optionally consults advisors and delegates authoring. Audit uses the supplied original with no author writes. Optional satire requires explicit user request and the same review budget.
6. Run workflows/review-candidate.yaml once per immutable candidate. It is a portable procedure, not a bundled runner. Host binds each returned object to the declared output key (packet, judgment, evidence, gates, result), resolves expressions, and aborts on exceptions. The action-only gates step is coordinator work, not a named external tool.
7. For repairs, coordinator adjudicates and sends changes to author, assigns a NEW revision/hash and reruns the full candidate workflow. At most two repair rounds per task, including satire. Track repair count outside the candidate DAG. Exhaustion returns PARTIAL/BLOCKED. accepted:false is a failed approval even when tool execution succeeds.
8. Acceptance is bounded to the exact reviewed text and source revision. No rewritten final synthesis after acceptance. Validate packet shapes and references. The helper verifies declared consistency, not truth, runtime isolation, or that the host really ran judges independently.

Exports must be inspected for role files, tool bindings and lifecycle support. Export success does not meet this contract. Missing capabilities block review rather than permitting an unrestricted substitute.
