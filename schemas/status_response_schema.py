status_response = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Generated schema for Root",
  "type": "object",
  "properties": {
    "state": {
      "type": "object",
      "properties": {
        "total": {
          "type": "number"
        },
        "used": {
          "type": "number"
        },
        "queued": {
          "type": "number"
        },
        "pending": {
          "type": "number"
        },
        "browsers": {
          "type": "object",
          "properties": {
            "android": {
              "type": "object",
              "properties": {
                "10.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "11.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "12.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "13.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "14.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "15.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "16.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "10.0",
                "11.0",
                "12.0",
                "13.0",
                "14.0",
                "15.0",
                "16.0"
              ]
            },
            "chrome": {
              "type": "object",
              "properties": {
                "148.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "148.0-min": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "149.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "149.0-min": {
                  "type": "object",
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "148.0",
                "148.0-min",
                "149.0",
                "149.0-min"
              ]
            },
            "firefox": {
              "type": "object",
              "properties": {
                "150.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "150.0-min": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "151.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "151.0-min": {
                  "type": "object",
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "150.0",
                "150.0-min",
                "151.0",
                "151.0-min"
              ]
            },
            "msedge": {
              "type": "object",
              "properties": {
                "144.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "144.0-min": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "145.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "145.0-min": {
                  "type": "object",
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "144.0",
                "144.0-min",
                "145.0",
                "145.0-min"
              ]
            },
            "playwright-chrome": {
              "type": "object",
              "properties": {
                "1.60.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.1": {
                  "type": "object",
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "1.60.0",
                "1.61.0",
                "1.61.1"
              ]
            },
            "playwright-chromium": {
              "type": "object",
              "properties": {
                "1.60.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.60.0-min": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.1": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.1-min": {
                  "type": "object",
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "1.60.0",
                "1.60.0-min",
                "1.61.0",
                "1.61.1",
                "1.61.1-min"
              ]
            },
            "playwright-firefox": {
              "type": "object",
              "properties": {
                "1.60.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.1": {
                  "type": "object",
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "1.60.0",
                "1.61.0",
                "1.61.1"
              ]
            },
            "playwright-msedge": {
              "type": "object",
              "properties": {
                "1.60.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.1": {
                  "type": "object",
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "1.60.0",
                "1.61.0",
                "1.61.1"
              ]
            },
            "playwright-webkit": {
              "type": "object",
              "properties": {
                "1.60.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.0": {
                  "type": "object",
                  "properties": {},
                  "required": []
                },
                "1.61.1": {
                  "type": "object",
                  "properties": {},
                  "required": []
                }
              },
              "required": [
                "1.60.0",
                "1.61.0",
                "1.61.1"
              ]
            }
          },
          "required": [
            "android",
            "chrome",
            "firefox",
            "msedge",
            "playwright-chrome",
            "playwright-chromium",
            "playwright-firefox",
            "playwright-msedge",
            "playwright-webkit"
          ]
        },
        "videos": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "total",
        "used",
        "queued",
        "pending",
        "browsers",
        "videos"
      ]
    },
    "origin": {
      "type": "string"
    },
    "browsers": {
      "type": "object",
      "properties": {
        "android": {
          "type": "number"
        },
        "chrome": {
          "type": "number"
        },
        "firefox": {
          "type": "number"
        },
        "msedge": {
          "type": "number"
        },
        "playwright-chrome": {
          "type": "number"
        },
        "playwright-chromium": {
          "type": "number"
        },
        "playwright-firefox": {
          "type": "number"
        },
        "playwright-msedge": {
          "type": "number"
        },
        "playwright-webkit": {
          "type": "number"
        }
      },
      "required": [
        "android",
        "chrome",
        "firefox",
        "msedge",
        "playwright-chrome",
        "playwright-chromium",
        "playwright-firefox",
        "playwright-msedge",
        "playwright-webkit"
      ]
    },
    "sessions": {
      "type": "object",
      "properties": {},
      "required": []
    },
    "browserProtocols": {
      "type": "object",
      "properties": {
        "android": {
          "type": "object",
          "properties": {
            "10.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "16.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "4.4": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            }
          },
          "required": [
            "10.0",
            "16.0",
            "4.4"
          ]
        },
        "chrome": {
          "type": "object",
          "properties": {
            "148.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "148.0-min": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "149.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "149.0-min": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            }
          },
          "required": [
            "148.0",
            "148.0-min",
            "149.0",
            "149.0-min"
          ]
        },
        "firefox": {
          "type": "object",
          "properties": {
            "150.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "150.0-min": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "151.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "151.0-min": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            }
          },
          "required": [
            "150.0",
            "150.0-min",
            "151.0",
            "151.0-min"
          ]
        },
        "msedge": {
          "type": "object",
          "properties": {
            "144.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "144.0-min": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "145.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "145.0-min": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            }
          },
          "required": [
            "144.0",
            "144.0-min",
            "145.0",
            "145.0-min"
          ]
        },
        "playwright-chrome": {
          "type": "object",
          "properties": {
            "1.60.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.1": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            }
          },
          "required": [
            "1.60.0",
            "1.61.0",
            "1.61.1"
          ]
        },
        "playwright-chromium": {
          "type": "object",
          "properties": {
            "1.60.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.60.0-min": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.1": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.1-min": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            }
          },
          "required": [
            "1.60.0",
            "1.60.0-min",
            "1.61.0",
            "1.61.1",
            "1.61.1-min"
          ]
        },
        "playwright-firefox": {
          "type": "object",
          "properties": {
            "1.60.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.1": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            }
          },
          "required": [
            "1.60.0",
            "1.61.0",
            "1.61.1"
          ]
        },
        "playwright-msedge": {
          "type": "object",
          "properties": {
            "1.60.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.1": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            }
          },
          "required": [
            "1.60.0",
            "1.61.0",
            "1.61.1"
          ]
        },
        "playwright-webkit": {
          "type": "object",
          "properties": {
            "1.60.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.0": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            },
            "1.61.1": {
              "type": "object",
              "properties": {
                "protocol": {
                  "type": "string"
                }
              },
              "required": [
                "protocol"
              ]
            }
          },
          "required": [
            "1.60.0",
            "1.61.0",
            "1.61.1"
          ]
        }
      },
      "required": [
        "android",
        "chrome",
        "firefox",
        "msedge",
        "playwright-chrome",
        "playwright-chromium",
        "playwright-firefox",
        "playwright-msedge",
        "playwright-webkit"
      ]
    },
    "version": {
      "type": "string"
    },
    "errors": {
      "type": "array",
      "items": {}
    }
  },
  "required": [
    "state",
    "origin",
    "browsers",
    "sessions",
    "browserProtocols",
    "version",
    "errors"
  ]
}