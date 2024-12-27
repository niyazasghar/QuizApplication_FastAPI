# Quiz Application

This **Quiz Application** is built with **FastAPI** and consists of three versions. Each version adds more functionality to the application. 

### **V1**: CRUD operations on Questions  
### **V2**: User Authentication 
### **V3**: Role-Based Authorization  

## Features

- **V1**: Create, Read, Update, and Delete quiz questions.
- **V2**: User authentication via JWT tokens to secure the API.
- **V3**: Role-based authorization where only authorized users with specific roles (admin, user) can access certain routes.

## Tech Stack

- **FastAPI**: A modern web framework for building APIs.
- **MySQL**: A relational database for storing quiz data.
- **SQLAlchemy**: ORM for handling database operations.
- **Pydantic**: Data validation and serialization.
- **JWT (JSON Web Tokens)**: For user authentication and session management.

## Prerequisites

- Python 3.7 or higher
- MySQL setup
- Virtual environment (optional but recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/niyazasghar/QuizApplication_FastAPI.git
cd QuizApplication_FastAPI
