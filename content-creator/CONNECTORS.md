# Connectors - Content Creator

This plugin can integrate with external tools via MCP (Model Context Protocol).

## Available Connectors

Currently, no external connectors are configured. The plugin works standalone with all its skills and commands.

## Adding Connectors

To add integrations, edit the `.mcp.json` file with your MCP server configurations:

```json
{
  "mcpServers": {
    "service-name": {
      "type": "http",
      "url": "https://mcp.service.com/mcp"
    }
  }
}
```

## Recommended Integrations

For enhanced functionality, consider connecting:

- **Notion** - For content calendar and planning
- **Canva** - For design asset creation
- **HubSpot** - For marketing automation
- **Ahrefs** - For SEO research
- **Slack** - For team notifications

## Local Scripts

This plugin includes Python scripts that can be run locally:

| Script | Purpose |
|--------|---------|
| `seo_analyzer.py` | Analyze content for SEO |
| `hashtag_generator.py` | Generate relevant hashtags |
| `hook_generator.py` | Generate viral hooks |
| `trend_tracker.py` | Track trending topics |

Run scripts from the `scripts/` directory.
