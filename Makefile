.PHONY: bootstrap up api web lint typecheck test format help

help:
	@echo "Aarogya AI Research Platform"
	@echo "  make bootstrap  - install JS + Python deps"
	@echo "  make up         - docker compose (web + api)"
	@echo "  make api        - run FastAPI locally"
	@echo "  make web        - run Next.js locally"
	@echo "  make lint       - lint all packages"
	@echo "  make typecheck  - typecheck"
	@echo "  make test       - run API tests"
	@echo "  make format     - format code"

bootstrap:
	./scripts/bootstrap.sh

up:
	docker compose -f docker/docker-compose.yml up --build

api:
	cd services/inference-api && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

web:
	pnpm --filter @aarogya/web dev

lint:
	./scripts/lint.sh

typecheck:
	./scripts/typecheck.sh

test:
	cd services/inference-api && python -m pytest -q

format:
	pnpm format
	cd core && python -m black aarogya_core && python -m isort aarogya_core
	cd services/inference-api && python -m black app tests && python -m isort app tests
