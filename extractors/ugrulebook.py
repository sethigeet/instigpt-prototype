import re
import jsonlines
import json
from pathlib import Path
from pypdf import PdfReader

from rich.progress import track
from rich import print
from rich.prompt import Prompt

reader = PdfReader("./data/ugrulebook.pdf")
pages = reader.pages[7:]

contents = "\n".join([page.extract_text() for page in pages])

bold_texts = []


def visit_body(text, cm, tm, font_dict, font_size):
    if (
        len(text.strip()) > 0
        and font_dict is not None
        and font_dict["/BaseFont"] == "/CIDFont+F2"
    ):
        bold_texts.append(text)


for page in track(pages, description="Extracting text from PDF"):
    page.extract_text(visitor_text=visit_body)

headings = []
start_indexes = []
regex = re.compile(r"^\d.+$")
for text in track(bold_texts, description="Cleaning extracted text"):
    if re.search(regex, text) is not None:
        headings.append(text)
        start_indexes.append(contents.find(text))

extracted_data = []
for i in track(
    range(len(start_indexes) - 1),
    description="Retreiving useful content from extracted text",
):
    start = start_indexes[i]
    end = start_indexes[i + 1]
    extracted_data.append({"doc": contents[start:end]})

print(f"Writing extracted text to [bold]'./extracted_data/rulebook.jsonl'")
with jsonlines.open("./extracted_data/rulebook.jsonl", "w") as w:
    w.write_all(extracted_data)
