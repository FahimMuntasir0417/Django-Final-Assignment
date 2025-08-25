# 🏠 House Rental Platform - Django REST Framework API

A comprehensive **house rental platform** built with **Django REST Framework (DRF)**.  
The platform enables users to **create, browse, and manage rental advertisements** with advanced features such as rent requests, favorites, reviews, messaging, notifications, and an analytics dashboard for admins.

---

## ✨ Features

- **User Authentication**: Secure **JWT-based authentication** system
- **Rent Advertisements**: Create, view, update, and delete rental listings
- **Admin Moderation**: Approval system for rental advertisements
- **Rent Requests**: Users can send rent requests to property owners
- **Favorites System**: Save and manage favorite advertisements
- **Reviews & Ratings**: Rate and review rental properties
- **Advanced Filtering**: Filter advertisements by category, price, amenities, etc.
- **Notifications**: Real-time notifications for important events
- **Messaging System**: Direct user-to-user messaging
- **Statistics Dashboard**: Admin dashboard with analytics and statistics

---

## 🛠 Tech Stack

- **Backend**: Django 4.2, Django REST Framework
- **Database**: PostgreSQL (recommended) or SQLite (for development)
- **Authentication**: JWT (JSON Web Tokens) via `djangorestframework-simplejwt`
- **File Storage**: Django Storage (for property images)
- **API Documentation**: DRF Spectacular (OpenAPI 3.0)

---

## 🚀 Installation

### ✅ Prerequisites

- Python **3.8+**
- PostgreSQL (optional but recommended)
- `virtualenv`

---

### ⚡ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/house-rental-platform.git
   cd house-rental-platform
   ```

# 📌 Django REST Framework API Endpoints

Below is the complete list of **API endpoints** available in the **House Rental Platform**.  
These endpoints follow **RESTful principles** and are secured with **JWT Authentication**.

---

## 🔑 Authentication Endpoints

### **Djoser Endpoints** (`/auth/`)

- **POST** `/auth/users/` – Create user (register)
- **POST** `/auth/users/activation/` – Activate user
- **POST** `/auth/jwt/create/` – Login (get JWT tokens)
- **POST** `/auth/jwt/refresh/` – Refresh JWT token
- **POST** `/auth/jwt/verify/` – Verify JWT token
- **GET** `/auth/users/me/` – Get current user profile
- **PUT** `/auth/users/me/` – Update current user profile
- **PATCH** `/auth/users/me/` – Partial update current user
- **DELETE** `/auth/users/me/` – Delete current user
- **POST** `/auth/users/reset_password/` – Reset password
- **POST** `/auth/users/reset_password_confirm/` – Confirm password reset

### **Custom Authentication Endpoints**

- **POST** `/auth/jwt/create/` – Get JWT token pair
- **POST** `/auth/jwt/refresh/` – Refresh JWT token
- **POST** `/auth/jwt/verify/` – Verify JWT token
- **POST** `/auth/logout/` – Logout user

---

## 👤 User Management Endpoints

- **GET** `/profile/` – Get user profile
- **POST** `/profile/image/` – Upload profile image
- **GET** `/profile/check-phone/{phone_number}/` – Check phone number availability
- **GET** `/users/` – List all users

---

## 🏷 Category Endpoints (`/categories/`)

- **GET** `/categories/` – List all categories
- **POST** `/categories/` – Create new category
- **GET** `/categories/{id}/` – Retrieve specific category
- **PUT** `/categories/{id}/` – Update category
- **PATCH** `/categories/{id}/` – Partial update category
- **DELETE** `/categories/{id}/` – Delete category

---

## 🛋 Amenity Endpoints (`/amenities/`)

- **GET** `/amenities/` – List all amenities
- **POST** `/amenities/` – Create new amenity
- **GET** `/amenities/{id}/` – Retrieve specific amenity
- **PUT** `/amenities/{id}/` – Update amenity
- **PATCH** `/amenities/{id}/` – Partial update amenity
- **DELETE** `/amenities/{id}/` – Delete amenity

---

## 📢 Advertisement Endpoints (`/advertisements/`)

- **GET** `/advertisements/` – List all advertisements
- **POST** `/advertisements/` – Create new advertisement
- **GET** `/advertisements/{id}/` – Retrieve specific advertisement
- **PUT** `/advertisements/{id}/` – Update advertisement
- **PATCH** `/advertisements/{id}/` – Partial update advertisement
- **DELETE** `/advertisements/{id}/` – Delete advertisement

### 🔗 Nested Advertisement Endpoints

#### **Images** (`/advertisements/{advertisement_pk}/images/`)

- **GET** `/advertisements/{advertisement_pk}/images/` – List all images
- **POST** `/advertisements/{advertisement_pk}/images/` – Add image
- **GET** `/advertisements/{advertisement_pk}/images/{id}/` – Get specific image
- **PUT** `/advertisements/{advertisement_pk}/images/{id}/` – Update image
- **PATCH** `/advertisements/{advertisement_pk}/images/{id}/` – Partial update image
- **DELETE** `/advertisements/{advertisement_pk}/images/{id}/` – Delete image

#### **Reviews** (`/advertisements/{advertisement_pk}/reviews/`)

- **GET** `/advertisements/{advertisement_pk}/reviews/` – List all reviews
- **POST** `/advertisements/{advertisement_pk}/reviews/` – Add review
- **GET** `/advertisements/{advertisement_pk}/reviews/{id}/` – Get specific review
- **PUT** `/advertisements/{advertisement_pk}/reviews/{id}/` – Update review
- **PATCH** `/advertisements/{advertisement_pk}/reviews/{id}/` – Partial update review
- **DELETE** `/advertisements/{advertisement_pk}/reviews/{id}/` – Delete review

#### **Rent Requests** (`/advertisements/{advertisement_pk}/rent-requests/`)

- **GET** `/advertisements/{advertisement_pk}/rent-requests/` – List all rent requests
- **POST** `/advertisements/{advertisement_pk}/rent-requests/` – Create rent request
- **GET** `/advertisements/{advertisement_pk}/rent-requests/{id}/` – Get specific rent request
- **PUT** `/advertisements/{advertisement_pk}/rent-requests/{id}/` – Update rent request
- **PATCH** `/advertisements/{advertisement_pk}/rent-requests/{id}/` – Partial update rent request
- **DELETE** `/advertisements/{advertisement_pk}/rent-requests/{id}/` – Delete rent request

---

## 📑 Rent Request Endpoints (`/rent-requests/`)

- **GET** `/rent-requests/` – List all rent requests
- **POST** `/rent-requests/` – Create new rent request
- **GET** `/rent-requests/{id}/` – Retrieve specific rent request
- **PUT** `/rent-requests/{id}/` – Update rent request
- **PATCH** `/rent-requests/{id}/` – Partial update rent request
- **DELETE** `/rent-requests/{id}/` – Delete rent request

---

## ❤️ Favorite Endpoints (`/favorites/`)

- **GET** `/favorites/` – List all favorites
- **POST** `/favorites/` – Add to favorites
- **GET** `/favorites/{id}/` – Retrieve specific favorite
- **PUT** `/favorites/{id}/` – Update favorite
- **PATCH** `/favorites/{id}/` – Partial update favorite
- **DELETE** `/favorites/{id}/` – Remove from favorites

---

## ⭐ Review Endpoints (`/reviews/`)

- **GET** `/reviews/` – List all reviews
- **POST** `/reviews/` – Create new review
- **GET** `/reviews/{id}/` – Retrieve specific review
- **PUT** `/reviews/{id}/` – Update review
- **PATCH** `/reviews/{id}/` – Partial update review
- **DELETE** `/reviews/{id}/` – Delete review

---

## 🔔 Notification Endpoints (`/notifications/`)

- **GET** `/notifications/` – List all notifications
- **POST** `/notifications/` – Create new notification
- **GET** `/notifications/{id}/` – Retrieve specific notification
- **PUT** `/notifications/{id}/` – Update notification
- **PATCH** `/notifications/{id}/` – Partial update notification
- **DELETE** `/notifications/{id}/` – Delete notification

---

## 💬 Message Endpoints (`/messages/`)

- **GET** `/messages/` – List all messages
- **POST** `/messages/` – Create new message
- **GET** `/messages/{id}/` – Retrieve specific message
- **PUT** `/messages/{id}/` – Update message
- **PATCH** `/messages/{id}/` – Partial update message
- **DELETE** `/messages/{id}/` – Delete message

---

## 📊 Statistics Endpoint

- **GET** `/statistics/` – Get advertisement statistics

---

## 🖼 Media Files (Development Only)

- **GET** `/media/{file_path}` – Serve media files (images, etc.)

---

## ✅ Key Features of API

- Fully **RESTful API** with proper HTTP methods (GET, POST, PUT, PATCH, DELETE)
- **Nested routes** for advertisement-related resources (images, reviews, rent requests)
- **JWT Authentication** with refresh & verify tokens
- User management with **profile & image upload**
- **Comprehensive CRUD** for all models
- Media file serving in **development mode**
- Testable with **Postman, curl, or DRF Browsable API** at `/api/` (if enabled)

---
