from app.services.rag_service import get_knowledge
from app.agent.base import BaseTool
from app.services.order_service import lookup_order
from app.services.sql_service import execute_sql
from app.services.ticket_service import lookup_ticket
from app.services.email_service import send_email



class KnowledgeSearchTool(BaseTool):

    @property
    def name(self):

        return "knowledge_search"

    @property
    def description(self):

        return (
            "Use for refund policies, shipping policies, "
            "returns, cancellations, warranties, FAQs, "
            "and other customer support documentation."
        )

    def execute(
            self,
            **kwargs
    ):

        question = kwargs["question"]

        knowledge = get_knowledge(
            question
        )

        return {
            "success": knowledge is not None,
            "type": "knowledge",
            "data": knowledge
        }


class OrderLookupTool(BaseTool):

    @property
    def name(self):

        return "order_lookup"

    @property
    def description(self):

        return (
            "Use ONLY when the user asks about a specific order, "
            "mentions an order ID like ORD1001, "
            "or asks for tracking or delivery status."
        )

    def execute(
            self,
            **kwargs
    ):

        order_id = kwargs["order_id"]

        service_result = lookup_order(
            order_id
        )

        return {
            "success": service_result["success"],
            "type": "order",
            "data": service_result
        }


class TicketLookupTool(BaseTool):

    @property
    def name(self):

        return "ticket_lookup"

    @property
    def description(self):

        return (
            "Use ONLY when the user asks about a support ticket, "
            "mentions a ticket ID like TKT1001, "
            "or asks for ticket status, priority, or assigned support agent."
        )

    def execute(
            self,
            **kwargs
    ):

        ticket_id = kwargs["ticket_id"]

        service_result = lookup_ticket(
            ticket_id
        )

        return {
            "success": service_result["success"],
            "type": "ticket",
            "data": service_result
        }


class EmailTool(BaseTool):

    @property
    def name(self):

        return "send_email"

    @property
    def description(self):

        return (
           "Use ONLY when the user explicitly asks to send an email. "
           "Extract ONLY the recipient email address. "
           "The email subject and body will be generated automatically from the current context."
        )

    def execute(
            self,
            **kwargs
    ):
        service_result = send_email(

            kwargs["to"],

            kwargs["subject"],

            kwargs["body"]
        )

        return {
            "success": service_result["success"],
            "type": "email",
            "data": service_result
        }

class SQLTool(BaseTool):

    @property
    def name(self):

        return "sql_search"

    @property
    def description(self):

        return (

            "Use ONLY for analytical questions involving "
            "orders or support tickets.\n"

            "Examples:\n"

            "- How many shipped orders are there?\n"
            "- Show cancelled orders.\n"
            "- List high priority tickets.\n"
            "- Show open tickets.\n\n"

            "Do NOT use when the user provides a specific "
            "order ID or ticket ID."

        )

    def execute(
            self,
            **kwargs
    ):

        question = kwargs["question"]

        return execute_sql(
            question
        )