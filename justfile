run:
	export DATABASE_URL="postgresql://postgres:mysecretpassword@0.0.0.0:5432/sqlalchemy" && poetry run uvicorn sqlalchemy_tutorial.main:app --host 0.0.0.0 --port 8000
