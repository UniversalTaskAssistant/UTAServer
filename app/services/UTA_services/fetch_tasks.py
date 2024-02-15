from uta.UTA import UTA

uta = UTA()
  
async def fetch_tasks():
    resp = uta.fetch_available_task_list()
    return {"task_list": resp}  
