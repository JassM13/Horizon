import os
import logging
import yaml

import asyncio

from horizon import client, exceptions

async def main():
  logger = logging.getLogger()
  if os.path.isfile("config.yml"):
    logger.info("Found config, loading...")
    with open("config.yml") as file:
      config = yaml.safe_load(file)
  else:
    logger.debug("Config not found, trying to read from env...")

  settings = {"settings": config["settings"], "core": config["core"], "token": os.getenv("TOKEN")}

  bot = client.HorizonPy(**settings)

  for module in os.listdir("modules"):
    if not module.startswith("."):
      try:
        logger.debug(f"Loading module {module}")
        bot.load_module(module)
      except exceptions.MissingFeatures as exc:
        if (
          settings.get("database", None)
          and exc.features != {"database"}
        ):
          raise

  await asyncio.gather(bot.start())

if __name__ == '__main__':
  asyncio.run(main())