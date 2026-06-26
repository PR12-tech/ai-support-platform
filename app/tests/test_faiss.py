from app.services.vector_store import (
    create_index,
    save_index,
    load_index
)

create_index(384)

save_index()

print(load_index())