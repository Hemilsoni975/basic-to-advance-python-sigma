import asyncio
import websockets

async def my_connect():
    async with websockets.connect("ws://localhost:3000") as websocket:
        for i in range(1,100,1):
            await websocket.send("hi hello eelooo")
            data_rcv  = await websocket.recv()
            print("data from server : " + data_rcv)

asyncio.get_event_loop().run_until_complete(my_connect())
