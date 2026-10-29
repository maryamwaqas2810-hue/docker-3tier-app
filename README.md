# 3-Tier Docker App

A simple 3-tier web application (frontend, backend, database) where each tier runs in its own Docker container and the whole stack starts with a single Docker Compose command. I built it to practice containerization.

## Architecture

```
Browser → Nginx (frontend) → Flask (backend) → PostgreSQL (db)
```

- **Frontend:** A simple HTML page served by Nginx. Nginx also works as a reverse proxy and forwards requests starting with `/api` to the backend.
- **Backend:** A Flask (Python) API that reads items from the database and returns them as JSON. Routes: `/health` and `/items`.
- **Database:** PostgreSQL. Data is stored in a Docker volume, so it is not lost when containers are removed.

## What I used and learned

- Dockerfiles and Docker Compose (3 services on one private network)
- Nginx as a reverse proxy
- A named volume to keep database data
- A healthcheck, so the backend starts only after the database is ready
- A `.env` file to keep secrets out of the code and out of Git

## Project structure

```
.
├── backend/            # Flask app + Dockerfile
├── frontend/           # index.html + nginx.conf + Dockerfile
├── docker-compose.yml
├── .env.example        # copy this to .env
└── README.md
```

## How to run

1. Clone the repo.
2. Copy `.env.example` to `.env` and set your own password.
3. Start everything:
   ```bash
   docker compose up -d --build
   ```
4. Open `http://localhost:8080` in your browser.
5. To stop: `docker compose down` (the data stays in the volume).