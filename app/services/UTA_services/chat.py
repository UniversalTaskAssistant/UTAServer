from uta.UTA import UTA
from ...schemas.data_schema import ConversationResponse

class Chat:
    def __init__(self, uta) -> None:
        self.uta = uta

    @classmethod
    async def create(cls):
        uta = UTA()
        return cls(uta)
    
    async def chat(self, **kwargs):
        resp = self.uta.chat_assistant(**kwargs)
        yield ConversationResponse(**resp).model_dump()