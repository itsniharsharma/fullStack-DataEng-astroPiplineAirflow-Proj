# fullStack-DataEng-astroPiplineAirflow-Proj



## Overview

AstroPipeline is a comprehensive full stack application that integrates modern web development, Windows desktop UI, data engineering, and custom API development. It leverages the V-model SDLC approach to ensure robust design, implementation, and testing at every stage.

---

## Features

- **Frontend**: React-based SPA for user interaction and data visualization.
- **Backend**: Flask REST API, PyMongo for MongoDB, and custom endpoints (see `astronihar_api.py`).
- **Windows Desktop**: PyQt5 dashboard for native Windows experience.
- **Data Engineering**: Apache Airflow ETL pipeline for automated data extraction and reporting.
- **Custom API**: `astronihar_api.py` exposes astrological data using Swiss Ephemeris.
- **Dockerized Airflow**: For scalable, reproducible ETL workflows.

---

## V-Model SDLC Approach

1. **Requirements Analysis**  
   - Defined user stories for astrology data, email reports, and dashboard analytics.

2. **System Design**  
   - Designed modular architecture: React frontend, Flask backend, PyQt5 desktop, Airflow ETL, MongoDB storage.

3. **Implementation**  
   - Developed each module in isolation, ensuring clear interfaces and documentation.

4. **Unit & Integration Testing**  
   - Wrote unit tests for backend APIs, ETL tasks, and UI components.
   - Manual and automated integration tests for data flow between modules.

5. **Verification & Validation**  
   - Verified each module against requirements.
   - Validated end-to-end workflow: user submits data → stored in MongoDB → processed by Airflow → results shown in dashboard and via API.

6. **Deployment**  
   - Dockerized Airflow and backend.
   - Provided scripts for local and production deployment.

---

## Directory Structure

```
fullStack-DataEng-astroPiplineAirflow-Proj/
├── airflow-docker/         # Airflow ETL pipeline (see dags/dataflow_etl.py)
├── backend/                # Flask API, MongoDB models, routes
├── react-form-app/         # React frontend
├── ui/                     # PyQt5 Windows dashboard
├── templates/              # HTML templates
├── astronihar_api.py       # Custom astrology API
├── main.py                 # Windows app entry point
└── README.md
```

---

## Key Modules

### 1. Frontend (React)
- Located in `react-form-app/`
- User forms, dashboard, and data visualization.

### 2. Backend (Flask)
- Located in `backend/` and `astronihar_api.py`
- REST endpoints, astrology calculations, MongoDB integration.

### 3. Windows Desktop (PyQt5)
- Located in `ui/` and launched via `main.py`
- Native dashboard for Windows users.

### 4. Data Engineering (Airflow)
- Located in `airflow-docker/dags/dataflow_etl.py`
- ETL pipeline: extracts emails from MongoDB, processes, and reports.

### 5. Custom API (`astronihar_api.py`)
- `/api/astronihar/d1` endpoint returns real-time astrological data.

---

## Setup & Usage

### Prerequisites

- Python 3.10+
- Node.js (for React frontend)
- Docker (for Airflow)
- MongoDB

### Installation

1. **Clone the repo**
   ```
   git clone https://github.com/yourusername/fullStack-DataEng-astroPiplineAirflow-Proj.git
   cd fullStack-DataEng-astroPiplineAirflow-Proj
   ```

2. **Backend**
   ```
   cd backend
   pip install -r requirements.txt
   python server.py
   ```

3. **Frontend**
   ```
   cd react-form-app
   npm install
   npm run dev
   ```

4. **Airflow**
   ```
   cd airflow-docker
   docker-compose up
   ```

5. **Windows Desktop**
   ```
   python main.py
   ```

6. **Custom API**
   ```
   python astronihar_api.py
   ```

---

## Testing

- Unit tests for backend and ETL: `pytest`
- Frontend: `npm test`
- Manual verification for desktop UI and API endpoints.

---

## Contributing

Pull requests and issues are welcome! Please follow the V-model SDLC for any new features or bug fixes.

---

## License

MIT License

---

## Author

Nihar Sharma

---

## Acknowledgements

- [Swiss Ephemeris](https://www.astro.com/swisseph/)
- [Apache Airflow](https://airflow.apache.org/)