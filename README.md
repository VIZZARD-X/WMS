# 📦 Warehouse Management System (WMS)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

A comprehensive, full-stack web application designed to handle complex inventory logic, supplier tracking, and physical warehouse mapping. Built entirely from the ground up using Django and vanilla web technologies.

## 🚀 Key Features

* **Advanced Storage Mapping:** Dynamic tracking of physical warehouse architecture, including mapping items to specific Aisles and Storage Spaces based on capacity.
* **Supplier & Order Management:** Fully relational database tracking for suppliers, inbound orders, and outbound shipments.
* **Inventory Control:** Real-time dashboards and reports to monitor stock levels and item movement.
* **Secure Access:** Built-in user authentication and role-based access control for warehouse staff.

## 🛠️ Tech Stack

* **Backend:** Python 3, Django 
* **Frontend:** HTML5, CSS3, Vanilla JavaScript, Django Template Language (DTL)
* **Database:** SQLite (Configured for easy migration to PostgreSQL)

## 💻 Local Setup & Installation

If you'd like to run this project locally, follow these steps:

**1. Clone the repository**
`git clone https://github.com/VIZZARD-X/WMS.git`
`cd WMS`

**2. Create and activate a virtual environment**
*On Windows:*
`python -m venv venv`
`venv\Scripts\activate`

*On macOS/Linux:*
`python3 -m venv venv`
`source venv/bin/activate`

**3. Install Django**
`pip install django`

**4. Run database migrations**
`python manage.py makemigrations`
`python manage.py migrate`

**5. Start the development server**
`python manage.py runserver`

Navigate to `http://127.0.0.1:8000/` in your browser to view the application.

---
*Developed by [Vignesh A](https://github.com/VIZZARD-X).*
