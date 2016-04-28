
from enum import unique, Enum

import sqlalchemy


class ColumnEnum(sqlalchemy.types.TypeDecorator):
    impl = sqlalchemy.types.String

    def __init__(self, enum_class, **kwargs):
        super().__init__(**kwargs)
        self._enum_class = enum_class

    def process_bind_param(self, value, dialet):
        return value.value

    def process_result_value(self, value, dialet):
        return self._enum_class(value)

    @property
    def python_type(self):
        return self._enum_class

@unique
class RoleEnum(Enum):
    admin = 'admin'
    common = 'common'



