# Development Docker

```bash
# from repo root
cp .env.example .env
docker compose -f docker/docker-compose.yml up --build
```

Services: `web` (3000), `inference-api` (8000). Profile `gpu` starts a placeholder worker only.
