# FastAPI KPA Assignment

## Setup Instructions

1. Create PostgreSQL DB `kpadb`.
2. Update the `.env` file with your DB credentials.
3. Run the app:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints

- POST `/formdata/` - Create new form data
- GET `/formdata/{id}` - Retrieve form data by ID
