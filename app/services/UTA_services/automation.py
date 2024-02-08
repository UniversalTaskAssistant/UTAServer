from sqlalchemy.ext.asyncio import AsyncSession
from uta.UTA import UTA

class Automation:
    def __init__(self, uta) -> None:
        self.uta = uta

    @classmethod
    async def create(cls):
        uta = UTA()
        return cls(uta)
    
    async def automation(self, message):
        _, action = self.uta.automate_task(
            user_id=message.get("user_id"), 
            task_id=message.get("task_id"), 
            ui_img_file=message.get("ui_img"), 
            ui_xml_file=message.get("ui_xml"),
            package_name=message.get("package_name"), 
            activity_name=message.get("activity_name"), 
            keyboard_active=message.get("keyboard_active"),
            printlog=False)
        yield action