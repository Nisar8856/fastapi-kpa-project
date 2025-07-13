# ⚡ FastAPI KPA Project – REST API with PostgreSQL

A high-performance REST API built using **FastAPI** and **PostgreSQL**.  
The project supports CRUD operations on form data and is documented with **Swagger UI** for easy testing.

## 📸 Screenshots


### ✅ Render Deployment
![Render](https://github.com/user-attachments/assets/b13c5d26-a0e4-4e8e-8b22-ae0a1c4f0b6c)


### ✅ Postman - API Test
![Postman](https://github.com/user-attachments/assets/475f33f1-7b23-4c47-b16a-3aa2118ad139)

---

## 🚀 Features

- ⚡ FastAPI framework for blazing-fast performance
- 🐘 PostgreSQL database integration via SQLAlchemy
- 📄 Automatic Swagger docs at `/docs`
- 📫 API tested using Postman and browser
- 🌐 Deployable on platforms like Render or Railway

---

## 🧰 Tech Stack

| Tech         | Purpose                    |
|--------------|-----------------------------|
| FastAPI      | Web framework               |
| PostgreSQL   | Relational database         |
| SQLAlchemy   | ORM for DB models           |
| Uvicorn      | ASGI server                 |
| Python-dotenv| Env variable management     |
| Swagger UI   | Auto API documentation      |

##✅  Create virtual environment

- python -m venv env
- env\Scripts\activate       # for Windows
- source env/bin/activate    # for macOS/Linux

##✅  Install dependencies
- pip install -r requirements.txt

## ✅ Setup .env file
- DB_NAME=your_db_name
- DB_USER=your_db_user
  
- DB_PASSWORD=your_db_password

- DB_HOST=localhost

- DB_PORT=5432

## 📦 Deployment 
 - Project is ready for deployment using Render, Railway, or Docker.
Just ensure start.sh and render.yaml are configured properly.






---

## 🔧 How to Run Locally

### ✅ Step 1: Clone the repo
```bash
git clone https://github.com/Nisar8856/fastapi-kpa-project.git
cd fastapi-kpa-project


