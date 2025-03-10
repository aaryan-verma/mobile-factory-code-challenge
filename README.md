# 📱 Mobile Factory API

## 🚀 Overview
The **Mobile Factory API** is a FastAPI application designed to facilitate the creation of mobile phone orders by allowing users to select components from various categories, ensuring that each order adheres to specific validation rules.

## 💁‍♂️ Folder Structure
```
mobile-factory-code-challenge/
├── app/                          # Main application directory
│   ├── api/                      # Contains API route definitions
│   │   └── routes.py             # Defines the API endpoints and request handling
│   ├── core/                     # Core functionalities of the application
│   │   ├── config.py             # Configuration settings for the application
│   │   ├── logger.py             # Logging setup and configuration
│   │   ├── exceptions.py         # Custom exception classes for error handling
│   │   └── container.py          # Dependency injection container for managing service instances
│   ├── models/                   # Data models used in the application
│   │   ├── component.py          # Enum definitions for different components
│   │   └── order.py              # Pydantic models for order requests and responses
│   ├── repositories/             # Data storage and retrieval logic
│   │   └── order_repository.py    # In-memory order repository for storing orders
│   ├── services/                 # Business logic and service layer
│   │   ├── order_service.py      # Contains the logic for creating and managing orders
│   │   └── id_generator.py       # Logic for generating unique order IDs
│   └── utils/                    # Utility functions and constants
│       └── constants.py          # Constants used throughout the application
├── tests/                        # Directory for test files
├── logs/                         # Directory for log files generated by the application
├── main.py                       # Entry point for the FastAPI application
├── run.sh                        # Script to run the application
└── requirements.txt              # List of dependencies for the project
```

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/aaryan-verma/mobile-factory-code-challenge.git
cd mobile_factory
```

### 2️⃣ Create a Virtual Environment
```sh
python3 -m venv venv  # Create virtual environment
source ./venv/bin/activate  # Activate (Linux/Mac)
# On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the FastAPI Application
```sh
./venv/bin/uvicorn app.main:app --reload
```
The API will be available at: **http://127.0.0.1:8000**

### 5️⃣ Access API Documentation
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 📌 API Endpoints
### **1️⃣ Place an Order**
#### **POST** `/orders`
Creates a new mobile factory order.

#### **Request Body**
```json
{
  "components": ["A", "D", "F", "I", "K"]
}
```

#### **Response (201 - Created)**
```json
{
    "order_id": "MFC-7ed35dd9-SSVY1O",
    "total": 142.3,
    "parts": [
        "LED Screen",
        "Wide-Angle Camera",
        "USB-C Port",
        "Android OS",
        "Metallic Body"
    ]
}
```

#### **Error Response (400 - Bad Request)**
```json
{
    "detail": [
        {
            "type": "value_error",
            "loc": [
                "body",
                "components"
            ],
            "msg": "Value error, Invalid component codes: S",
            "input": [
                "A",
                "S",
                "F",
                "I",
                "K"
            ],
            "ctx": {
                "error": {}
            }
        }
    ]
}
```

### **2️⃣ Check Service Status**
#### **GET** `/health`
Checks if the service is running and operational.

#### **Response (200 - OK)**
```json
{
    "status": "ok",
    "message": "Service is running."
}
```

## 📌 Features
- **Robust Component Validation**: Ensures users select only valid components with checks for duplicates and category requirements.
- **Automatic Price Calculation**: Computes the total cost based on selected components.
- **Logging**: Logs all activities, including errors, into separate log files for easy monitoring.
- **User-Friendly API Documentation**: Interactive API docs via Swagger UI and ReDoc.
- **Comprehensive Unit Tests**: Covers scenarios such as valid orders, duplicate components, and invalid component codes.
- **Service Monitoring**: A `/health` endpoint allows quick service health checks without authentication.

## 🤖 Running Tests
Run unit tests with **pytest**:
```sh
pytest tests/
```

## 🏢 Technologies Used
- **FastAPI** (Web Framework)
- **Uvicorn** (ASGI Server)
- **Pydantic** (Data Validation)
- **Pytest** (Unit Testing)

## 📌 Notes
- The order must contain exactly **one part per category**: Screen, Camera, Port, OS, and Body.
- Invalid or duplicate categories will result in a **400 Bad Request** error.
- The `order_id` is generated using a custom ID generator for uniqueness.

---
## 📩 Contact
For issues or suggestions, please raise an issue on GitHub!

Happy Coding! 🚀

