# Schedule.ai

An AI-powered scheduling application that converts natural language into calendar events.

![License](https://img.shields.io/github/license/TheFlying12/schedule.ai)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

## 🌟 Features

- 📝 **Natural Language Processing**: Type scheduling requests in plain English
- 🗓️ **Calendar Integration**: Creates standard iCalendar files compatible with most calendar apps
- 🚫 **Blocking Time**: Distinguish between focused work blocks and regular events
- 💻 **Multiple Interfaces**: Use via command line, API, or GUI (coming soon)

## 📋 Quick Start Guide

### Option 1: Install with pip (Easiest)

```bash
# Install from PyPI
pip install scheduleai

# Run first-time setup
scheduleai --setup

# Start scheduling!
scheduleai "Meeting with marketing team tomorrow at 2pm for 1 hour"
```

### Option 2: Download the App

Visit our [Releases page](https://github.com/TheFlying12/schedule.ai/releases) to download:
- Windows: `scheduleai-windows.exe`
- macOS: `scheduleai-macos.dmg`
- Linux: `scheduleai-linux.deb`

### Option 3: Clone the Repository (For Developers)

```bash
# Clone repo
git clone https://github.com/TheFlying12/schedule.ai.git
cd schedule.ai

# Install in development mode
pip install -e .

# Create config file
cp .env.example .env
# Edit .env with your OpenAI API key

# Run the app
scheduleai -i
```

## 💡 Usage Examples

### Command Line

```bash
# Add a simple event
scheduleai "Doctor appointment on Friday at 3pm"

# Block time for focused work
scheduleai "Block 2 hours tomorrow morning for project work"

# Interactive mode
scheduleai -i

# Show detailed information
scheduleai -v "Team standup every weekday at 9:30am"
```

### API

```bash
# Start the API server
python main.py

# In another terminal, use curl to add events
curl -X POST "http://localhost:8000/schedule" \
     -H "Content-Type: application/json" \
     -d '{"text":"Lunch with Alex on Thursday at noon"}'
```

## 📅 Calendar Integration

Schedule.ai creates standard `.ics` files that you can import into:
- Google Calendar
- Apple Calendar
- Microsoft Outlook
- And most other calendar applications

By default, your calendar is stored at:
- Windows: `%APPDATA%\ScheduleAI\schedule.ics`
- macOS: `~/Library/Application Support/ScheduleAI/schedule.ics`
- Linux: `~/.config/scheduleai/schedule.ics`

## 🔑 Requirements

- Python 3.8+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch: `git checkout -b new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin new-feature`
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.