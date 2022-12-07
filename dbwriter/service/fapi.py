import asyncio

from fastapi import BackgroundTasks, FastAPI


app = FastAPI()

# poetry run uvicorn fapi:app

app.g_message_count = 0
app.g_is_running = False


async def mock_counter():
    while app.g_is_running:
        app.g_message_count += 1
        await asyncio.sleep(0.5)


@app.get("/stats")
async def get_stats():
    return {
        "meaasges processed": app.g_message_count,
        "is running": app.g_is_running,
    }


@app.get("/start")
async def start(background_tasks: BackgroundTasks):
    if not app.g_is_running:
        app.g_is_running = True
        background_tasks.add_task(mock_counter)
        return {"message": "the process is started"}
    return {"message": "the process is already started"}


@app.get("/stop")
async def stop():
    if app.g_is_running:
        app.g_is_running = False
        return {"message": "the process is stoped"}
    return {"message": "the process is already stoped"}


@app.on_event("shutdown")
def shutdown():
    app.g_is_running = False
