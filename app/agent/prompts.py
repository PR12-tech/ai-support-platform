TOOL_SELECTION_PROMPT = """

Choose the best tool for the user's request.

Return only one tool for now.

Available tools:

{tools}

Question:

{question}

Choose the SINGLE best tool.

Reply ONLY in valid JSON.

Example 1:

{{
    "tool": "knowledge_search",
    "arguments": {{
        "question": "Can I get a refund?"
    }}
}}

Example 2:

{{
    "tool": "order_lookup",
    "arguments": {{
        "order_id": "ORD1001"
    }}
}}

If no tool is appropriate, reply with:

{{
    "tool": "NONE",
    "arguments": {{}}
}}
"""

OBSERVATION_PROMPT = """
You are an AI agent.

The user asked:

{question}

The tool used:

{tool}

The tool returned:

{result}

Decide whether another tool is required.

Reply ONLY with one of these:

CONTINUE

or

FINISH
"""