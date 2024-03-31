# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CommentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.topic_id = self.scope['url_route']['kwargs']['topic_id']
        self.room_group_name = f'comment_{self.topic_id}'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        comment = text_data_json['comment']

        # Send comment to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'comment_message',
                'comment': comment
            }
        )

    async def comment_message(self, event):
        comment = event['comment']

        # Send comment to WebSocket
        await self.send(text_data=json.dumps({
            'comment': comment
        }))
