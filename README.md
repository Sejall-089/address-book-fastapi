 
# Address Book API (FastAPI)

A simple Address Book backend API built using **FastAPI**, **SQLite**, and **SQLAlchemy**.

This API allows users to:

- Create an address
- Update an address
- Delete an address
- Retrieve all saved addresses
- Find addresses within a given radius from coordinates

---

# Tech Stack

- Python 3
- FastAPI
- SQLite
- SQLAlchemy
- Geopy
- Uvicorn

---

# Project Structure

address-book-fastapi
│
├── app
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── routes.py
│   └── logger.py
│
├── requirements.txt
├── README.md
└── .gitignore

---

# Setup Instructions

Clone the repository

git clone https://github.com/Sejall-089/address-book-fastapi.git

Move into the project directory

cd address-book-fastapi

Create virtual environment

python -m venv venv

Activate virtual environment

Windows:

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

---

# Run the Application

Start the FastAPI server

uvicorn app.main:app --reload

Server will run at:

http://127.0.0.1:8000

---

# API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

---

# Example API

Create Address

POST /addresses

Example request body:

{
  "name": "Home",
  "street": "MG Road",
  "city": "Pune",
  "latitude": 18.5204,
  "longitude": 73.8567
}

---

# Health Check

GET /health

Response:

{
  "status": "ok"
}

---

# Author

Sejal Gupta