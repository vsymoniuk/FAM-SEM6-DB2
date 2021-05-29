from enum import Enum


class Tags(Enum):
    work = 1,
    private = 2,
    shared = 3

    @classmethod
    def has_member(cls, value):
        return value in Tags._member_names_