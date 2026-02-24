# codex-skill-enhancer reference policy

Use this file to guide reference selection when enhancing skills.

## Allowed source types (preferred order)

1. Official product documentation (primary vendor docs)
2. Official standards documentation (for example, Markdown or YAML specs)
3. Primary project documentation in the target repository

## Disallowed as primary evidence

- Personal blogs, forums, and social posts when official documentation exists
- AI-generated summaries without a link to official upstream documentation

## Minimum reference requirements per run

- Include at least 2 official sources when external guidance affects decisions.
- Include at least 1 official source for each major standards-related change (examples: markdown rules, YAML structure, testing guidance).
- Provide references in the final output as:
  - Source title
  - URL
  - One-line relevance note

## Suggested official source starting points

- OpenAI developer or product documentation: https://platform.openai.com/docs
- GitHub Copilot documentation: https://docs.github.com/en/copilot
- Cursor documentation: https://docs.cursor.com
- YAML language specification: https://yaml.org/spec/
- CommonMark specification: https://spec.commonmark.org
