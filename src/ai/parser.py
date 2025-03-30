from typing import Dict, Any
import json
import openai
from src.utils.config import get_config

def parse_text(text: str) -> Dict[Any, Any]:
    """Parse natural language input into structured event details using AI.
    
    Args:
        text (str): Natural language input from user
        
    Returns:
        Dict[Any, Any]: Structured event details including:
            - title: Event title
            - start_time: Start time (ISO format)
            - end_time: End time (ISO format)
            - description: Optional description
            - is_blocking: Whether this is blocking time or a specific event
    """
    config = get_config()
    
    # Ensure API key is set
    openai.api_key = config.get("openai_api_key")
    
    # Call the OpenAI API to parse the text
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": """You are a scheduling assistant that extracts event details from text.
             Extract the following information:
             - title: A brief title for the event
             - start_time and end_time: In ISO format (YYYY-MM-DDTHH:MM:SS)
             - description: Any additional details about the event
             - is_blocking: true if this is blocking time for work/focus, false if it's a specific event
             
             Use the current date for relative time references like "tomorrow" or "next week".
             """},
            {"role": "user", "content": f"Extract calendar event details from this text: {text}"}
        ],
        temperature=0.1,
        response_format={"type": "json_object"}
    )
    
    # Extract and parse the JSON response
    try:
        content = response.choices[0].message.content
        event_details = json.loads(content)
        return event_details
    except (json.JSONDecodeError, AttributeError, IndexError) as e:
        print(f"Error parsing AI response: {e}")
        # Fallback to a placeholder
        return {
            "title": "Schedule Event",
            "start_time": "2025-03-29T10:00:00",
            "end_time": "2025-03-29T11:00:00",
            "description": text,
            "is_blocking": "blocking" in text.lower() or "work" in text.lower()
        }