# FastAPI Project Setup Guide 🚀

This guide helps you set up and run the FastAPI backend.

## 🔧 Steps to Start the Server

### 1️⃣ Create a Virtual Environment
```sh
python -m venv venv

venv\Scripts\activate

pip install fastapi uvicorn sqlalchemy alembic python-jose[cryptography] passlib[bcrypt] python-multipart aiosqlite

uvicorn app.main:app --reload



