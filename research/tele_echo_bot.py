import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import openai
import sys

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
print(API_TOKEN)
