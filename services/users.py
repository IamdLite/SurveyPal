from peewee import fn

from models import User
from utils.misc.logging import logger

def count_users() -> int:
    query = User.select(fn.COUNT(User.id))
    return query.scalar()

def get_users() -> list[User]:
    query = User.select()
    return list(query)

def get_user(user_id: int) -> User:
    return User.get_or_none(User.id == user_id)

def update_user(user: User, name: str, username: str = None) -> User:
    user.name = name
    user.username = username
    user.save()

    return user

def edit_user_language(user: User, lang: str):
    query = User.update(language=lang).where(User.id == user.id)
    query.execute()

def create_user(id: int, name: str, username: str = None, language: str  = None )->User:
    new_user = User.create(id=id, name=name, username = username, language=language)  

    new_user.is_admin = False
    new_user.save()
    
    logger.logger.info(f'User {new_user} created')
    
    return new_user

def get_or_create_user(id: int, name: str, username: str, language: str):
    user = get_user(id)
    
    if user:
        user.update(user=user, name=name, username=username)
        return user
    
    return create_user(id=id, name=name, username=username, language=language)