import requests

from os import getenv
from dotenv import load_dotenv

load_dotenv()
token = getenv("DISCORD_TOKEN")

header = {
    "Authorization": token,
    "Content-Type": "application/json"
}

def send(channel: str, message: str):
    response = requests.post(f"https://discord.com/api/v10/channels/{channel}/messages", headers=header, json={"content": message})
    return response.json()