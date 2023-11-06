import json
import jsonlines
from requests import Session
from requests.sessions import RequestsCookieJar
from rich.progress import track, Progress, SpinnerColumn, TimeElapsedColumn, TextColumn
from rich import print

from . import RESOBIN_SESSIONID

sess = Session()
cookies = RequestsCookieJar()
cookies.set("sessionid", RESOBIN_SESSIONID)
sess.cookies = cookies

URL = "https://resobin.gymkhana.iitb.ac.in/api/courses"
with Progress(
    SpinnerColumn(),
    TextColumn("{task.description}"),
    TimeElapsedColumn(),
    transient=True,
) as progress:
    task = progress.add_task(f"Fetching courses", total=None)
    res = sess.get(URL, params={"search_fields": "code,title,description"})
    data = res.json()
    progress.update(task, completed=True)
extracted_data = []

for course in track(data["results"], description="Processing data", transient=True):
    extracted_data.append(
        {
            "doc": json.dumps(
                {
                    "code": course["code"],
                    "title": course["title"],
                    "department": course["department"],
                    "description": course["description"],
                    "credits": course["credits"],
                    "semester": course["semester"],
                    "tags": course["tags"],
                }
            )
        }
    )

print("Writing extracted text to [bold]'./extracted_data/courses.jsonl'")
with jsonlines.open("./extracted_data/courses.jsonl", "w") as w:
    w.write_all(extracted_data)
