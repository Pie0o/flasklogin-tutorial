from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    SUBSCRIBER = "subscriber"
    ANONYMOUS = "anonymous"