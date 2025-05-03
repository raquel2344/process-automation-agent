# Process Automation Agent

## Overview

The **Process Automation Agent** is an AI-powered solution designed to streamline departmental processes. It leverages cutting-edge tools such as the OpenAI API, a web browser, and the Google Calendar API to automate tasks like:

- Scheduling meetings.
- Preparing documentation.
- Sending reminders and notifications.
- Managing follow-ups.

This repository contains the code, documentation, and guides required to set up and use the agent effectively.

---

## Features

- **Meeting Scheduler**: Automatically schedules meetings using the Google Calendar API.
- **Documentation Generator**: Uses OpenAI's GPT models to create meeting notes and summaries.
- **Reminder System**: Sends timely reminders for upcoming meetings and tasks.
- **Follow-Up Manager**: Handles follow-ups based on meeting outcomes.
- **API Collector**: Dynamically collects and manages APIs using a web browser.

---

## Repository Structure

```plaintext
process-automation-agent/
├── docs/                        # Documentation
├── src/                         # Source code
│   ├── agent/                   # Core automation logic
│   ├── api/                     # API management
│   ├── integrations/            # Third-party integrations
│   └── main.py                  # Entry point
├── tests/                       # Unit and integration tests
├── .github/                     # GitHub workflows
├── requirements.txt             # Python dependencies
├── setup.py                     # Installation and packaging
└── LICENSE                      # Project license
```

---

## Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/raquel2344/process-automation-agent.git
   cd process-automation-agent
   ```

2. **Install Dependencies**

   Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up API Keys**

   Create a `.env` file with the following keys:

   ```plaintext
   OPENAI_API_KEY=<your-openai-api-key>
   GOOGLE_CALENDAR_CREDENTIALS=<path-to-google-credentials-file>
   ```

4. **Run the Application**

   Start the agent by running:

   ```bash
   python src/main.py
   ```

---

## Documentation

Comprehensive documentation is available in the `docs/` directory. Start with:

- [Setup Guide](docs/setup.md)
- [API Integration](docs/api_integration.md)
- [Usage Instructions](docs/usage.md)

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](docs/contributing.md) for more details on how to get started.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.