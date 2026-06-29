# Week 1 – Python Dev Training (Daily 90‑min Sprints)

**Theme:** Foundations + First Deploy Path

## Day 1 (Python Core)
- venv, pytest, flake8 in `projects/python/basics`
- Add a new function + test; push to GitHub → CI green
- Stretch: add type hints; run `pre-commit install`

## Day 2 (Web API)
- Compare Flask vs FastAPI; start `web/fastapi-starter`
- Implement `/api/echo` test; run locally with `uvicorn`

## Day 3 (SQL Low-Cost)
- Start Postgres with `docker compose up -d db`
- Run `projects/sql/postgres/main.py`, then extend schema + query

## Day 4 (AWS + boto3)
- Configure `aws configure`
- In `aws/s3-basics`, upload/list/download; add a pytest using moto/boto3 stubber

## Day 5 (CI/CD)
- Open `.github/workflows/ci.yml` and verify tests/lint/security run
- Add a new test → watch CI
- (Optional) Try Jenkinsfile and GitLab CI

## Day 6 (IaC OIDC)
- In `infra/aws/terraform-github-oidc` set vars and `terraform apply`
- Save role ARN as repo secret `AWS_OIDC_ROLE_ARN`
- Confirm `aws_assume_role_check` job passes

## Day 7 (Ansible)
- Use `ansible/provision-nginx` against an EC2 or lab VM
- Template index page; validate via curl

**Completion Criteria:** All labs started; CI green; OIDC role validated; one EC2 or VM provisioned by Ansible.
