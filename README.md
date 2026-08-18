start project 18.08.2026
# 💊 Pharmacy Sales Project

Dorixonada dorilar, kassirlar va savdo cheklarining kirim-chiqimini boshqarish uchun yaratilgan **REST API** loyiha.

Loyiha **FastAPI** va **SQLAlchemy** yordamida ishlab chiqilgan bo‘lib, foydalanuvchilar, dorilar, cheklar va chek tarkibidagi mahsulotlarni boshqarish imkonini beradi.

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

Loyihaning dependency'lari `requirements.txt` faylida berilgan.

---

## 📁 Project Structure

```text
pharmacy-sales-project/
│
├── app/
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
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

## 🗃️ Database Models

Loyihada 4 ta asosiy model mavjud:

### 👤 Users

Foydalanuvchilarni saqlaydi.

* `id`
* `username`
* `password`
* `full_name`
* `role`

Rollar:

* `ADMIN`
* `CASHIER`

### 💊 Drugs

Dorilar haqidagi ma'lumotlarni saqlaydi.

* `id`
* `name`
* `amount`
* `desc`
* `base_price`
* `cell_price`
* `bar_code`

### 🧾 Checks

Savdo cheklari haqidagi ma'lumotlarni saqlaydi.

* `id`
* `check_num`
* `date_created`
* `cashier_id`

### 📦 CheckItem

Chek tarkibidagi dorilarni saqlaydi.

* `id`
* `amount`
* `drug_id`
* `check_id`

Ushbu modellar orasidagi bog‘lanishlar SQLAlchemy `relationship` va `ForeignKey` orqali tashkil qilingan.

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

## ⚙️ Installation

### 1. Repository'ni clone qilish

```bash
git clone https://github.com/javlonbeksaidov-developer/pharmacy-sales-project.git
```

### 2. Project papkasiga o'tish

```bash
cd pharmacy-sales-project
```

### 3. Virtual environment yaratish

```bash
python -m venv venv
```

### 4. Virtual environment'ni yoqish

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 5. Dependency'larni o‘rnatish

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Project

FastAPI serverni ishga tushirish:

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

Server ishga tushgandan keyin Swagger UI orqali API'larni test qilish mumkin:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 👨‍💻 Author

**Javlonbek Saidov**

🐙 GitHub: [javlonbeksaidov-developer](https://github.com/javlonbeksaidov-developer)

---

## ⭐ Support

Agar loyiha foydali bo‘lsa, repository'ga ⭐ **Star** bosishni unutmang.

**Made with ❤️ and Python**
