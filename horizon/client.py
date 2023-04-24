import logging
import traceback
from datetime import datetime
from typing import Dict

import aiohttp
import discord
from discord.ext import commands
from discord.ext.commands.view import StringView

from horizon import exceptions

class HorizonPy(commands.AutoShardedBot):
  def __init__(self, **options):
    super().__init__(
      commands.when_mentioned_or('!'), intents = discord.Intents.all()
    )
    self.logger = logging.getLogger("HorizonClient")
    self.core: Dict[str, str]
    self.owner_ids = set(options.pop("owner", []))
    self.created = datetime.now()
    #self.session = aiohttp.ClientSession(loop=self.loop)
    
    self.options = options

  async def on_ready(self):
    print(
      f"Logged in as {self.user.name}."
    )
    
    await self.change_presence(activity=discord.Activity(name="with code"))

  async def get_context(
    self, message: discord.Message, *, cls = commands.Context 
  ) -> commands.Context:
    ctx = await super().get_context(message, cls=cls)

    return ctx

  def load_module(self, name: str):
    if name in self.extensions:
      return

    self.load_extension(f"modules.{name}")

  def reload_module(self, name: str):
    self.reload_extension(f"modules.{name}")

  async def start(self, bot: bool = True):
    print("Bot running...")
    token = self.options.pop("token")
    await super().start(token)