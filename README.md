# 📦 Warehouse Management System (WMS)

A comprehensive warehouse and inventory management system built with **Django** (Backend) and **Vanilla JavaScript** (Frontend), using **SQLite/PostgreSQL** for data storage. Designed to manage physical warehouse layouts, inventory flow, and logistics operations efficiently.

---

## 🚀 Features

### 🏢 Warehouse Management
- Create and manage warehouses
- Define **Aisles, Racks, Shelves, and Bins**
- Track storage capacity usage in real time
- Visual mapping of item locations

### 📦 Inventory Management
- Add and manage SKUs with metadata (dimensions, category, supplier)
- Real-time stock quantity updates
- Track inward and outward item movement
- Prevent duplicate or invalid stock operations

### 🚛 Logistics & Orders
- Supplier management
- Purchase order creation and tracking
- Goods inward (GRN) processing
- Outbound shipment tracking

### 🔐 Authentication & Authorization
- Role-based access control (Admin, Manager, Staff)
- Secure login with Django authentication
- Action-level permissions
- Complete audit trail via Django Admin

---

## 🛠️ Tech Stack

### Backend
- **Framework**: Django 5.x
- **Language**: Python 3.10+
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Authentication**: Django Auth
- **Templating**: Django Template Language (DTL)

### Frontend
- **Languages**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS
- **Interactivity**: Vanilla JavaScript (DOM manipulation)

### DevOps & Tools
- **Version Control**: Git & GitHub
- **Environment**: Virtualenv
- **Server**: Gunicorn (Production-ready)

---

## 📋 Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.10+ | Runtime |
| Git | Latest | Version Control |
| VS Code | Recommended | Development |

### Verify Installation
```bash
python --version
git --version
```
---
### 🚀 Quick Start Guide

### Step 1: Clone the Repository
```bash
git clone https://github.com/VIZZARD-X/WMS.git
cd WMS
```
### Step 2: Backend Setup
#### 2.1 Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```
#### 2.2 Install Dependencies
```bash
pip install -r requirements.txt
```
#### 2.3 Environment Configuration
Create a .env file:
```bash
SECRET_KEY=dev-secret-change-me
DEBUG=True
DATABASE=sqlite
```
#### 2.4 Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
#### 2.5 Create Superuser
```bash
python manage.py createsuperuser
```
#### 2.6 Run Development Server
```bash
python manage.py runserver
```
##### Access:
- Application: http://127.0.0.1:8000/
 - Admin Panel: http://127.0.0.1:8000/admin/
--- 
### 📁 Project Structure
```bash
WMS/
│
├── warehouse/                  # Core Application
│   ├── models.py               # Warehouse, Inventory, Orders
│   ├── views.py                # Business logic
│   ├── urls.py                 # App routing
│   ├── admin.py                # Admin configuration
│   └── migrations/
│
├── templates/
│   ├── auth/                   # Authentication pages
│   ├── warehouse/              # Warehouse views
│   └── inventory/              # Inventory pages
│
├── static/
│   ├── css/
│   └── js/
│
├── wms/                        # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```
---
### 🧩 Database Schema

#### Warehouses
```bash
- id (PK)
- name
- location
- total_capacity
- created_at
```
#### Storage Units
```bash
- id (PK)
- warehouse_id (FK)
- aisle
- rack
- shelf
- bin
- capacity
```
#### Items
```bash
- id (PK)
- sku (unique)
- name
- category
- length
- width
- height
- supplier_id (FK)
```
#### Inventory
```bash
- id (PK)
- item_id (FK)
- storage_unit_id (FK)
- quantity
- updated_at
```
#### Stock Movements
```bash
- id (PK)
- item_id (FK)
- movement_type (IN / OUT)
- quantity
- performed_by (FK -> User)
- timestamp
```
---
### 🔧 Common Commands
```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
```
---
### 🧪 Troubleshooting
#### Migrations not applying
```bash
python manage.py migrate --run-syncdb
```
#### Static files not loading
```bash
python manage.py collectstatic
```
#### Permission issues
- Verify user roles in Django Admin
- Check group-level permissions
---
### 🔐 Production Notes
- Set DEBUG=False
- Use PostgreSQL
- Configure ALLOWED_HOSTS
- Enable HTTPS
- Secure SECRET_KEY
- Restrict admin access
