from sqlalchemy.ext.asyncio import AsyncSession
from UTABackend.UTA import UTA

class Automation:
    def __init__() -> None:
        pass

    @classmethod
    async def create(cls, db: AsyncSession):
        
        return cls()
    
    
    async def automation(self, db, message):
        
        yield "__END_OF_RESPONSE__"