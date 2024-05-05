from uta.UTA import UTA

class Automation:
    def __init__(self, uta) -> None:
        self.uta = uta

    @classmethod
    async def create(cls):
        uta = UTA()
        return cls(uta)
    
    async def automation(self, **kwargs):
        _, action = self.uta.automate_task(**kwargs)
        yield action

class QueryRAI:
    def __init__(self, uta) -> None:
        self.uta = uta

    @classmethod
    async def create(cls):
        uta = UTA()
        return cls(uta)
    
    async def queryrai(self, **kwargs):
        yield self.uta.query_detect_rai_risk(**kwargs)

class CheckAction:
    def __init__(self, uta) -> None:
        self.uta = uta

    @classmethod
    async def create(cls):
        uta = UTA()
        return cls(uta)
    
    async def checkaction(self, **kwargs):
        yield self.uta.check_action_on_ui(**kwargs)