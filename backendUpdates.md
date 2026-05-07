smart-ev-saas/
│
├── backend/
│   ├── app.py                  # Flask app entry point
│   ├── models.py               # SQLAlchemy models
│   ├── routes.py               # API routes
│   ├── config.py               # Environment/config settings
│   ├── extensions.py           # DB/init setup
│   │
│   ├── services/
│   │   ├── queue_service.py
│   │   ├── charger_service.py
│   │   ├── prediction_service.py
│   │   └── notification_service.py
│   │
│   ├── utils/
│   │   ├── helpers.py
│   │   └── validators.py
│   │
│   └── tests/
│       ├── test_routes.py
│       └── test_services.py
│
├── frontend/
│   ├── dashboard.py            # Main Streamlit app
│   │
│   ├── pages/
│   │   ├── admin.py
│   │   ├── driver.py
│   │   └── analytics.py
│   │
│   ├── components/
│   │   ├── sidebar.py
│   │   └── charts.py
│   │
│   └── assets/
│       └── styles.css
│
├── simulation/
│   ├── simulator.py
│   ├── traffic_generator.py
│   └── demand_predictor.py
│
├── database/
│   ├── ev_saas.db
│   └── seed_data.py
│
├── docs/
│   ├── api.md
│   └── architecture.md
│
├── .env
├── .gitignore
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md