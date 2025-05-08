# predictive-maintenance-app

Predictive Maintenance Web App for Mining Equipment
This project implements a web application for predictive maintenance of mining equipment, leveraging 5G-enabled AI systems as outlined in the document "5G ENABLED AI SYSTEM FOR PREDICTIVE MAINTENANCE IN MINING EQUIPMENT" by Moomba Kenneth Shimbulo and Saliya Tonkola. The app allows users to upload equipment data via Excel files, processes the data using Python, uses xAI's Grok API for AI-driven failure predictions, and visualizes results with Vue.js and Chart.js. The application is designed to be hosted on Render using Docker for scalability.
Table of Contents

Project Overview
Features
Tech Stack
Project Structure
Prerequisites
Setup Instructions
Running Locally
Deploying on Render
Excel File Format
Simulation Details
Alignment with Document
Contributing
License

Project Overview
The web app simulates a predictive maintenance system for mining equipment, addressing the challenges of reactive maintenance, high downtime, and safety risks in mining operations. It processes equipment data (e.g., vibration, temperature, uptime hours), predicts potential failures using AI, and visualizes maintenance recommendations. The system is designed to be compatible with high-speed 5G data transfer for efficient real-time monitoring, as emphasized in the document.
Features

Excel Data Upload: Users can upload Excel files containing equipment data.
AI-Driven Predictions: Utilizes xAI's Grok API to predict equipment failure probabilities and recommend maintenance schedules.
Data Visualization: Displays failure probability graphs using Vue.js and Chart.js.
Scalable Deployment: Hosted on Render with Docker for backend and frontend services.
Cross-Origin Support: Configured CORS for seamless frontend-backend communication.
Simulation: Forecasts equipment issues and schedules maintenance tasks based on AI predictions.

Tech Stack

Backend:
Python 3.11
FastAPI (API framework)
pandas (Excel processing)
openpyxl (Excel file handling)
requests (Grok API integration)


Frontend:
Vue.js 3 (UI framework)
Vuetify (Material Design components)
Chart.js (Graphing)


Deployment:
Docker (Containerization)
Render (Hosting)


AI:
xAI Grok API (Predictive analytics)



Project Structure
predictive-maintenance-app/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src/
│   │   ├── main.py              # FastAPI application
│   │   ├── ai_service.py        # Grok API integration
│   │   ├── data_processor.py    # Excel data processing
├── frontend/
│   ├── Dockerfile
│   ├── package.json
│   ├── src/
│   │   ├── components/
│   │   │   ├── UploadComponent.vue  # File upload UI
│   │   │   ├── GraphComponent.vue   # Prediction graphs
│   │   ├── App.vue                  # Main Vue component
│   │   ├── main.js                 # Vue app entry point
├── docker-compose.yml               # Local development setup
├── README.md                       # Project documentation

Prerequisites

Python 3.11+
Node.js 18+
Docker and Docker Compose
Render account (render.com)
xAI API key (console.x.ai)
Git

Setup Instructions

Clone the Repository:
git clone https://github.com/your-username/predictive-maintenance-app.git
cd predictive-maintenance-app


Backend Setup:

Navigate to the backend directory:cd backend


Install Python dependencies:pip install -r requirements.txt




Frontend Setup:

Navigate to the frontend directory:cd frontend


Install Node.js dependencies:npm install




Environment Variables:

Set the xAI API key for the backend:export XAI_API_KEY=your-xai-api-key


Alternatively, add it to Render's environment variables during deployment.



Running Locally

Start Services with Docker Compose:

From the project root, run:docker-compose up --build


This starts the backend at http://localhost:8000 and the frontend at http://localhost:8080.


Access the App:

Open http://localhost:8080 in a browser.
Upload an Excel file to view predictions and graphs.


Stop Services:

Press Ctrl+C and clean up:docker-compose down





Deploying on Render

Push to GitHub:

Initialize a Git repository and push the project:git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/predictive-maintenance-app.git
git push -u origin main




Create Backend Service:

In Render, create a new Web Service and select Docker.
Link your GitHub repository and point to the backend directory.
Configure:
Runtime: Docker
Start Command: uvicorn main:app --host 0.0.0.0 --port 8000
Port: 8000
Environment Variable: XAI_API_KEY=your-xai-api-key




Create Frontend Service:

Create another Web Service, select Docker, and point to the frontend directory.
Configure:
Runtime: Docker
Start Command: npm run serve
Port: 8080




Update CORS:

In backend/src/main.py, update the allow_origins list to include your Render frontend URL (e.g., https://your-frontend.onrender.com).
Commit and push the changes.


Test Deployment:

Access the frontend URL provided by Render.
Upload an Excel file to verify predictions and visualizations.



Excel File Format
The app expects Excel files (.xlsx or .xls) with the following columns:
equipment_id,timestamp,vibration,temperature,uptime_hours
EQ001,2025-01-01 08:00:00,0.5,75.2,1200
EQ001,2025-01-02 08:00:00,0.7,78.1,1224
EQ002,2025-01-01 08:00:00,0.3,70.5,800
...


equipment_id: Unique identifier for the equipment.
timestamp: Date and time of the measurement (e.g., YYYY-MM-DD HH:MM:SS).
vibration: Vibration level (numeric, normalized by the app).
temperature: Equipment temperature in °C (numeric, normalized).
uptime_hours: Total operational hours (numeric).

Example file: equipment_data.xlsx.
Simulation Details

Data Processing:
The backend uses pandas to read and normalize Excel data (vibration and temperature) for consistent AI input.


AI Predictions:
The Grok API analyzes equipment data to predict failure probabilities (0-1) and recommend maintenance dates.
Predictions include equipment_id, failure_probability, recommended_maintenance_date, and health_status (Good, Warning, Critical).


Visualization:
The frontend displays a line chart of failure probabilities per equipment, enabling users to identify at-risk machines.


5G Compatibility:
While not directly implementing 5G, the app is designed for high-speed data transfer, aligning with the document's emphasis on 5G efficiency.



Alignment with Document
This project aligns with the objectives and methodology of the provided document:

Aim: Implements a 5G-enabled AI system for predictive maintenance using Grok API and a web app.
Objectives:
Develops a predictive maintenance system for mining equipment.
Processes and analyzes equipment data to simulate maintenance schedules.
Provides a foundation for comparing local and international predictive maintenance systems (extendable with additional data).


Methodology:
Uses AI algorithms (via Grok API) to identify patterns in equipment data.
Simulates maintenance forecasts and recommendations.
Supports data collection from Excel files, adaptable for local mining site data.


Benefits:
Reduces downtime and operational costs.
Improves safety by identifying at-risk equipment.
Supports environmental and economic benefits through efficient maintenance.



The app does not directly evaluate local mining site methods or implement Arduino/Proteus (as mentioned in the document) but focuses on a scalable web-based simulation, which can be extended for hardware integration.
Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
