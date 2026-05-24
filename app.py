from flask import Flask, render_template, jsonify
from database import init_db, get_kpis, get_monthly_revenue, get_category_sales, get_top_products, get_recent_orders, get_region_sales

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html", kpis=get_kpis())

@app.route("/api/monthly-revenue")
def monthly_revenue(): return jsonify(get_monthly_revenue())

@app.route("/api/category-sales")
def category_sales(): return jsonify(get_category_sales())

@app.route("/api/top-products")
def top_products(): return jsonify(get_top_products())

@app.route("/api/recent-orders")
def recent_orders(): return jsonify(get_recent_orders())

@app.route("/api/region-sales")
def region_sales(): return jsonify(get_region_sales())

@app.route("/api/kpis")
def kpis(): return jsonify(get_kpis())

if __name__ == "__main__":
    init_db()
    print("\n✅ Database ready!")
    print("🚀 Open http://localhost:5000 in your browser")
    print("   Press Ctrl+C to stop\n")
    app.run(debug=True, host="0.0.0.0", port=5000)
