from fastapi import FastAPI
from pydantic import BaseModel
from src.ai.parser import parse_text
from src.calendar.manager import add_event_to_calendar

app = FastAPI()

class ScheduleRequest(BaseModel):
    text: str

@app.post("/schedule")
async def schedule_event(request: ScheduleRequest):
    # Parse the text using AI
    event_details = parse_text(request.text)
    
    # Add the event to calendar
    result = add_event_to_calendar(event_details)
    
    return {"success": True, "event": event_details, "calendar_result": result}
