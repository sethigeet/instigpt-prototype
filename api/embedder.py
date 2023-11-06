from pathway.stdlib.ml.index import KNNIndex
import pathway as pw
from llm_app.model_wrappers import SentenceTransformerTask

EMBEDDING_DIMENSIONS = 384
transformer = SentenceTransformerTask("sentence-transformers/all-MiniLM-L6-v2")


def get_embedded_data(context, data):
    return context + context.select(vector=transformer.apply(data))


def get_embeddings_index(embedded_data):
    return KNNIndex(
        embedded_data.vector, embedded_data, n_dimensions=EMBEDDING_DIMENSIONS
    )


def concat_with_titles(**kwargs) -> str:
    combined = [f"{title}: {value}" for title, value in kwargs.items()]
    return ", ".join(combined)


def transform(data):
    return data.select(
        doc=pw.apply(concat_with_titles, **data),
    )
