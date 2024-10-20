
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
from websockets.server import serve
import random

async def echo(websocket):
    async for message in websocket:
        # Appending a random number to the received message
        modified_message = f"{message} - {random.randint(1, 1000)}"
        await websocket.send(modified_message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
