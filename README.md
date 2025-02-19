# E-Commerce Store 🛒

A simple e-commerce web application built using **Flask**, **SQLAlchemy**, **Bootstrap**, and **JavaScript**. This project allows users to browse products, add them to their cart, and proceed with checkout.

## 🚀 Features

- 📦 **Product Listings:** View a list of available products with images, descriptions, and prices.
- 🛒 **Shopping Cart:** Add products to the cart and see a summary before checkout.
- 💳 **Checkout Process:** Enter shipping and payment details to complete an order.
- 🛠️ **Admin Dashboard:** Manage products, including adding new items.
- 🎨 **Responsive UI:** Designed with **Bootstrap** for a modern and mobile-friendly interface.

---

## 📚 Project Structure

```
/e-commerce-store
│️️️static/
│️   ├️─ css/custom.css       # Custom styles
│️   └️─ js/main.js           # JavaScript for frontend interactivity
│️️templates/
│️   ├️─ base.html            # Main template layout
│️   ├️─ index.html           # Homepage displaying products
│️   ├️─ product.html         # Individual product details
│️   ├️─ cart.html            # Shopping cart page
│️   ├️─ checkout.html        # Checkout page
│️   └️─ admin.html           # Admin panel to manage products
│️app.py                   # Main Flask application
│️models.py                # Database models using SQLAlchemy
│️routes.py                # Routes for handling requests
│️pyproject.toml           # Dependencies and project settings
│️replit.nix               # Replit configuration
│️uv.lock                  # Package lock file
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/e-commerce-store.git
cd e-commerce-store
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3️⃣ Set Up the Database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4️⃣ Run the Application
```bash
flask run
```
Visit `http://127.0.0.1:5000/` in your browser.

---

## 🎨 Technologies Used

- **Backend:** Flask, Flask-SQLAlchemy, Flask-Session
- **Frontend:** Bootstrap, JavaScript, HTML, CSS
- **Database:** PostgreSQL (or SQLite for local testing)
- **Deployment:** Gunicorn (for production)

---

## 🌝 Screenshots

| Homepage | Product Page | Cart Page |
|----------|------------|----------|
| ![Homepage](screenshots/home.png) | ![Product](screenshots/product.png) | ![Cart](screenshots/cart.png) |

---

## 🛠️ Future Improvements

- 🔍 **Search Functionality:** Implement search for products.
- 🏷️ **Categories & Filters:** Allow users to filter by category.
- 📧 **Email Notifications:** Send confirmation emails after checkout.
- 🏦 **Payment Integration:** Add Stripe or PayPal for real payments.

---

## 👨‍💻 Author
Built by Mira Kapoor Wadehra (https://github.com/mirakw).

---

### ⭐ If you like this project, consider giving it a **star** on GitHub!

