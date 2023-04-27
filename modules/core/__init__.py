"""
Core bot commands and functionality settings
"""

from .info import InfoCommands
#from .admin import AdminCommands
#from .prefix import PrefixManager
#from .error import ErrorHandler

async def setup(bot):
  await bot.add_cog(InfoCommands())
  #bot.add_cog(AdminCommands())
  #bot.add_cog(PrefixManager())
  #bot.add_cog(ErrorHandler())
  