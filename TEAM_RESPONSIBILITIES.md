👥 TEAM RESPONSIBILITIES
👤 Member 1 — Backend Developer
Responsibilities:
Flask API development
Database design (SQLite + SQLAlchemy)
Business logic implementation
Queue management system
Works on:
backend/app.py
backend/routes.py
backend/models.py
backend/services/*
👤 Member 2 — Frontend Developer
Responsibilities:
Streamlit dashboard UI
Admin + driver views
API integration
Charts & visualization
Works on:
frontend/dashboard.py
frontend/pages/*
👤 Member 3 — Simulation & Testing
Responsibilities:
EV arrival simulation
Queue load testing
System stress testing
Data generation
Works on:
simulation/simulator.py
simulation/traffic_generator.py
⚙️ CORE FEATURES (MVP)
🚗 Driver Features
View available chargers
Join queue
View estimated wait time
Receive availability updates
🏢 Admin Features
View stations
Monitor charger occupancy
View active queues
Track system usage
🧠 System Features
EV arrival simulation
Queue management system
Charger allocation system
Basic wait time prediction
Real-time updates (optional)
🧠 CORE LOGIC DESIGN
1. Charger Allocation Logic
IF charger is available:
    assign EV immediately
ELSE:
    add EV to queue
2. Queue Management Logic
FIFO (First In First Out)
Each station has its own queue
Position determines priority
3. Wait Time Prediction
Wait Time =
(Number of vehicles ahead × Avg charging time)
÷ Available chargers
4. EV Simulation Logic
Random EV arrival every 2–5 seconds
Assign random station
Trigger queue or charger allocation
🗄️ DATABASE DESIGN (SQLite)
📦 Database File
database/ev_saas.db
📊 TABLES
1. Stations
id (PK)
name
location
total_chargers
2. Chargers
id (PK)
station_id (FK)
status (available / occupied / offline)
power_kw
3. Queue
id (PK)
station_id
driver_id
position
wait_time
status
created_at
4. Charging Sessions
id (PK)
charger_id
driver_id
start_time
end_time
energy_used
🔌 API DESIGN (FLASK)
Driver APIs
GET  /stations
POST /queue/join
GET  /queue/status
GET  /wait-time
Admin APIs
POST /stations
POST /chargers
GET  /analytics
GET  /occupancy
🚀 SETUP INSTRUCTIONS
1. Clone Repo
git clone https://github.com/<username>/smart-ev-saas.git
cd smart-ev-saas
2. Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install Dependencies
pip install flask
pip install flask_sqlalchemy
pip install flask_socketio
pip install streamlit
pip install requests
4. Run Backend
python backend/app.py

Runs at:

http://localhost:5000
5. Run Frontend
streamlit run frontend/dashboard.py

Runs at:

http://localhost:8501
6. Run Simulation
python simulation/simulator.py
🔀 GIT WORKFLOW
Branch Strategy
main
├── backend-dev
├── frontend-dev
├── simulation-dev
Workflow Steps
git checkout -b backend-dev
git add .
git commit -m "feature update"
git push origin backend-dev

Then create Pull Request on GitHub.

⚠️ IMPORTANT RULES
❌ Never work directly on main
❌ Avoid modifying same file without coordination
✅ Always pull latest code before work
✅ Use API for all communication
✅ Keep simulation separate from backend
🔮 FUTURE SCALING PLAN

After MVP:

Phase 1
SQLite → PostgreSQL
Phase 2
threading → Celery + Redis
Phase 3
Add Docker
Phase 4
Cloud deployment (AWS / Render)
Phase 5
Mobile app + IoT integration
🎯 FINAL OUTCOME

A complete EV Charging SaaS system with:

Real-time simulation
Queue management
Charger monitoring
Scalable backend design
Dashboard interface
SaaS-ready architecture
💡 CORE PRINCIPLE
Build simple → make it work → then scale
