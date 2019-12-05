from channels.generic.websocket import AsyncWebsocketConsumer
import json

class GraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #Aqui envio los datos desde la BD a front
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def graph_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

