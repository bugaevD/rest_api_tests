success_auth_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "refresh": {
      "type": "string"
    },
    "access": {
      "type": "string"
    }
  },
  "required": [
    "refresh",
    "access"
  ]
}

get_user_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "username": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "username"
  ]
}

unsuccessful_auth_schema = {
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

blank_username_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "username": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "username"
  ]
}

blank_password_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "password": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "password"
  ]
}

blank_both_fields_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "username": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "password": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "username",
    "password"
  ]
}

missing_password_schema = blank_password_schema
missing_username_schema = blank_username_schema
missing_both_fields_schema = blank_both_fields_schema

unsupported_content_type_auth_schema = {
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

invalid_json_schema = unsupported_content_type_auth_schema

invalid_body_type_schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "nonFieldErrors": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "nonFieldErrors"
  ]
}

none_body_type_schema = blank_both_fields_schema