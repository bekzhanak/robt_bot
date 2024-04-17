from fastapi import FastAPI, Response
from bot import bot
import utils

app = FastAPI()


@app.get('/door_opened/{name}')
async def door_opened(name: str):
    for chat_id in utils.get_chats():
        await bot.send_message(chat_id, text=f"{name} opened the door")
    return Response(status_code=200)


@app.get('/door_closed/{name}')
async def door_closed(name: str):
    for chat_id in utils.get_chats():
        await bot.send_message(chat_id, text=f"{name} closed the door")
    return Response(status_code=200)


@app.get('/alert')
async def alert():
    for chat_id in utils.get_chats():
        await bot.send_message(chat_id, text="Somebody is trying to open the door")
    return Response(status_code=200)
