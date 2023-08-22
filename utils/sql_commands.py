from sqlalchemy.exc import IntegrityError

from utils.datbase import session
from utils.schemas import User


def register_user(user_id: int):
    user = User(
        user_id=user_id
    )
    session.add(user)

    try:
        session.commit()
    except IntegrityError:
        session.rollback()


def select_users():
    users = session.query(User).all()
    return users
