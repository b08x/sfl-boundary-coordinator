# Migration decisions

Source: sfl-boundry.zip, SHA-256 89167a42e457c8b1522653f526cfdffee77feca5847e386b3bd6f900b14d452f. Original plugin version 0.3.0; portable definitions version 0.4.0. Input retained with private design-source attribution redacted in migration/antigravity/.

| Antigravity | OpenGAP |
|---|---|
| agents/*.md frontmatter | root and 11 recursive agent.yaml/SOUL.md/PROMPT.md/RULES.md definitions |
| mainAgent/subagent | root agent and explicit agents map |
| model: inherit | omitted model; host selects session model |
| tools and inheritance flags | host-contract.md capability obligations |
| review_packets MCP | preserved Python server plus three script tool definitions |
| plugin.json and mcp_config.json | provenance only; no active vendor bootstrap |

The current schema uses delegation mode explicit (not manual), risk tier standard (not medium), and workflow steps as an array. Older skill reference examples do not validate against this pinned schema.

Vendor-only skill frontmatter `user-invocable` is preserved as string metadata `source-user-invocable`; the active schema forbids that top-level field.

Public-source hygiene: both design-basis copies omit a private archive URL, personal attribution and archive-specific context. The supplied ZIP remains the authoritative original; the retained provenance tree is redacted in those files.
