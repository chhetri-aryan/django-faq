# FAQ Assignment

This assignment involves developing a FAQ system using the Django framework that supports multiple languages. The system integrates with Google Translate to automatically translate FAQ questions and answers into different languages. The process includes creating a model to store FAQs and their translations, implementing an API for retrieving them, and using Django REST Framework for API development. Additionally, the project incorporates rich text formatting for answers, uses Redis for caching translations, and provides an admin panel to easily manage FAQs.


## Table of Contents
+ Installation 
+ API Usage
+ Contribution
+ License

## Prerequisites
- Python 3.12 or later
- Django 5.1.5
- SQLite
- Redis

## ScreenShots:

| Image |
|-------|
| ![Image](https://github.com/user-attachments/assets/02716f71-6b4f-49c8-ac6a-210fe665986f) |
| ![Image](https://github.com/user-attachments/assets/3e608512-b0c3-46a8-a079-4d8bbcb52dbf) |
| ![Image](https://github.com/user-attachments/assets/f4bef59e-fa84-41cf-acdd-44bf6fa9150d) |
| ![Image](https://github.com/user-attachments/assets/6e246b09-9e6f-4bce-afed-5d476c7f7ac0) |
| ![Image](https://github.com/user-attachments/assets/8b24f7d9-0ef4-425d-98dc-e144c8fc21ef) |
| ![Image](https://github.com/user-attachments/assets/159c0a60-12cb-482b-9aea-ee384cad74c2) |

## Installation
Follow the steps provided below

### Step 1: Clone Repository
```bash
git clone <repository-url>
cd <project-directory>
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Set up the database
- Database chosen can be managed in `settings.py`
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 4: Create Super User
```bash
python manage.py createsuperuser
```

### Step 5: Run the server
```bash
python manage.py runserver
```

## Working
Access the stored FAQ's and create new ones in the admin panel at
`http://127.0.0.1:8000/faqs/?format=json` 
`http://127.0.0.1:8000/admin/`

## Contributions 
Contributions to carry forward and scale up this plain FAQ system are welcomed.

## License
Project is licensed under the MIT License.
