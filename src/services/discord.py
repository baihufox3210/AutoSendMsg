import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

class DiscordService:
    def __init__(self):
        self.token = os.getenv("DISCORD_TOKEN")
        self.headers = {
            "Authorization": self.token,
            "Content-Type": "application/json"
        }
        if not self.token:
            print("Warning: Discord Token is not set")

    async def send_message(self, channel_id: str, message: str):
        url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        payload = {"content": message}
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, json=payload) as response:
                if response.status == 200:
                    return await response.json()

                else:
                    error_data = await response.text()
                    return {"error": f"Discord API Error {response.status}", "details": error_data}

discord_service = DiscordService()