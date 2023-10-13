import websockets
import asyncio

async def my_accept(websocket,path):
    while True:
        data_rcv = await websocket.recv();
        print("recieved data : " + data_rcv)
        await websocket.send("websocket_svr send data = " + data_rcv)

websoc_svr = websockets.serve(my_accept, "localhost", 3000)


asyncio.get_event_loop().run_until_complete(websoc_svr)
asyncio.get_event_loop().run_forever()