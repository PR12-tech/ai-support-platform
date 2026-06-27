from app.agent.tools import (
    KnowledgeSearchTool,
    OrderLookupTool
)

TOOLS = {

    "knowledge_search": {

        "tool": KnowledgeSearchTool(),

        "parameters": {

            "question": "The customer's support question."
        }

    },

    "order_lookup": {

        "tool": OrderLookupTool(),

        "parameters": {

            "order_id": "The customer's support question."
        }

    }

}