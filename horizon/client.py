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
      
    )