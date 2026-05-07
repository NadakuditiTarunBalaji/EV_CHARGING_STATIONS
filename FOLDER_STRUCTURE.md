smart-ev-saas/
│
├── backend/
│   ├── app.py                  # Flask app entry point
│   ├── models.py               # Database models
│   ├── routes.py               # API endpoints
│   ├── config.py               # Config settings
│   │
│   ├── services/
│   │     ├── queue_service.py  # Queue logic
│   │     ├── charger_service.py
│   │     └── prediction_service.py
│
├── frontend/
│   ├── dashboard.py            # Streamlit UI
│   ├── pages/
│   │     ├── admin.py
│   │     └── driver.py
│
├── simulation/
│   ├── simulator.py            # EV arrival generator
│   └── traffic_generator.py
│
├── database/
│   └── ev_saas.db              # SQLite database file
│
├── requirements.txt
└── README.md
