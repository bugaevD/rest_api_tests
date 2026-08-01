delete_other_user_club_schema = {
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

delete_club_without_auth_schema = delete_other_user_club_schema
delete_nonexistent_club_schema = delete_other_user_club_schema
delete_already_deleted_club_schema = delete_other_user_club_schema
delete_invalid_id_schema = delete_other_user_club_schema