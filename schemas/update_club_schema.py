success_put_update_club_schema = {
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
    "modified": {
      "type": "string"
    }
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

success_patch_update_club_schema = success_put_update_club_schema
update_club_without_auth_schema = {
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
update_non_existent_club_schema = update_club_without_auth_schema
put_update_missing_required_fields_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "bookTitle": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "bookAuthors": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "publicationYear": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "description": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "telegramChatLink": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "bookTitle",
    "bookAuthors",
    "publicationYear",
    "description",
    "telegramChatLink"
  ]
}
update_other_member_club_schema = update_club_without_auth_schema
patch_update_empty_body_schema = success_patch_update_club_schema