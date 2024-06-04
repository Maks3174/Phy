import tkinter as tk
from tkinter import messagebox, simpledialog
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from sqlalchemy import create_engine
from models import Sale, Salesman, Customer, DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def view_all_sales():
    sales = session.query(Sale).all()
    result = [(sale.SaleID, sale.SalesmanID, sale.CustomerID, sale.Amount, sale.SaleDate) for sale in sales]
    messagebox.showinfo("All Sales", result)

def view_sales_by_salesman():
    salesman_id = simpledialog.askinteger("Input", "Enter Salesman ID:")
    sales = session.query(Sale).filter(Sale.SalesmanID == salesman_id).all()
    result = [(sale.SaleID, sale.SalesmanID, sale.CustomerID, sale.Amount, sale.SaleDate) for sale in sales]
    messagebox.showinfo("Sales by Salesman", result)

def view_max_sale():
    sale = session.query(Sale).order_by(Sale.Amount.desc()).first()
    result = (sale.SaleID, sale.SalesmanID, sale.CustomerID, sale.Amount, sale.SaleDate)
    messagebox.showinfo("Max Sale", result)

def view_min_sale():
    sale = session.query(Sale).order_by(Sale.Amount.asc()).first()
    result = (sale.SaleID, sale.SalesmanID, sale.CustomerID, sale.Amount, sale.SaleDate)
    messagebox.showinfo("Min Sale", result)

def view_max_sale_by_salesman():
    salesman_id = simpledialog.askinteger("Input", "Enter Salesman ID:")
    sale = session.query(Sale).filter(Sale.SalesmanID == salesman_id).order_by(Sale.Amount.desc()).first()
    result = (sale.SaleID, sale.SalesmanID, sale.CustomerID, sale.Amount, sale.SaleDate)
    messagebox.showinfo("Max Sale by Salesman", result)

def view_min_sale_by_salesman():
    salesman_id = simpledialog.askinteger("Input", "Enter Salesman ID:")
    sale = session.query(Sale).filter(Sale.SalesmanID == salesman_id).order_by(Sale.Amount.asc()).first()
    result = (sale.SaleID, sale.SalesmanID, sale.CustomerID, sale.Amount, sale.SaleDate)
    messagebox.showinfo("Min Sale by Salesman", result)

def view_max_sale_by_customer():
    customer_id = simpledialog.askinteger("Input", "Enter Customer ID:")
    sale = session.query(Sale).filter(Sale.CustomerID == customer_id).order_by(Sale.Amount.desc()).first()
    result = (sale.SaleID, sale.SalesmanID, sale.CustomerID, sale.Amount, sale.SaleDate)
    messagebox.showinfo("Max Sale by Customer", result)

def view_min_sale_by_customer():
    customer_id = simpledialog.askinteger("Input", "Enter Customer ID:")
    sale = session.query(Sale).filter(Sale.CustomerID == customer_id).order_by(Sale.Amount.asc()).first()
    result = (sale.SaleID, sale.SalesmanID, sale.CustomerID, sale.Amount, sale.SaleDate)
    messagebox.showinfo("Min Sale by Customer", result)

def view_salesman_with_max_sales():
    result = session.query(Sale.SalesmanID, func.sum(Sale.Amount).label('TotalSales')).group_by(Sale.SalesmanID).order_by(func.sum(Sale.Amount).desc()).first()
    messagebox.showinfo("Salesman with Max Sales", result)

def view_salesman_with_min_sales():
    result = session.query(Sale.SalesmanID, func.sum(Sale.Amount).label('TotalSales')).group_by(Sale.SalesmanID).order_by(func.sum(Sale.Amount).asc()).first()
    messagebox.showinfo("Salesman with Min Sales", result)

def view_customer_with_max_purchases():
    result = session.query(Sale.CustomerID, func.sum(Sale.Amount).label('TotalPurchases')).group_by(Sale.CustomerID).order_by(func.sum(Sale.Amount).desc()).first()
    messagebox.showinfo("Customer with Max Purchases", result)

def view_avg_purchase_by_customer():
    customer_id = simpledialog.askinteger("Input", "Enter Customer ID:")
    result = session.query(func.avg(Sale.Amount)).filter(Sale.CustomerID == customer_id).first()
    messagebox.showinfo("Average Purchase by Customer", result)

def view_avg_purchase_by_salesman():
    salesman_id = simpledialog.askinteger("Input", "Enter Salesman ID:")
    result = session.query(func.avg(Sale.Amount)).filter(Sale.SalesmanID == salesman_id).first()
    messagebox.showinfo("Average Purchase by Salesman", result)

root = tk.Tk()
root.title("Sales Database Reports")

menubar = tk.Menu(root)
root.config(menu=menubar)

report_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Reports", menu=report_menu)

report_menu.add_command(label="View All Sales", command=view_all_sales)
report_menu.add_command(label="View Sales by Salesman", command=view_sales_by_salesman)
report_menu.add_command(label="View Max Sale", command=view_max_sale)
report_menu.add_command(label="View Min Sale", command=view_min_sale)
report_menu.add_command(label="View Max Sale by Salesman", command=view_max_sale_by_salesman)
report_menu.add_command(label="View Min Sale by Salesman", command=view_min_sale_by_salesman)
report_menu.add_command(label="View Max Sale by Customer", command=view_max_sale_by_customer)
report_menu.add_command(label="View Min Sale by Customer", command=view_min_sale_by_customer)
report_menu.add_command(label="Salesman with Max Sales", command=view_salesman_with_max_sales)
report_menu.add_command(label="Salesman with Min Sales", command=view_salesman
