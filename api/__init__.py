import pathway as pw

from .embedder import get_embedded_data, get_embeddings_index
from .prompt import prompt


def run(host, port):
    # Given a user question as a query from your API
    query, response_writer = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=QueryInputSchema,
        autocommit_duration_ms=50,
    )

    # Real-time data coming from external data sources such as jsonlines file
    data = pw.io.jsonlines.read(
        "./extracted_data", schema=DataInputSchema, mode="streaming"
    )

    # Compute embeddings for each document using the OpenAI Embeddings API
    embedded_data = get_embedded_data(context=data, data=data.doc)

    # Construct an index on the generated embeddings in real-time
    index = get_embeddings_index(embedded_data)

    # Generate embeddings for the query from the OpenAI Embeddings API
    embedded_query = get_embedded_data(context=query, data=pw.this.query)

    # Build prompt using indexed data
    responses = prompt(index, embedded_query, pw.this.query)

    # Feed the prompt to ChatGPT and obtain the generated answer.
    response_writer(responses)

    # Run the pipeline
    pw.run()


class DataInputSchema(pw.Schema):
    doc: str


class QueryInputSchema(pw.Schema):
    query: str
