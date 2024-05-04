from uta.UTA import UTA

uta = UTA()
  
async def fetch_tasks():
    return {"task_list": uta.fetch_available_task_list()}  

async def setup_user(**kwargs):
    return uta.set_user(**kwargs)

async def fetch_conversation(**kwargs):
    return uta.set_conv(**kwargs)

async def fetch_all_previouse_conversation_preview(**kwargs):
    return {"user_id": kwargs.get("user_id", ""), "conversation": uta.get_all_conversations_previews(**kwargs)}

async def fetch_all_previouse_task(**kwargs):
    return {"user_id": kwargs.get("user_id", ""), "task": uta.get_all_tasks(**kwargs)}
 
async def set_my_app_recommend_tasks(**kwargs):
    return {"app_tasks": uta.set_my_app_recommend_tasks(**kwargs)}