from app.agent.parser import parse_tool_response

response = """
```json
{
    "tool": "knowledge_search",
    "arguments": {
        "question": "Can I get a refund?"
    }
}
"""

tool_name, arguments = parse_tool_response(response)

print(tool_name)
print(arguments)
