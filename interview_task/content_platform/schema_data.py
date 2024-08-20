from enum import Enum


class SchemaTags(Enum):
    CONTENT = "content"
    USER = "user"
    JWT = "jwt"
    RATING = "rating"


CONTENT_API_METADATA = {
    "ContentCreate": {
        "tags": [SchemaTags.CONTENT.value],
        "summary": "Create a new content item",
    },
    "ContentList": {
        "tags": [SchemaTags.CONTENT.value],
        "summary": "Get all content items from the DB",
    },
    "ContentRetrieve": {
        "tags": [SchemaTags.CONTENT.value],
        "summary": "Get a content item by ID",
    },
    "ContentUpdate": {
        "tags": [SchemaTags.CONTENT.value],
        "summary": "Update a content item by ID",
    },
    "ContentDestroy": {
        "tags": [SchemaTags.CONTENT.value],
        "summary": "Delete a content item by ID",
    },
}
