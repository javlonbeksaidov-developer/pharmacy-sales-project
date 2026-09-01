<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&section=header&text=Pharmacy%20Sales&fontSize=55&fontAlignY=35&animation=fadeIn&fontColor=ffffff" width="100%"/>

<a href="https://github.com/javlonbeksaidov-developer">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=3776AB&center=true&vCenter=true&width=600&lines=Python+FastAPI+SQLite3;Create+%E2%80%A2+Read+%E2%80%A2+Update+%E2%80%A2+Delete;pharmacy+sales+project" alt="Typing SVG" />
</a>

<br>

  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-Framework-009688?style=flat-square&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pydantic-Validation-E92063?style=flat-square&logo=pydantic&logoColor=white" />
  <img src="https://img.shields.io/badge/Uvicorn-ASGI-499848?style=flat-square" />

</div>

## 📖 About

Dorixonada dorilar, kassirlar va savdo cheklarining kirim-chiqimini boshqarish uchun yaratilgan **REST API** loyiha.

Loyiha **FastAPI** va **SQLAlchemy** yordamida ishlab chiqilgan bo‘lib, foydalanuvchilar, dorilar, cheklar va chek tarkibidagi mahsulotlarni boshqarish imkonini beradi.

**Start Project:** `18.08.2026`

**Status:** ✅ Completed

---

## 🚀 Features

* 👤 Foydalanuvchilarni boshqarish
* 💊 Dorilarni boshqarish
* 🧾 Cheklar bilan ishlash
* 📦 Chek tarkibidagi dorilarni boshqarish
* 🔄 CRUD operations
* 👨‍💼 Admin va kassir rollari
* 🗄️ SQLAlchemy ORM
* 📚 Swagger API Documentation

---

## 🛠️ Tech Stack

| Technology     | Description             |
| -------------- | ----------------------- |
| 🐍 Python      | Backend dasturlash tili |
| ⚡ FastAPI      | REST API framework      |
| 🗄️ SQLAlchemy | ORM                     |
| 📦 Pydantic    | Data validation         |
| 🚀 Uvicorn     | ASGI server             |

---

## 📁 Project Structure

```text
pharmacy-sales-project/
│
├── app/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes_user.py
│   ├── routes_drug.py
│   ├── routes_check.py
│   └── routes_check_item.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔗 API Endpoints

### 👤 Users

| Method   | Endpoint                  | Description            |
| -------- | ------------------------- | ---------------------- |
| `POST`   | `/users/register/`        | Yangi user yaratish    |
| `GET`    | `/users/`                 | Barcha userlarni olish |
| `GET`    | `/users/admins/`          | Adminlarni olish       |
| `GET`    | `/users/cashier/`         | Kassirlarni olish      |
| `GET`    | `/users/{user_id}`        | ID orqali user olish   |
| `PUT`    | `/users/update/{user_id}` | Userni yangilash       |
| `DELETE` | `/users/delete/{user_id}` | Userni o‘chirish       |

### 💊 Drugs

| Method   | Endpoint                  | Description            |
| -------- | ------------------------- | ---------------------- |
| `POST`   | `/drugs/create/`          | Dori yaratish          |
| `GET`    | `/drugs/`                 | Barcha dorilarni olish |
| `GET`    | `/drugs/{drug_id}`        | ID orqali dori olish   |
| `PUT`    | `/drugs/update/{drug_id}` | Dorini yangilash       |
| `DELETE` | `/drugs/delete/{drug_id}` | Dorini o‘chirish       |

### 🧾 Checks

| Method   | Endpoint                    | Description            |
| -------- | --------------------------- | ---------------------- |
| `POST`   | `/checks/create/`           | Yangi chek yaratish    |
| `GET`    | `/checks/`                  | Barcha cheklarni olish |
| `GET`    | `/checks/{check_id}`        | ID orqali chek olish   |
| `PUT`    | `/checks/update/{check_id}` | Chekni yangilash       |
| `DELETE` | `/checks/delete/{check_id}` | Chekni o‘chirish       |

### 📦 Check Items

| Method   | Endpoint                              | Description                  |
| -------- | ------------------------------------- | ---------------------------- |
| `POST`   | `/check-items/create/`                | Chekka dori qo‘shish         |
| `GET`    | `/check-items/`                       | Barcha chek itemlarini olish |
| `GET`    | `/check-items/{check_item_id}`        | ID orqali olish              |
| `PUT`    | `/check-items/update/{check_item_id}` | Chek itemini yangilash       |
| `DELETE` | `/check-items/delete/{check_item_id}` | Chek itemini o‘chirish       |

---

# 🚀 Installation

## 1️⃣ Clone repository

```bash
git clone https://github.com/javlonbeksaidov-developer/pharmacy-sales-project.git
```

## 2️⃣ Project folder

```bash
cd pharmacy-sales-project
```

## 3️⃣ Create virtual environment

```bash
python -m venv venv
```

## 4️⃣ Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / MacOS

```bash
source venv/bin/activate
```

## 5️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

## 6️⃣ Run the Project

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

You can test all CRUD operations directly from Swagger UI.


---

<div align="center">

# 👨‍💻 Author

<table align="center">
<tr>
<td align="center" width="220">

<img src="https://github.com/javlonbeksaidov-developer.png" width="150" height="150" style="border-radius:50%;" />

</td>

<td align="center">

<h3>SOFTWARE ENGINEER</h3>

<h3>Connect with me</h3>

<p align="center"><a href="https://t.me/saidov_1701"><img src="https://img.icons8.com/fluency/64/telegram-app.png" width="45" alt="Telegram"/></a>&nbsp;&nbsp;&nbsp;<a href="https://instagram.com/#"><img src="https://img.icons8.com/fluency/64/instagram-new.png" width="45" alt="Instagram"/></a>&nbsp;&nbsp;&nbsp;<a href="https://facebook.com/javlonbeksaidov.developer"><img src="https://img.icons8.com/fluency/64/facebook-new.png" width="45" alt="Facebook"/></a>&nbsp;&nbsp;&nbsp;<a href="https://youtube.com/@JavlonbekSaidov-Developer"><img src="https://img.icons8.com/fluency/64/youtube-play.png" width="45" alt="YouTube"/></a>&nbsp;&nbsp;&nbsp;<a href="mailto:javlonbeksaidov09@gmail.com"><img src="https://img.icons8.com/fluency/64/gmail-new.png" width="45" alt="Gmail"/></a></p>

</td>
</tr>
</table>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=2500&pause=1000&center=true&vCenter=true&width=650&lines=Javlonbek+Saidov+Alijon+o%27g%27li;Python+Backend+Developer" alt="Typing SVG" />

<br><br>

<strong>⭐ If you like this project, don't forget to give it a star!</strong>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer&animation=fadeIn" width="100%"/>

