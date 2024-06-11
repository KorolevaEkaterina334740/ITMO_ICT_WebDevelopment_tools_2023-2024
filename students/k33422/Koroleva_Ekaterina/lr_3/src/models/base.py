from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

__all__ = ['Base']


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    id: Mapped[int] = mapped_column(primary_key=True)
