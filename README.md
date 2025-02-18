# FastAPI Project Setup Guide 🚀

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

