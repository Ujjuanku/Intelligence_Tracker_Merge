# Competitive Intelligence Tracker

A production-grade competitive intelligence web app that tracks SaaS competitor pages (pricing, changelogs, documentation). It detects meaningful content changes, filters out irrelevant noise, and uses AI to generate strategic insights dynamically.

## 🚀 Live Demo & Repository
- **Live Demo**: [Insert Live Hosted Link Here]
- **GitHub Repository**: [https://github.com/Ujjuanku/Intelligence_Tracker_Merge](https://github.com/Ujjuanku/Intelligence_Tracker_Merge)

## 📋 What is Done
- **Competitor Tracking**: Add links to competitors (e.g., pricing, docs, changelogs) and fetch their current content.
- **Smart Diffing**: Paragraph-level comparison tailored for documentation, highlighting actual structural and textual changes.
- **Strategic Noise Filtering**: Intelligent preprocessing removes dynamic noise like timestamps, vote counts, and headers/footers.
- **AI-Powered Insights**: Integrates with OpenAI's GPT-3.5-Turbo to categorize changes into Pricing, Features, Positioning, and Strategy.
- **History Tracking**: Retains historical snapshots and shows previous checks per competitor.
- **System Health Page**: A dedicated `/system-status` dashboard to monitor the backend, database connection, and AI service health.
- **Basic Error Handling**: Graceful fallback forms and UI states for empty pages or missing data.

## 🚧 What is Not Done (Future Improvements)
- **Automated Scheduling**: Cron jobs for running checks automatically at set intervals.
- **Alerting System**: Email or Slack notifications when significant strategic changes are detected.
- **Advanced Filtering**: User-defined tags or custom rules to fine-tune the noise filtering per URL.

## 📦 Deployment & Local Setup Instructions

### Option 1: Docker (Single Command Run)
*If you lack a local Python setup or want the easiest deployment route.*
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ujjuanku/Intelligence_Tracker_Merge.git
   cd Intelligence_Tracker_Merge
   ```
2. **Set up Environment Variables**:
   ```bash
   cp .env.example .env
   # Open .env and add your OPENAI_API_KEY
   ```
3. **Run via Docker Compose**:
   ```bash
   docker compose up --build
   ```
4. **Access the App**: Open `http://localhost:8000` in your browser.

### Option 2: Local Python Environment
1. **Clone the repository** (as above) and navigate into it.
2. **Create a virtual environment and install dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Set up Environment Variables**: Add your `OPENAI_API_KEY` to the `.env` file just like above. Ensure PostgreSQL is running locally and set `DATABASE_URL` in `.env` if not using SQLite fallback.
4. **Run the Server**:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
5. **Access the App**: `http://localhost:8000`

## 📁 System Architecture
- **Backend Framework**: FastAPI (Async execution for high performance)
- **Database**: PostgreSQL with asyncpg (managed via SQLAlchemy ORM)
- **Frontend**: Jinja2 templating with pure Vanilla CSS (No heavy JS frameworks, keeping it lightweight)
- **Generative AI**: OpenAI GPT-3.5-Turbo for content diff summarization

## 📄 Included Documentation
As requested by the assignment, you will find additional documentation files in the repository root:
- **`AI_NOTES.md`**: Explains my AI tooling usage and LLM provider choices.
- **`ABOUTME.md`**: Contains personal details and resume summary.
- **`PROMPTS_USED.md`**: Records prompts used during app development.
