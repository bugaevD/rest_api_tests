from schemas.auth_schema import none_body_type_schema

success_register = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "username": {
      "type": "string"
    },
    "firstName": {
      "type": "string"
    },
    "lastName": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "remoteAddr": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "username",
    "firstName",
    "lastName",
    "email",
    "remoteAddr"
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

very_long_username_schema = {
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

very_long_password_schema = {
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

very_long_both_fields_schema = {
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

unsupported_content_type_registred_schema = {
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

invalid_username_schema = blank_username_schema
invalid_password_schema = blank_password_schema
already_registered_schema = blank_username_schema
very_short_username_schema = very_long_username_schema
very_short_password_schema = very_long_password_schema
very_short_both_fields_schema = very_long_both_fields_schema
missing_username_schema = blank_username_schema
missing_password_schema = blank_password_schema
missing_both_fields_schema = blank_both_fields_schema
invalid_json_schema = unsupported_content_type_registred_schema
none_body_type_schema = blank_both_fields_schema