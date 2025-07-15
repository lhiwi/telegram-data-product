#  Shipping a Data Product: From Raw Telegram Data to an Analytical API

This project implements an end-to-end data pipeline to analyze public data from Ethiopian medical business Telegram channels. It includes scraping data, transforming and modeling it with dbt, enriching it using object detection (YOLOv8), and exposing insights via an analytical API built with FastAPI. Orchestration is handled using Dagster, and the entire stack is containerized using Docker.

---

##  Features

*  **Telegram Scraping**: Collects messages and media using Telethon.
*  **Data Lake & Transformation**: Raw JSON messages are stored and transformed into a star schema with dbt.
*  **YOLO Enrichment**: Uses YOLOv8 to detect objects in image data.
*  **Analytical API**: FastAPI exposes insights via clean RESTful endpoints.
*  **Orchestration with Dagster**: Jobs are orchestrated and monitored from a local UI.
*  **Reproducibility with Docker**: Runs the entire project using containers.

---

##  Project Structure

```
telegram-data-product/
├── .github/workflows/ci.yml         # GitHub Actions CI pipeline
├── data/
│   └── raw/telegram_messages/       # Raw scraped Telegram data
├── notebooks/                       # Exploration and analysis notebooks
├── src/                             # Source code modules
├── scripts/                         # Scraper, loader, enrichment scripts
├── tests/                           # Unit and environment tests
├── dbt/                             # dbt models and config
├── api/                             # FastAPI app (main.py, models, schemas, etc.)
├── dagster_pipeline/                # Dagster jobs and ops
├── requirements.txt                 # Python dependencies
├── Dockerfile                       # Base Docker image
├── docker-compose.yml               # Docker orchestration
├── .env                             # Secrets (excluded from Git)
├── .gitignore
└── README.md
```

---

##  Setup & Run Locally (venv)

```bash
# Clone project and enter folder
cd telegram-data-product

# Set up virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run test to verify env
pytest tests/
```

---

##  Run with Docker

```bash
# Build and start services
docker-compose up -d --build
```

---

##  Technologies

* Python 3.10+
* Telethon
* dbt-core + dbt-postgres
* PostgreSQL
* Ultralytics YOLOv8
* FastAPI
* Dagster
* Docker

---

##  Tasks Overview

| Task   | Description                                              |
| ------ | -------------------------------------------------------- |
| Task 0 | Project setup, Docker, `.env`, requirements              |
| Task 1 | Scraping and storing Telegram messages and media         |
| Task 2 | Data modeling and transformation using dbt (Star Schema) |
| Task 3 | Object detection on images using YOLOv8                  |
| Task 4 | FastAPI endpoints for insights                           |
| Task 5 | Orchestrate everything using Dagster                     |

---

