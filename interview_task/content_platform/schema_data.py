from enum import Enum


class SchemaTags(Enum):
    CONTENT = "content"
    USER = "user"
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


RATING_API_METADATA = {
    "RatingCreate": {
        "tags": [SchemaTags.RATING.value],
        "summary": "Rate a content item",
    },
    "RatingList": {
        "tags": [SchemaTags.RATING.value],
        "summary": "Get all ratings of content items from the DB",
    },
    "RatingRetrieve": {
        "tags": [SchemaTags.RATING.value],
        "summary": "Get a rated content item by ID",
    },
    "RatingUpdate": {
        "tags": [SchemaTags.RATING.value],
        "summary": "Update a rating of content item by ID",
    },
    "RatingDestroy": {
        "tags": [SchemaTags.RATING.value],
        "summary": "Delete a rating by ID",
    },
}
