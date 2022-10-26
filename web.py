import json

from fastapi import FastAPI, WebSocket
import uvicorn

from kfka import kfk_consumer

app = FastAPI()


@app.on_event('startup')
async def init_kfk():
    await kfk_consumer.init("kine", group_id='ws')
    await kfk_consumer.star()


@app.on_event('shutdown')
async def stop_db():
    await kfk_consumer.stop()
    await ws_header.stop_all()


class WebSocketHeader:
    ws_list = []
    flag = True

    async def send(self, ws, data):
        await ws.send_text(json.dumps(data))

    async def broadcast(self, data):
        for ws in self.ws_list:
            await self.send(ws, data)

    async def accept(self, ws):
        await ws.accept()
        self.ws_list.append(ws)

    async def stop(self, ws, room):
        self.ws_list[room].remove(ws)
        await ws.close()

    async def stop_all(self):
        for ws in self.ws_list:
            await ws.close()


ws_header = WebSocketHeader()


@app.websocket("/{kline_id}")
async def websocke_endpoint(kline_id: str, ws: WebSocket):
    await ws_header.accept(ws)
    while True:
        try:
            async for msg in kfk_consumer:
                await ws_header.broadcast(msg.value.decode())
        except Exception:
            print(6)
            await ws_header.stop(ws, kline_id)


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000)
