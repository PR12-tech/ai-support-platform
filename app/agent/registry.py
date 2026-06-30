from app.agent.tools import (
    KnowledgeSearchTool,
    OrderLookupTool,
    TicketLookupTool,
    EmailTool
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

            "order_id": "Order ID such as ORD1001"
        }

    },

    "ticket_lookup": {

         "tool": TicketLookupTool(),

         "parameters": {

             "ticket_id": "Support ticket ID such as TKT1001"
         }
     },

    "send_email": {

        "tool": EmailTool(),

        "parameters": {

            "to": "Recipient email address.",

            "subject": "Subject of the email.",

            "body": "Email content."
        }
    }

}


