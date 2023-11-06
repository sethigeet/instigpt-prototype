import json
import sys
from requests import Session
from requests.sessions import RequestsCookieJar
from rich.progress import track, Progress, SpinnerColumn, TimeElapsedColumn, TextColumn

from . import RESOBIN_SESSIONID

COURSE = sys.argv[1]

sess = Session()
cookies = RequestsCookieJar()
cookies.set("sessionid", RESOBIN_SESSIONID)
sess.cookies = cookies

URL = f"https://resobin.gymkhana.iitb.ac.in/api/courses/{COURSE}/resources"
with Progress(
    SpinnerColumn(),
    TextColumn("{task.description}"),
    TimeElapsedColumn(),
    transient=True,
) as progress:
    task = progress.add_task(f"Fetching resources for {COURSE}", total=None)
    res = sess.get(URL)
    data = res.json()
    progress.update(task, completed=True)

extracted_data = []

for resource in track(data, description="Processing data", transient=True):
    extracted_data.append(
        {
            "doc": json.dumps(
                {
                    "course": resource["course"],
                    "file": resource["file"],
                    "title": resource["title"],
                    "description": resource["description"],
                    "timestamp": resource["timestamp"],
                    "year": resource["year"],
                    "year": resource["tags"],
                }
            )
        }
    )

with open("./data/courses.json", "w") as f:
    json.dump(extracted_data, f)

print("[green]Successfully extracted data!")
