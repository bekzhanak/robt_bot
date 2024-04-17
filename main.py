import bot
import asyncio
import uvicorn
from service import app
from models import Base
from utils import engine

def start_uvicorn(loop):
    config = uvicorn.Config(app, loop=loop)
    server = uvicorn.Server(config)
    loop.run_until_complete(server.serve())
    

def start_bot(loop):
    loop.create_task(bot.start()) 

            
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    start_bot(loop)
    start_uvicorn(loop)
