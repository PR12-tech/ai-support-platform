from app.services.context_compressor import compress_context

question = "Can I get a refund and how long does it take?"

context = """
Customers may request a refund within 30 days.

Refund processing takes 5-7 business days.

Our company was founded in 2012.

Support is available Monday-Friday.
"""

compressed = compress_context(
    question,
    context
)

print(compressed)