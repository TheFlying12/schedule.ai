from typing import Dict, Any
import icalendar
import datetime
import uuid
import os
from src.utils.config import get_config

def add_event_to_calendar(event_details: Dict[Any, Any]) -> Dict[str, Any]:
    """Add event to iCalendar file.
    
    Args:
        event_details (Dict[Any, Any]): Event details including title, start/end times, etc.
        
    Returns:
        Dict[str, Any]: Result of the operation
    """
    try:
        # Get the path to the calendar file from config
        config = get_config()
        calendar_path = config.get("calendar_path", "calendar.ics")
        
        # Create a new calendar or load existing one
        cal = None
        if os.path.exists(calendar_path):
            with open(calendar_path, 'rb') as f:
                cal = icalendar.Calendar.from_ical(f.read())
        else:
            cal = icalendar.Calendar()
            cal.add('prodid', '-//Schedule.ai//scheduleai.com//')
            cal.add('version', '2.0')
        
        # Create event
        event = icalendar.Event()
        
        # Add properties to the event
        event.add('summary', event_details.get('title', 'Untitled Event'))
        
        # Convert ISO strings to datetime objects
        start_time = datetime.datetime.fromisoformat(event_details.get('start_time'))
        end_time = datetime.datetime.fromisoformat(event_details.get('end_time'))
        
        event.add('dtstart', start_time)
        event.add('dtend', end_time)
        
        # Add a unique identifier
        event.add('uid', str(uuid.uuid4()))
        
        # Add description if provided
        if event_details.get('description'):
            event.add('description', event_details.get('description'))
        
        # Add a category for blocking time vs regular event
        if event_details.get('is_blocking', False):
            event.add('categories', 'BLOCKING')
        
        # Add the event to the calendar
        cal.add_component(event)
        
        # Save the calendar
        with open(calendar_path, 'wb') as f:
            f.write(cal.to_ical())
        
        return {
            "status": "success",
            "message": f"Event '{event_details.get('title')}' added to calendar",
            "calendar_path": calendar_path
        }
    
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to add event to calendar: {str(e)}"
        }
