from discord import ClientException


class MissingFeatures(ClientException):
  def __init__(self, cog, features: set):
    self.features = features
    self.cog = cog
    super().__init__(
      f"{cog.__class__.__name__} requires missing features: {features}"
    )


class WebAPIExeception(Exception):
  def __init__(self, api: str):
    super().__init__()
    self.api = api


class WebAPINoResults(WebAPIExeception):
  def __init__(self, api: str, q: str):
    super().__init__(api)
    self.q = q


class WebAPIUnreachable(WebAPIExeception):
  pass


class WebAPIInvalidResponse(WebAPIExeception):
  def __init__(self, api: str, status: int):
    super().__init__(api)
    self.status = status
