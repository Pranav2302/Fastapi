# FastAPI Project Setup Guide 🚀
## 📖 How to Use
View API documentation at **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**.

This guide helps you set up and run the FastAPI backend.

## 🔧 Steps to Start the Server
### 1️⃣ Create a Virtual Environment
```sh
python -m venv venv
```

2️⃣ Activate the Virtual Environment
```
venv\Scripts\activate
```

3️⃣ Install Required Dependencies
```
pip install fastapi uvicorn sqlalchemy alembic python-jose[cryptography] passlib[bcrypt] python-multipart aiosqlite
```

4️⃣ Run the FastAPI Server
```
uvicorn app.main:app --reload

```
<img src="fastapi.png" alt="Alt Text" width="300" />

