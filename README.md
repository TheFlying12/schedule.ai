# Schedule.ai

An AI-powered scheduling application that takes natural language input and updates your calendar.

## Features

- Process natural language input to understand scheduling requests
- Create calendar events in iCalendar format
- Distinguish between blocking time and specific events
- Supports both API and CLI interfaces

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key

### Installation Options

#### Option 1: Install from PyPI (for end users)

```bash
# Install the package
pip install scheduleai

# Set up configuration (first-time setup)
scheduleai --setup
```

#### Option 2: Install from GitHub (for developers)

1. Clone the repository
2. Install in development mode:
   ```bash
   pip install -e .
   ```
3. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   CALENDAR_PATH=/path/to/your/calendar.ics
   ```

#### Option 3: Standalone Application (for non-technical users)

Download the standalone application for your platform:
- [Windows Installer (.exe)](https://github.com/yourusername/schedule.ai/releases)
- [macOS Application (.dmg)](https://github.com/yourusername/schedule.ai/releases)
- [Linux Package (.deb/.rpm)](https://github.com/yourusername/schedule.ai/releases)

## Usage

### Command Line Interface

The CLI allows you to quickly add events from the terminal:

```bash
# Direct command
python src/cli.py "Block time for working on project tomorrow from 2-4pm"

# Interactive mode
python src/cli.py -i

# Show detailed output
python src/cli.py -v "Meeting with team at 3pm Thursday"
```

### Web API

Start the FastAPI server:

```bash
python main.py
```

The API will be available at http://localhost:8000

Send a POST request to `/schedule` with your natural language text:

```bash
curl -X POST "http://localhost:8000/schedule" \
     -H "Content-Type: application/json" \
     -d '{"text":"Block time for working on project tomorrow from 2-4pm"}'
```

## Examples

Here are some examples of the natural language inputs you can use:

- "Block off 3-5pm tomorrow for focused work"
- "Schedule a meeting with marketing team on Friday from 10-11am"
- "Add doctor appointment next Monday at 2pm for 45 minutes"
- "Block time for gym every weekday from 7-8am"

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
