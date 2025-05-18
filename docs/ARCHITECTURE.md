# GitHub Analysis Project Architecture

## Overview

This project collects public data from GitHub repositories, processes language statistics, and stores everything in a MongoDB database, exposing REST endpoints for querying and management.

## Components

- **Flask API**  
  Exposes REST endpoints and orchestrates the ETL process.
- **ETL Service**  
  Class that consumes the GitHub API, processes data, and saves it to MongoDB.
- **MongoDB**  
  NoSQL database for storing repositories and language statistics.
- **Docker Compose**  
  Orchestrates the API and MongoDB containers.

## Folder Structure

```
github-analysis/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── languages.py
│   │   └── etl.py
│   ├── services/
│   │   └── github_etl.py
│   └── models/
│       └── repository.py
│
├── infra/
│   └── docker/
│       ├── Dockerfile
│       └── docker-compose.yml
│
├── .env
├── API.md
└── ARCHITECTURE.md
```

## Data Flow

1. The user sends a POST to `/api/etl` with the owner and token.
2. The backend runs the ETL, collects data from GitHub, and saves it to MongoDB.
3. Data can be queried via `/api/languages`.
4. The user can remove data for an owner via DELETE `/api/etl/<owner>`.

## Notes

- You do not need to install MongoDB locally; just use Docker Compose.
- The GitHub token is sent in the POST request, not required in `.env`.
- The system is extensible for other endpoints and analyses.
