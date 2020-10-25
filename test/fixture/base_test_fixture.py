FAV = "fav"
GROUPING = "grouping"
NAME = "name"
EXTRA = "extra"
PASSWORD = "password"
USERNAME = "username"
URL = "url"

headers = [URL, USERNAME, PASSWORD, EXTRA, NAME, GROUPING, FAV]

url_parsed_field = {
    "label": "Website",
    "order": 4,
    "sensitive": 0,
    "type": "url",
    "uid": 13,
    "value": "https://identity.linuxfoundation.org/user/login",
}

userName_parsed_field = {
    "label": "Username",
    "order": 1,
    "sensitive": 0,
    "type": "username",
    "uid": 10,
    "value": "basicName",
}

row_with_all_fields = {
    "favorite": 0,
    "fields": [
        {
            "label": "Website",
            "order": 4,
            "sensitive": 0,
            "type": "url",
            "uid": 13,
            "value": "https://identity.linuxfoundation.org/",
        },
        {
            "label": "Username",
            "order": 1,
            "sensitive": 0,
            "type": "username",
            "uid": 10,
            "value": "basicName",
        }

    ],
    "icon": {
        "fav": "identity.linuxfoundation.org",
        "image": {
            "file": "misc/login"
        },
        "type": 1,
        "uuid": ""
    },
    "note": "",
    "template_type": "login.default",
    "title": "Linuxfoundation",
    "uuid": "d13f6d99-4af4-43ee-bafa-778ac5f93c7f"
}
