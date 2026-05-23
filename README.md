# 🛒 ECommerce Analytics Dashboard

> A **full-stack analytics dashboard** for e-commerce sales data — built with Flask, SQLite, Chart.js and deployed live on Render.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)
![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)

---

## 🌐 Live Demo

👉 **[View Live Dashboard](https://ecommerce-analytics.onrender.com)**

---

## ✨ Features

- 📊 **5 KPI Cards** — Revenue, Profit, Orders, Avg Order Value, Regions
- 📈 **Monthly Revenue & Profit** bar chart
- 🍩 **Sales by Category** donut chart
- 🏆 **Top Products** horizontal bar chart
- 🗺️ **Revenue by Region** polar chart
- 🧾 **Recent Orders** live table
- 🔌 **REST API** — 6 endpoints for data access
- 🚀 **Deployed live** on Render.com

---

## 🗂️ Project Structure

```
EcommerceAnalytics-Dashboard/
├── app.py               # Flask routes
├── database.py          # SQLite + all queries
├── templates/
│   └── dashboard.html   # Full frontend (Chart.js)
├── requirements.txt     # Flask + Gunicorn
├── render.yaml          # Render deploy config
├── Procfile             # Gunicorn start command
└── README.md
```

---

## 🚀 Run Locally

```bash
git clone https://github.com/Eshwarkadari/EcommerceAnalytics-Dashboard
cd EcommerceAnalytics-Dashboard
pip install flask gunicorn
python app.py
```
Open **http://localhost:5000**

---

## 🔌 REST API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /api/kpis` | Total revenue, profit, orders |
| `GET /api/monthly-revenue` | Month-wise revenue & profit |
| `GET /api/category-sales` | Sales breakdown by category |
| `GET /api/top-products` | Top 8 products by revenue |
| `GET /api/recent-orders` | Last 10 orders |
| `GET /api/region-sales` | Revenue by region |

---

## 🚀 Deploy on Render (Free)

1. Fork this repo
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Set: **Build Command** = `pip install -r requirements.txt`
5. Set: **Start Command** = `gunicorn app:app`
6. Click **Deploy** — live in 2 minutes!

---

## 👨‍💻 Author

**Kadari Eshwar** — ECE Student, JNTU Hyderabad
[GitHub](https://github.com/Eshwarkadari) | [LinkedIn](https://www.linkedin.com/in/eshwar-kadari-134aa4278)
