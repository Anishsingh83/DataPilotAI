# DataPilot AI

An AI-powered data science assistant that automates data analysis, preprocessing, visualization, machine learning, and report generation through a modern web application.

---

## Overview

DataPilot AI is a Flask-based platform designed to simplify the complete data science workflow. It enables users to upload datasets, analyze them, clean data, visualize insights, build machine learning models, and generate reports from a single interface.

The project is being developed with a modular architecture and follows software engineering best practices including version control, configuration management, logging, and scalable project organization.

---

## Planned Features

- CSV and Excel dataset upload
- Automated data profiling
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Interactive visualizations
- Machine learning model recommendation
- AutoML pipeline
- AI-generated business insights
- Report generation (PDF / Excel)
- Dataset chat assistant
- User authentication

---

## Technology Stack

### Backend

- Python
- Flask

### Data Science

- Pandas
- NumPy
- Scikit-learn

### Visualization

- Matplotlib
- Seaborn
- Plotly

### Database

- SQLite
- SQLAlchemy

### Utilities

- python-dotenv
- Loguru

---

## Project Structure

```text
DataPilotAI/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── ai/
│   ├── analysis/
│   ├── data/
│   ├── database/
│   ├── ml/
│   ├── reports/
│   ├── utils/
│   └── visualization/
│
├── templates/
├── static/
├── instance/
└── logs/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Anishsingh83/DataPilotAI.git
```

Move into the project directory

```bash
cd DataPilotAI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

---

## Development Roadmap

### Completed

- Project initialization
- Professional folder structure
- Git repository setup
- GitHub integration
- Package initialization
- Naming standardization

### In Progress

- Project documentation
- Configuration management
- Logging system
- Flask application factory

### Upcoming

- File upload module
- Data preprocessing engine
- EDA dashboard
- Machine learning engine
- AI recommendation engine
- Report generation
- User authentication
- Production deployment

---

## License

This project is licensed under the MIT License.