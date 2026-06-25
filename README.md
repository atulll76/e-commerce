# E-Commerce API Backend

A modern, async RESTful e-commerce API built with **FastAPI**, **SQLAlchemy 2.0 (Async)**, and **MySQL (aiomysql)**, implementing a decoupled **Service Layer** and **Repository Pattern**.

---

## Architecture Overview

The system follows a strict layered architecture:
`FastAPI Router (HTTP controllers)` ➔ `Service Layer (Transaction Boundaries & Business Logic)` ➔ `Repository Layer (Database Queries & Data Access)` ➔ `SQLAlchemy Models`

- **Routers**: Handles HTTP protocol operations, serialization, input validation, and maps routes to service endpoints.
- **Service Layer**: Manages SQLAlchemy `AsyncSession` transaction boundaries (`commit`/`rollback`) and coordinates operations across repositories.
- **Repository Layer**: Provides reusable data-access interfaces mapping queries to databases.

---

## API Documentation & Resource Usage

All write operations (POST, PUT, DELETE) automatically execute inside database transaction blocks. Rollbacks are managed at the Service Layer on any failure.

### 1. Users Endpoint (`/users`)

Manages customer profiles, emails, usernames, and addresses.

| Method | Endpoint | Description | Request Body | Response Model |
| :--- | :--- | :--- | :--- | :--- |
| **POST** | `/users` | Create a new user profile | `UserCreate` | `UserResponse` |
| **GET** | `/users` | Retrieve paginated users list | *None* (query params: `skip`, `limit`) | `List[UserResponse]` |
| **GET** | `/users/{user_id}` | Retrieve a user profile by ID | *None* | `UserResponse` |
| **PUT** | `/users/{user_id}` | Update user details by ID | `UserUpdate` | `UserResponse` |
| **DELETE** | `/users/{user_id}`| Delete a user by ID | *None* | `UserResponse` |

#### Sample User Payload (`POST /users`)
```json
{
  "first_name": "Atul",
  "last_name": "Chauhan",
  "username": "atul01",
  "email": "atul01@gmail.com",
  "password": "supersecurepassword123",
  "phone_number": "+919876543210",
  "date_of_birth": "1995-08-15"
}
```

---

### 2. Products Endpoint (`/products`)

Manages inventory catalog, pricing, category classification, and manufacturers.

| Method | Endpoint | Description | Request Body | Response Model |
| :--- | :--- | :--- | :--- | :--- |
| **POST** | `/products` | Create a new product entry | `ProductCreate` | `ProductResponse` |
| **GET** | `/products` | Retrieve paginated product list | *None* (query params: `skip`, `limit`) | `List[ProductResponse]` |
| **GET** | `/products/{product_id}`| Retrieve product details by ID | *None* | `ProductResponse` |
| **PUT** | `/products/{product_id}`| Update product details | `ProductUpdate` | `ProductResponse` |
| **DELETE** | `/products/{product_id}`| Delete a product by ID | *None* | `ProductResponse` |

#### Sample Product Payload (`POST /products`)
```json
{
  "manufacturer_id": 1,
  "category_id": 2,
  "product_name": "Nike Air Zoom Pegasus 40",
  "product_description": "Premium daily running shoes with responsive cushioning.",
  "color": "Black/White",
  "size": "UK-9",
  "material": "Mesh/Synthetics",
  "gender": "Unisex",
  "price": 6999.00,
  "stock_quantity": 50,
  "image_url": "https://example.com/images/nike-pegasus-40.jpg",
  "is_active": true
}
```

---

### 3. Orders Endpoint (`/orders`)

Coordinates e-commerce order checkout flows, transaction management, and stock reservations.

| Method | Endpoint | Description | Request Body | Response Model |
| :--- | :--- | :--- | :--- | :--- |
| **POST** | `/orders` | Atomic checkout (updates stock & creates order) | `OrderCreate` | `OrderResponse` |
| **GET** | `/orders` | Retrieve paginated orders list | *None* (query params: `skip`, `limit`) | `List[OrderResponse]` |
| **GET** | `/orders/{order_id}` | Retrieve order details by ID | *None* | `OrderResponse` |
| **PUT** | `/orders/{order_id}` | Update order/payment status | `OrderUpdate` | `OrderResponse` |
| **DELETE** | `/orders/{order_id}`| Delete/cancel an order by ID | *None* | `OrderResponse` |

#### Sample Order Payload (`POST /orders`)
```json
{
  "user_id": 1,
  "address_id": 1,
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 3,
      "quantity": 1
    }
  ]
}
```

---

### 4. Verification Endpoints (`/verify`)

Lightweight endpoints used specifically for pipeline testing, repository pattern validation, and integration tests.

- `GET /verify/users/{user_id}`: Fetches basic user information directly from repository.
- `GET /verify/products/{product_id}`: Fetches basic product details.
- `POST /verify/orders`: Submits a test order utilizing transactional service operations.

---

## Running the Application Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up your MySQL database with `sql/ddl.sql` schema and update credentials in database configuration.
3. Start the FastAPI development server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Access interactive API documentation at: [http://localhost:8000/docs](http://localhost:8000/docs).
