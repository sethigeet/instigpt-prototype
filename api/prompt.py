import os
from datetime import datetime

import pathway as pw
from llm_app.model_wrappers import OpenAIChatGPTModel

# api_key = os.environ["HF_API_KEY"]
api_key = os.environ["OPENAI_API_KEY"]


# model = HFApiTextGenerationTask(api_key=api_key)
model = OpenAIChatGPTModel(api_key=api_key)


def prompt(index, embedded_query, user_query):
    @pw.udf
    def build_prompt(local_indexed_data, query):
        docs_str = "\n".join(local_indexed_data)
        prompt = f"Given the following data: \n {docs_str} \nanswer this query: {query}, Assume that current date is: {datetime.now()}. and clean the output"
        return prompt

    query_context = embedded_query + index.get_nearest_items(
        embedded_query.vector, k=3, collapse_rows=True
    ).select(local_indexed_data_list=pw.this.doc).promise_universe_is_equal_to(
        embedded_query
    )

    prompt = query_context.select(
        prompt=build_prompt(pw.this.local_indexed_data_list, user_query)
    )

    return prompt.select(
        query_id=pw.this.id,
        result=model.apply(
            pw.this.prompt,
            # locator="bigscience/bloom",
            locator="gpt-3.5-turbo",
            temperature=0.0,
            max_tokens=200,
        ),
    )
