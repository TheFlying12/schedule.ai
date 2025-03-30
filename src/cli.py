#!/usr/bin/env python3
import argparse
import sys
import os
import json
from src.ai.parser import parse_text
from src.calendar.manager import add_event_to_calendar
from dotenv import load_dotenv
import getpass
import pkg_resources

def setup_config():
    """Setup configuration for Schedule.ai"""
    print("Schedule.ai Setup")
    print("=================")
    
    # Determine config directory
    config_dir = get_config_dir()
    os.makedirs(config_dir, exist_ok=True)
    
    config_path = os.path.join(config_dir, "config.json")
    env_path = os.path.join(config_dir, ".env")
    
    # Check if config already exists
    if os.path.exists(config_path) and os.path.exists(env_path):
        print(f"\nConfiguration already exists at {config_dir}")
        overwrite = input("Do you want to overwrite it? (y/n): ").lower()
        if overwrite != 'y':
            print("Setup cancelled.")
            return
    
    # Get OpenAI API key
    api_key = getpass.getpass("\nEnter your OpenAI API key: ")
    
    # Get calendar path
    default_calendar = os.path.join(config_dir, "schedule.ics")
    calendar_path = input(f"\nEnter path for your calendar file (default: {default_calendar}): ")
    if not calendar_path:
        calendar_path = default_calendar
    
    # Create config.json
    config = {
        "calendar_path": calendar_path
    }
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    # Create .env file
    with open(env_path, 'w') as f:
        f.write(f"OPENAI_API_KEY={api_key}\n")
        f.write(f"CONFIG_PATH={config_path}\n")
    
    print(f"\n✅ Setup complete! Configuration saved to {config_dir}")
    print(f"You can now use 'scheduleai' command to manage your calendar.")

def get_config_dir():
    """Get the configuration directory for Schedule.ai"""
    if sys.platform == 'win32':
        return os.path.join(os.environ.get('APPDATA', os.path.expanduser('~')), 'ScheduleAI')
    elif sys.platform == 'darwin':  # macOS
        return os.path.expanduser('~/Library/Application Support/ScheduleAI')
    else:  # Linux and other Unix-like
        return os.path.expanduser('~/.config/scheduleai')

def main():
    """Command line interface for Schedule.ai"""
    
    # Get package version
    try:
        version = pkg_resources.get_distribution("scheduleai").version
    except:
        version = "0.1.0"  # Development version
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Schedule.ai: AI-powered calendar scheduling')
    parser.add_argument('text', nargs='*', help='Natural language text describing the event to schedule')
    parser.add_argument('-i', '--interactive', action='store_true', help='Run in interactive mode')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show detailed output')
    parser.add_argument('--setup', action='store_true', help='Run setup wizard')
    parser.add_argument('--version', action='version', version=f'Schedule.ai v{version}')
    
    args = parser.parse_args()
    
    # Run setup if requested
    if args.setup:
        setup_config()
        return
    
    # Load environment variables
    config_dir = get_config_dir()
    env_path = os.path.join(config_dir, ".env")
    
    if os.path.exists(env_path):
        load_dotenv(env_path)
    else:
        load_dotenv()  # Try default .env file
        
        # Check if we have necessary config
        if not os.environ.get("OPENAI_API_KEY"):
            print("Error: OpenAI API key not found.")
            print("Please run 'scheduleai --setup' to configure Schedule.ai")
            sys.exit(1)
    
    # Handle interactive mode
    if args.interactive or not args.text:
        print("Schedule.ai Interactive Mode")
        print("Type 'exit' or 'quit' to exit")
        print("Enter your scheduling request:")
        
        while True:
            # Get user input
            try:
                user_input = input("> ")
            except (KeyboardInterrupt, EOFError):
                print("\nExiting...")
                sys.exit(0)
                
            # Check for exit command
            if user_input.lower() in ('exit', 'quit'):
                print("Exiting...")
                break
                
            # Process the request
            process_request(user_input, verbose=args.verbose)
    else:
        # Process the text from command line arguments
        text = ' '.join(args.text)
        process_request(text, verbose=args.verbose)

def process_request(text, verbose=False):
    """Process a scheduling request"""
    try:
        print(f"Processing: {text}")
        
        # Parse the text using AI
        event_details = parse_text(text)
        
        if verbose:
            print("\nExtracted event details:")
            for key, value in event_details.items():
                print(f"  {key}: {value}")
        
        # Add the event to calendar
        result = add_event_to_calendar(event_details)
        
        # Show the result
        if result.get("status") == "success":
            print(f"\n✅ {result.get('message')}")
        else:
            print(f"\n❌ {result.get('message')}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()