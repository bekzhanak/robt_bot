from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Chat

engine = create_engine(url="sqlite:///users.db")


def get_chats():
    query = select(Chat)
    with Session(engine) as session:
        result = [chat.chat_id for chat in session.scalars(query)]
    return result


def create_chat(chat_id):
    chat = Chat(chat_id=chat_id)
    with Session(engine) as session:
        session.add(chat)
        session.commit()
