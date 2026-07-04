import logging

logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

logging.getLogger("httpx").setLevel(logging.WARNING)

logging.getLogger("httpcore").setLevel(logging.WARNING)

logging.getLogger("huggingface_hub").setLevel(logging.WARNING)

logging.getLogger("sentence_transformers").setLevel(logging.WARNING)

logging.getLogger("transformers").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)