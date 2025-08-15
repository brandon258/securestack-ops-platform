.PHONY: bootstrap lint test plan up down
bootstrap: ## Install tools & hooks
\tpipx install poetry pre-commit || true
\tpre-commit install

lint:
\tpre-commit run --all-files

plan:
\tterraform -chdir=terraform/envs/sandbox plan

up:
\tpoetry run securestack up --env sandbox

down:
\tpoetry run securestack down --env sandbox
