from uta.UTA import UTA

uta = UTA()
  
async def fetch_tasks():
    resp = uta.fetch_available_task_list()
    return {"task_list": resp}  

async def fetch_tasks_info():
    resp = uta.fetch_task_info_list()
    return {"task_info_list": resp}  

async def fetch_hc_task_list():
    resp = uta.fetch_hardcode_task_list()
    return {"hc_task_list": resp}  
