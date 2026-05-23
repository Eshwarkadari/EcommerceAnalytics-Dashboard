"""
database.py — SQLite Database with sample ecommerce data
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
"""

import sqlite3, os

DB = "ecommerce.db"

ORDERS = [
    ("2024-01-05","Ravi Kumar","Electronics","Laptop Pro",55000,1,0.05,"Hyderabad","South"),
    ("2024-01-08","Priya Sharma","Clothing","Silk Saree",3500,2,0.10,"Mumbai","West"),
    ("2024-01-12","Amit Patel","Electronics","Wireless Earbuds",2800,1,0.0,"Ahmedabad","West"),
    ("2024-01-15","Sneha Reddy","Books","Python Programming",650,3,0.0,"Bangalore","South"),
    ("2024-01-18","Vikram Singh","Electronics","Smart Watch",8500,1,0.05,"Delhi","North"),
    ("2024-01-22","Anita Joshi","Home","Coffee Maker",4200,1,0.0,"Pune","West"),
    ("2024-01-25","Rahul Nair","Clothing","Formal Shirt",1200,3,0.10,"Chennai","South"),
    ("2024-01-28","Deepika Rao","Beauty","Skincare Kit",2200,1,0.0,"Kolkata","East"),
    ("2024-02-02","Suresh Menon","Electronics","Bluetooth Speaker",3500,2,0.05,"Kochi","South"),
    ("2024-02-05","Kavya Iyer","Books","Data Science Guide",850,2,0.0,"Hyderabad","South"),
    ("2024-02-08","Ravi Kumar","Home","Air Purifier",12000,1,0.10,"Hyderabad","South"),
    ("2024-02-12","Priya Sharma","Electronics","Tablet 10inch",22000,1,0.05,"Mumbai","West"),
    ("2024-02-15","Amit Patel","Clothing","Running Shoes",4500,1,0.0,"Ahmedabad","West"),
    ("2024-02-18","Sneha Reddy","Beauty","Perfume Set",3800,1,0.10,"Bangalore","South"),
    ("2024-02-22","Vikram Singh","Electronics","Gaming Mouse",2200,1,0.0,"Delhi","North"),
    ("2024-02-25","Anita Joshi","Books","Machine Learning",950,1,0.0,"Pune","West"),
    ("2024-03-01","Rahul Nair","Home","Standing Desk",18000,1,0.05,"Chennai","South"),
    ("2024-03-05","Deepika Rao","Clothing","Ethnic Wear",5500,2,0.10,"Kolkata","East"),
    ("2024-03-08","Suresh Menon","Electronics","Laptop Pro",55000,1,0.0,"Kochi","South"),
    ("2024-03-12","Kavya Iyer","Beauty","Makeup Kit",4500,1,0.05,"Hyderabad","South"),
    ("2024-03-15","Ravi Kumar","Electronics","Smart TV 43inch",35000,1,0.10,"Hyderabad","South"),
    ("2024-03-18","Priya Sharma","Home","Coffee Maker",4200,2,0.0,"Mumbai","West"),
    ("2024-03-22","Amit Patel","Books","IoT Handbook",750,2,0.0,"Ahmedabad","West"),
    ("2024-03-25","Sneha Reddy","Electronics","Wireless Mouse",1200,3,0.05,"Bangalore","South"),
    ("2024-04-01","Vikram Singh","Clothing","Leather Jacket",8500,1,0.10,"Delhi","North"),
    ("2024-04-05","Anita Joshi","Electronics","Smart Watch",8500,2,0.0,"Pune","West"),
    ("2024-04-08","Rahul Nair","Beauty","Hair Care Set",2800,1,0.05,"Chennai","South"),
    ("2024-04-12","Deepika Rao","Home","Air Purifier",12000,1,0.0,"Kolkata","East"),
    ("2024-04-15","Suresh Menon","Clothing","Formal Suit",12000,1,0.10,"Kochi","South"),
    ("2024-04-18","Kavya Iyer","Electronics","Bluetooth Speaker",3500,1,0.05,"Hyderabad","South"),
    ("2024-05-02","Ravi Kumar","Books","Python Programming",650,5,0.0,"Hyderabad","South"),
    ("2024-05-05","Priya Sharma","Electronics","Gaming Mouse",2200,2,0.0,"Mumbai","West"),
    ("2024-05-08","Amit Patel","Home","Standing Desk",18000,1,0.05,"Ahmedabad","West"),
    ("2024-05-12","Sneha Reddy","Clothing","Silk Saree",3500,3,0.10,"Bangalore","South"),
    ("2024-05-15","Vikram Singh","Electronics","Tablet 10inch",22000,1,0.0,"Delhi","North"),
    ("2024-05-18","Anita Joshi","Beauty","Skincare Kit",2200,2,0.05,"Pune","West"),
    ("2024-05-22","Rahul Nair","Electronics","Laptop Pro",55000,1,0.10,"Chennai","South"),
    ("2024-05-25","Deepika Rao","Books","Data Science Guide",850,3,0.0,"Kolkata","East"),
    ("2024-06-01","Suresh Menon","Home","Coffee Maker",4200,3,0.0,"Kochi","South"),
    ("2024-06-05","Kavya Iyer","Electronics","Smart TV 43inch",35000,1,0.05,"Hyderabad","South"),
    ("2024-06-08","Ravi Kumar","Clothing","Running Shoes",4500,2,0.0,"Hyderabad","South"),
    ("2024-06-12","Priya Sharma","Beauty","Perfume Set",3800,2,0.10,"Mumbai","West"),
    ("2024-06-15","Amit Patel","Electronics","Wireless Earbuds",2800,3,0.0,"Ahmedabad","West"),
    ("2024-06-18","Sneha Reddy","Home","Air Purifier",12000,2,0.05,"Bangalore","South"),
    ("2024-07-01","Vikram Singh","Electronics","Laptop Pro",55000,1,0.0,"Delhi","North"),
    ("2024-07-05","Anita Joshi","Clothing","Ethnic Wear",5500,3,0.10,"Pune","West"),
    ("2024-07-08","Rahul Nair","Books","Machine Learning",950,2,0.0,"Chennai","South"),
    ("2024-07-12","Deepika Rao","Electronics","Smart Watch",8500,2,0.05,"Kolkata","East"),
    ("2024-08-01","Suresh Menon","Beauty","Makeup Kit",4500,2,0.0,"Kochi","South"),
    ("2024-08-05","Kavya Iyer","Electronics","Gaming Mouse",2200,3,0.05,"Hyderabad","South"),
]

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS orders")
    c.execute("""CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_date TEXT, customer TEXT, category TEXT,
        product TEXT, price REAL, quantity INTEGER,
        discount REAL, city TEXT, region TEXT,
        revenue REAL, profit REAL
    )""")
    for o in ORDERS:
        revenue = o[4] * o[5] * (1 - o[6])
        profit  = revenue * 0.25
        c.execute("INSERT INTO orders (order_date,customer,category,product,price,quantity,discount,city,region,revenue,profit) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                  (*o, round(revenue,2), round(profit,2)))
    conn.commit(); conn.close()
    print(f"✅ Database initialized with {len(ORDERS)} orders")

def query(sql):
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(sql).fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_kpis():
    r = query("SELECT COUNT(*) total_orders, ROUND(SUM(revenue),0) total_revenue, ROUND(SUM(profit),0) total_profit, ROUND(AVG(revenue),0) avg_order FROM orders")[0]
    r["profit_margin"] = round((r["total_profit"] / r["total_revenue"]) * 100, 1)
    return r

def get_monthly_revenue():
    return query("SELECT SUBSTR(order_date,1,7) month, ROUND(SUM(revenue),0) revenue, ROUND(SUM(profit),0) profit FROM orders GROUP BY month ORDER BY month")

def get_category_sales():
    return query("SELECT category, COUNT(*) orders, ROUND(SUM(revenue),0) revenue FROM orders GROUP BY category ORDER BY revenue DESC")

def get_top_products():
    return query("SELECT product, category, COUNT(*) sold, ROUND(SUM(revenue),0) revenue FROM orders GROUP BY product ORDER BY revenue DESC LIMIT 8")

def get_recent_orders():
    return query("SELECT order_date, customer, product, category, city, ROUND(revenue,0) revenue FROM orders ORDER BY order_date DESC LIMIT 10")

def get_region_sales():
    return query("SELECT region, COUNT(*) orders, ROUND(SUM(revenue),0) revenue FROM orders GROUP BY region ORDER BY revenue DESC")
