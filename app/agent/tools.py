from app.services.rag_service import get_knowledge
from app.agent.base import BaseTool
from app.services.order_service import lookup_order
from app.tests.test_querywriter import question


class KnowledgeSearchTool(BaseTool):

    @property
    def name(self):

        return "knowledge_search"

    @property
    def description(self):

        return (
            "Searches the customer support "
            "knowledge base."
        )

    def execute(
            self,
            **kwargs
    ):

        question = kwargs["question"]

        return get_knowledge(
            question
        )

class OrderLookupTool(BaseTool):

    @property
    def name(self):

        return "order_lookup"

    @property
    def description(self):

        return (
            "Looks up an order using an order ID. "
            "Use this tool whenever the user asks "
            "about order status, tracking or delivery."
        )

    def execute(
            self,
            **kwargs
    ):

        order_id = kwargs["order_id"]

        return lookup_order(
            order_id
        )