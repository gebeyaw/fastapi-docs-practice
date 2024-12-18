from fastapi import FastAPI, Body
from typing import Annotated
from uuid import UUID
from datetime import datetime, time, timedelta


app = FastAPI()

@app.put("/item/{item_id}")
async def read_items(
        item_id: UUID,
        start_datetime:Annotated[datetime, Body()],
        end_datetime:Annotated[datetime, Body()],
        process_after:Annotated[timedelta, Body()],
        repeat_after: Annotated[time | None, Body()] = None,
                     ):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after":process_after,
        "repeat_after":repeat_after,
        "start_process":start_process,
        "duration":duration
    }

