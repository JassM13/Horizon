from quart import Quart

class Dashboard(Quart):
  def __init__(self):
    super().__init__(
      import_name = "Dashboard"
    )

    @self.route("/")
    def home():
      return "Hello, World!"


  async def start(self, host, port):
    print("running...")
    await super().run_task(host=host, port=port)