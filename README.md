# 💹 Compounding Investment API

A Django REST API to simulate and track the compounding growth of investments over time. It automatically calculates and stores yearly compounded interests with monthly topups  and capital gains upon creation or update of investment data.

---

## 🚀 Features

- Create and manage investment portfolios.
- Automatically calculate monthly interest and capital gains using a compounding model.
- Update or delete individual investment entries.
- API endpoint to view all growth records related to an investment.
- PostgreSQL-backed with Django REST Framework for clean browsable API access.
- Trigger growth calculation on `POST` and `PUT`.

---

## 🧠 Tech Stack

- Python 3.12
- Django 5.2.4
- Django REST Framework 3.16.0
- PostgreSQL
- psycopg2-binary
- Postman (for testing)

---

## 🗂 Project Structure
```
.
├── compounding_investment/ # Project config
│ └── settings.py # Database + app settings
├── grow_your_wealth/ # Core investment logic
│ ├── models.py # Investment and InvestmentGrowth models
│ ├── calculator.py # Logic for computing growth over time
│ ├── signals.py # Trigger growth calculation after save
│ ├── views.py # DRF views (List, Detail)
│ ├── serializers.py # DRF serializers
│ ├── urls.py # App-specific API routes
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation & Setup

1. **Clone the repo:**

   ```bash
   git clone https://github.com/karianjahi/compounding_investment.git
   cd compounding_investment
   ```

2. **Create virtual environment & install dependencies:**
    ```
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. **PostgreSQL Setup:**
- Make sure PostgreSQL is installed and a DB named financedb exists:
    ```
    CREATE DATABASE financedb;
    CREATE USER karianjahi WITH PASSWORD 'Sagana&9sf';
    GRANT ALL PRIVILEGES ON DATABASE financedb TO karianjahi;
    ```

4. **Apply migrations:**
    ```
    python manage.py migrate
    ```

5. **Run development server:**
    ```
    python manage.py runserver
    ```

6. **Access API:**
    - Visit `http://127.0.0.1:8000/api/`

## 📬 API Usage
### 📌 Investment Endpoint

| Method | Endpoint                 | Description                             |
|--------|--------------------------|-----------------------------------------|
| GET    | `/investments/`          | List all investments                    |
| POST   | `/investments/`          | Create a new investment (triggers growth calculation) |
| GET    | `/investments/{id}/`     | Retrieve details of a specific investment |
| PUT    | `/investments/{id}/`     | Update an investment and recalculate growth |
| DELETE | `/investments/{id}/`     | Delete an investment                    |


### Example POST /api/investments/ body:
    ```
    {
    "initial_amount": 100000,
    "top_up": 5000,
    "interest_rate": 0.12,
    "duration_in_years": 5,
    "topup_frequency": "month",
    "company": "Mansa-X",
    "name": "Retirement Plan"
    }
    ```
### 📈 Investment Growth Endpoints

| Method | Endpoint                          | Description                                 |
|--------|-----------------------------------|---------------------------------------------|
| GET    | `/admin/`                         | Django Admin Dashboard                      |
| GET    | `/investments/`                   | List all investment records                 |
| GET    | `/investments/<int:pk>/`          | Retrieve details of one investment + its growth |


### Response format
    ```
    {
    "investment": 1,
    "year": 2024,
    "month": 1,
    "interest": "432.00",
    "capital_gains": "10432.00"
    }
    ```

## 🔁 Auto Calculation Logic
- Growth is calculated via calculator.py and connected through Django signals.py.
- When a new Investment is created or updated, existing growth entries are cleared and recalculated.

## 🧪 Testing the API
You can test endpoints using:

- Django’s Browsable API at http://127.0.0.1:8000/api/

- Postman: import and test endpoints directly.


## 🔒 Authentication
Currently no authentication is enabled — the API is public for development purposes.


## 🪪 License
This project is licensed under the MIT License.


## ✍️ Author
Developed by Dr.rer.nat Joseph Karianjahi Njeri

## 📌 TODOs / Suggestions
- Add user authentication and API token access.

- Build a simple frontend dashboard (optional).

- Add pagination for growth records.

- Add CSV export or reporting.

