import os
import json
import sys
from typing import Dict, Any

_config_cache = None

def get_config_dir():
    """Get the configuration directory for Schedule.ai"""
    if sys.platform == 'win32':
        return os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), 'ScheduleAI')
    elif sys.platform == 'darwin':  # macOS
        return os.path.expanduser('~/Library/Application Support/ScheduleAI')
    else:  # Linux and other Unix-like
        return os.path.expanduser('~/.config/scheduleai')

def get_config() -> Dict[str, Any]:
    """Get application configuration.
    
    Returns:
        Dict[str, Any]: Configuration dictionary
    """
    global _config_cache
    
    # Return cached config if available
    if _config_cache is not None:
        return _config_cache
    
    # Default config
    default_config = {
        "openai_api_key": os.environ.get("OPENAI_API_KEY", ""),
        "calendar_path": os.environ.get("CALENDAR_PATH", "calendar.ics"),
    }
    
    # First, try to load from CONFIG_PATH environment variable
    config_path = os.environ.get("CONFIG_PATH")
    
    # If not set, try the default location in user's config directory
    if not config_path:
        config_dir = get_config_dir()
        config_path = os.path.join(config_dir, "config.json")
    
    # Try to load config from file
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                file_config = json.load(f)
                default_config.update(file_config)
        except Exception as e:
            print(f"Error loading config from {config_path}: {e}")
    
    # Cache the config
    _config_cache = default_config
    
    return default_config