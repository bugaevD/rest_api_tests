success_create_club_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "bookTitle": {
      "type": "string"
    },
    "bookAuthors": {
      "type": "string"
    },
    "publicationYear": {
      "type": "number"
    },
    "description": {
      "type": "string"
    },
    "telegramChatLink": {
      "type": "string"
    },
    "owner": {
      "type": "number"
    },
    "members": {
      "type": "array",
      "items": {
        "type": "number"
      }
    },
    "reviews": {
      "type": "array",
      "items": {}
    },
    "created": {
      "type": "string"
    },
    "modified": {}
  },
  "required": [
    "id",
    "bookTitle",
    "bookAuthors",
    "publicationYear",
    "description",
    "telegramChatLink",
    "owner",
    "members",
    "reviews",
    "created",
    "modified"
  ]
}

duplicate_create_club_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "bookTitle": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "bookTitle"
  ]
}

no_auth_create_club_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "detail": {
      "type": "string"
    }
  },
  "required": [
    "detail"
  ]
}

invalid_token_create_club_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "detail": {
      "type": "string"
    },
    "code": {
      "type": "string"
    },
    "messages": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "tokenClass": {
            "type": "string"
          },
          "tokenType": {
            "type": "string"
          },
          "message": {
            "type": "string"
          }
        },
        "required": [
          "tokenClass",
          "tokenType",
          "message"
        ]
      }
    }
  },
  "required": [
    "detail",
    "code",
    "messages"
  ]
}

empty_book_title_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "bookTitle": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "bookTitle"
  ]
}

empty_book_author_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "bookAuthors": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "bookAuthors"
  ]
}

empty_book_description_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "description": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "description"
  ]
}

empty_book_telegram_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "telegramChatLink": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "telegramChatLink"
  ]
}
empty_book_publication_year_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "publicationYear": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "publicationYear"
  ]
}


missing_book_title_schema = empty_book_title_schema
missing_book_author_schema = empty_book_author_schema
missing_book_description_schema = empty_book_description_schema
missing_book_telegram_schema = empty_book_telegram_schema
missing_book_publication_year_schema = empty_book_publication_year_schema
invalid_data_type_book_publication_year_schema = missing_book_publication_year_schema
invalid_json_schema = no_auth_create_club_schema
unsupported_media_type_schema = no_auth_create_club_schema
very_long_book_author_schema = empty_book_author_schema
very_long_book_title_schema = empty_book_title_schema
invalid_telegram_link_schema = empty_book_telegram_schema