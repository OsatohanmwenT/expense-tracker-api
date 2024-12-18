# Expense Tracking and Budgeting API

The **Expense Tracking and Budgeting API** helps individuals manage their finances by tracking expenses, setting budgets, and generating real-time alerts. The API supports user authentication, secure data management, and easy integration with third-party services.

## Problem Solved

Managing personal finances can be overwhelming. This API simplifies the process by enabling users to:

- **Track expenses**: Categorize and store expenses with various attributes.
- **Set budgets**: Create, update, and monitor budgets, ensuring users stay within their spending limits.
- **Automate alerts**: Get notified when spending exceeds or approaches predefined limits.
- **Visualize data**: Gain insights into spending habits with analytics and visual breakdowns.

## Key Features

- **User Management**: Register, log in, and authenticate users with JWT-based authentication.
- **Expense Tracking**: Add, update, and categorize expenses.
- **Budget Management**: Set and adjust budgets, track expenses against limits, and receive alerts.
- **Data Analytics**: Summarize expenses, view detailed breakdowns by category, and export data.
- **Real-time Notifications**: WebSocket support for live notifications of budget alerts.
- **Secure Access**: JWT-based authentication and password hashing for secure access to the system.
- **Group Expense Tracking**: Track expenses for groups of users, with automatic splitting of expenses.
- **Debt Notifications**: Get notified when debts are owed within a group, with real-time notifications for updates and payment status.

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM (SQLite also available as an alternative)
- **Authentication**: JWT, OAuth2
- **Notifications**: WebSocket-based live notifications
- **Data Visualization**: Integration with front-end for trends and expense tracking

---

## Installation

### Prerequisites

- **Python 3.12+**

---

### Using Pipenv

1. **Install Pipenv**:
   ```bash
   pip install pipenv
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/Incognitol07/expense-tracker-api.git
   cd expense-tracker-api
   ```

3. **Set up environment variables**:
   - Copy the `.env.example` file to `.env`:
     - **Mac/Linux**:
       ```bash
       cp .env.example .env
       ```
     - **Windows** (Command Prompt):
       ```cmd
       copy .env.example .env
       ```
     - **Windows** (PowerShell):
       ```powershell
       Copy-Item .env.example .env
       ```
   - Edit the `.env` file and update the variables with your configuration:
     ```plaintext
     ENVIRONMENT=development
     DB_HOST=localhost
     DB_NAME=expense_tracker
     DB_USER=postgres
     DB_PASSWORD=password
     JWT_SECRET_KEY=myjwtsecretkey
     MASTER_KEY=master_key
     ```

4. **Install dependencies**:
   ```bash
   pipenv install --ignore-pipfile
   ```

5. **Activate the virtual environment**:
   ```bash
   pipenv shell
   ```

6. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

---

### Without a Virtual Environment

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Incognitol07/expense-tracker-api.git
   cd expense-tracker-api
   ```

2. **Set up environment variables**:
   - Copy the `.env.example` file to `.env`:
     - **Mac/Linux**:
       ```bash
       cp .env.example .env
       ```
     - **Windows** (Command Prompt):
       ```cmd
       copy .env.example .env
       ```
     - **Windows** (PowerShell):
       ```powershell
       Copy-Item .env.example .env
       ```
   - Edit the `.env` file and update the variables with your configuration:
     ```plaintext
     ENVIRONMENT=development
     DB_HOST=localhost
     DB_NAME=expense_tracker
     DB_USER=postgres
     DB_PASSWORD=password
     JWT_SECRET_KEY=myjwtsecretkey
     MASTER_KEY=master_key
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   uvicorn app.main:app --reload
   ```

   The application will be available at `http://127.0.0.1:8000`.

## Features Overview

### Real-Time Notifications

- **WebSocket Endpoint**: `http://127.0.0.1:8000/ws/notifications/{user_id}` - Connect to this WebSocket endpoint for live notifications about budget alerts and spending updates.

This feature allows users to stay updated with budget notifications in real-time, improving their ability to manage finances instantly.

---

### Group Expense Tracking and Debt Notifications

- **Group Creation**: Users can create groups and invite others to join by email. Upon acceptance, group members can share and track expenses.
- **Expense Splitting**: Expenses paid by one member can be split among all group members, with real-time updates sent through notifications.
- **Debt Notifications**: When expenses are split, users will receive notifications about how much they owe or are owed within the group. These notifications include the status of debt payments.

---

## Project Structure

```plaintext
expense-tracker-api/
├── app/
│   ├── main.py              # Application entry point
│   ├── websocket_manager.py # WebSocket connection management
│   ├── routers/             # API endpoint routers
│   ├── schemas/             # Pydantic models for request validation
│   ├── utils/               # Utility functions (e.g., security, notifications)
│   ├── models/              # SQLAlchemy models
│   ├── database.py          # Database connection and session handling
│   └── config.py            # Configuration settings
├── requirements.txt         # Versions of installed packages
├── Pipfile                  # Pipenv dependencies
├── Pipfile.lock             # Locked dependency versions
├── .env                     # Environment variables
└── README.md                # Project documentation
```

---

## Testing the API

You can test the API using **curl**, **Postman**, **Bruno**, or FastAPI's interactive docs available at `http://127.0.0.1:8000/docs` or `http://127.0.0.1:8000/redoc` for a more comprehensive documentation.

### Example Request

To register a new user:

```bash
curl -X POST "http://127.0.0.1:8000/auth/register" -H "accept: application/json" -H "Content-Type: application/json" -d '{"username": "testuser", "email": "test@user.com", "password": "password123"}'
```

### WebSocket Notifications

To test real-time notifications via WebSocket:

1. Connect to `http://127.0.0.1:8000/ws/notifications/{user_id}`.
2. Upon spending updates or threshold alerts, the connected WebSocket will receive messages in real time.

---

## Conclusion

The Expense Tracking and Budgeting API offers a robust system for managing personal finances, automating budget management, and visualizing financial data. With features like real-time alerts, secure authentication, group expense tracking, debt notifications, and comprehensive data tracking, this API helps users make informed decisions about their finances.

---

## License

This project is licensed under the MIT License.