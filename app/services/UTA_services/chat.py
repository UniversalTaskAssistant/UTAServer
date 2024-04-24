from uta.UTA import UTA
import json
from ...schemas.data_schema import ConversationResponse

class Chat:
    def __init__(self, uta) -> None:
        self.uta = uta

    @classmethod
    async def create(cls):
        uta = UTA()
        return cls(uta)
    
    async def chat(self, **kwargs):
        resp = self.uta.chat(**kwargs)
        yield json.dumps(ConversationResponse(**resp).model_dump())