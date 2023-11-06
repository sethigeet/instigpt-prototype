# Get list of courses

GET: `https://resobin.gymkhana.iitb.ac.in/api/courses?search_fields=code,title,description`
Response:

```json
{
    "count": 4003,
    "next": "https://resobin.gymkhana.iitb.ac.in/api/courses?p=2&search_fields=code%2Ctitle%2Cdescription",
    "previous": null,
    "results": [
        {
            "code": "AE102",
            "title": "Data Analysis and Interpretation",
            "department": {
                "name": "Aerospace Engineering",
                "slug": "aerospace-engineering"
            },
            "description": "",
            "credits": 6,
            "semester": [
                {
                    "year": 2023,
                    "season": "autumn",
                    "timetable": []
                },
                {
                    "year": 2023,
                    "season": "spring",
                    "timetable": []
                }
            ],
            "tags": [
                "Theory"
            ],
            "reviews_count": 1,
            "resources_count": 11,
            "favorited_by_count": 25,
            "review_requesters_count": 116,
            "resource_requesters_count": 71,
            "cutoffs": {
                "cutoff": null
            }
        },
        ...
    ]
}
```

---

# Get Resources

GET: `https://resobin.gymkhana.iitb.ac.in/api/courses/MA111/resources`
Response:

```json
[
    {
        "id": "ccf2e216-ccca-4ca8-8ff9-6bdb93be9446",
        "uploaded_by": {
            "id": "4542fa38-c2da-42e5-906d-685cc41bf259",
            "name": "ResoBin Admin",
            "ldap_id": "NA",
            "profile_picture": null
        },
        "course": "MA111",
        "file": "https://resobin.gymkhana.iitb.ac.in/mediafiles/resources/ccf2e216/MA_111_-_Tutorials_2022-23.pdf",
        "title": "MA 111 - Tutorials 2022-23.pdf",
        "description": "",
        "author": "null",
        "modules": "null",
        "thumbnail": "https://resobin.gymkhana.iitb.ac.in/mediafiles/thumbnails/ccf2e216-ccca-4ca8-8ff9-6bdb93be9446_TQvlNCX.png",
        "timestamp": "2023-08-28T16:43:31.548019+05:30",
        "year": 2023,
        "status": "approved",
        "tags": [
            "Tutorials"
        ],
        "file_size": 158026,
        "mime_type": "application/pdf"
    },
    ...
]
```
