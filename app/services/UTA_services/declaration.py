from uta.UTA import UTA

class Declaration:
    def __init__(self, uta) -> None:
        self.uta = uta

    @classmethod
    async def create(cls):
        uta = UTA()
        return cls(uta)
    
    async def declaration(self, message):
        resp = self.uta.declare_task(user_id=message.get("user_id"), task_id=message.get("task_id"), user_msg=message.get("user_msg"))
        yield resp
