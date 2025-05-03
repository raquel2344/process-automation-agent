# Setup

## Prerequisites
- Python 3.8 or higher
- Virtual environment tool (e.g., `venv`, `virtualenv`)
- API keys for OpenAI and Google Calendar

## Installation Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/process-automation-agent.git
   cd process-automation-agent
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add the following:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_CALENDAR_API_KEY=your_google_calendar_api_key
   ```

5. **Run Tests**:
   ```bash
   pytest
   ```

6. **Start the Application**:
   ```bash
   python src/main.py
   ```

## Troubleshooting
- Ensure all dependencies are installed correctly.
- Verify API keys and environment variables.