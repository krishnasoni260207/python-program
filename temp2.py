# -------------------- IMPORTS --------------------
import mysql.connector
import tkinter as kt
from tkinter import filedialog, messagebox, ttk
import csv as c


# -------------------- DATABASE CONNECTION --------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="inventory"
)

mycursor = mydb.cursor()


# -------------------- DATABASE FUNCTION --------------------
def store_data():

    # ---------- VALIDATION ----------
    if entry2.get() == "":
        messagebox.showerror("Error", "Product name required")
        return

    query = """
    INSERT INTO product
    (product_id, product_name, brand, catagory, p_rate, s_rate, status)
    VALUES (NULL, %s, %s, %s, %s, %s, 'Active')
    """

    values = (
        entry2.get(),
        entry3.get(),
        entry4.get(),
        entry5.get(),
        entry6.get(),
    )

    mycursor.execute(query, values)
    mydb.commit()

    # last inserted product id
    product_id = mycursor.lastrowid

    # ---------- INSERT STOCK ----------
    mycursor.execute(
        "INSERT INTO stock (product_id, quantity) VALUES (%s, %s)",
        (product_id, entry7.get() or 0)
    )
    mydb.commit()

    # ---------- SUCCESS MESSAGE ----------
    messagebox.showinfo(
        "Success",
        f"Product Stored Successfully\nGenerated Product ID: {product_id}"
    )

    # ---------- CLEAR INPUTS ----------
    entry2.delete(0, kt.END)
    entry3.set('')
    entry4.set('')
    entry5.delete(0, kt.END)
    entry6.delete(0, kt.END)
    entry7.delete(0, kt.END)

# -------------------- STATUS TOGGLE --------------------
def toggle_status_from_table(event, table):
    row_id = table.identify_row(event.y)
    col_id = table.identify_column(event.x)

    if col_id != "#7" or not row_id:
        return

    row = table.item(row_id)["values"]
    product_id = row[0]
    symbol = row[6]

    if symbol == "✔":
        new_symbol = "❌"
        new_status = "Deactive"
    else:
        new_symbol = "✔"
        new_status = "Active"

    mycursor.execute(
        "UPDATE product SET status=%s WHERE product_id=%s",
        (new_status, product_id)
    )
    mydb.commit()

    table.item(row_id, values=(
        row[0], row[1], row[2], row[3], row[4], row[5], new_symbol
    ))


# -------------------- MAIN WINDOW --------------------
window = kt.Tk()
window.geometry("480x600")
window.title("Inventory Manager")
window.config(bg="#f8f4f8")
window.resizable(True, True)


# -------------------- STYLES --------------------
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TCombobox", padding=5, font=("Segoe UI", 10))


# -------------------- HEADER --------------------
header = kt.Frame(window, bg="#1f2937", height=70)
header.pack(fill="x")

title = kt.Label(
    header,
    text="Inventory Management System",
    font=("Segoe UI", 18, "bold"),
    fg="white",
    bg="#1f2937"
)
title.pack(pady=18)


# -------------------- FORM CARD --------------------
card = kt.Frame(window, bg="white", bd=1, relief="solid")
card.pack(padx=20, pady=20, fill="both", expand=True)


def field_label(text):
    return kt.Label(
        card,
        text=text,
        bg="white",
        fg="#374151",
        font=("Segoe UI", 11, "bold")
    )


# -------------------- FORM FIELDS --------------------
field_label("Product Name").pack(anchor="w", padx=20, pady=(15, 2))
entry2 = kt.Entry(card, font=("Segoe UI", 11))
entry2.pack(fill="x", padx=20)

field_label("Brand").pack(anchor="w", padx=20, pady=(15, 2))
entry3 = ttk.Combobox(card, values=["hp", "oppo", "earthonic"], state="readonly")
entry3.pack(fill="x", padx=20)

field_label("Category").pack(anchor="w", padx=20, pady=(15, 2))
entry4 = ttk.Combobox(card, values=["mobile", "laptop", "TV"], state="readonly")
entry4.pack(fill="x", padx=20)

field_label("Purchase Rate").pack(anchor="w", padx=20, pady=(15, 2))
entry5 = kt.Entry(card, font=("Segoe UI", 11))
entry5.pack(fill="x", padx=20)

field_label("Selling Rate").pack(anchor="w", padx=20, pady=(15, 2))
entry6 = kt.Entry(card, font=("Segoe UI", 11))
entry6.pack(fill="x", padx=20)

field_label("QTY").pack(anchor="w", padx=20, pady=(15, 2))
entry7 = kt.Entry(card, font=("Segoe UI", 11))
entry7.pack(fill="x", padx=20)


# -------------------- BUTTON FRAME --------------------
btn_frame = kt.Frame(card, bg="white")
btn_frame.pack(pady=25)


# SAVE BUTTON
ttk.Button(btn_frame, text="Save Product", command=store_data)\
    .grid(row=0, column=0, padx=10)


# -------------------- PRODUCT TABLE --------------------
def view_table():
    win = kt.Toplevel(window)
    win.geometry("750x500")
    win.title("Product Table")

    table = ttk.Treeview(
        win,
        columns=("id","name","brand","cat","pr","sr","st"),
        show="headings"
    )

    heads = ["ID","Product","Brand","Category","P Rate","S Rate","Status"]

    for c,h in zip(table["columns"],heads):
        table.heading(c,text=h)
        table.column(c,width=100,anchor="center")

    table.pack(fill="both",expand=True)

    table.bind("<Button-1>", lambda e: toggle_status_from_table(e, table))

    mycursor.execute("SELECT * FROM product")

    for r in mycursor.fetchall():
        st = "✔" if r[6]=="Active" else "❌"
        table.insert("", "end", values=(r[0],r[1],r[2],r[3],r[4],r[5],st))


ttk.Button(btn_frame, text="View Product", command=view_table)\
    .grid(row=0, column=1, padx=10)





# -------------------- STOCK TABLE --------------------
def view_stock_table():
    win = kt.Toplevel(window)
    win.geometry("750x500")
    win.title("Stock Table")

    table = ttk.Treeview(
        win,
        columns=("pn","br","qty","pr","tot"),
        show="headings"
    )

    table.heading("pn", text="Product")
    table.heading("br", text="Brand")
    table.heading("qty", text="Quantity")
    table.heading("pr", text="Base Rate")
    table.heading("tot", text="Total Value")

    table.pack(fill="both", expand=True, padx=10, pady=10)

    query = """
    SELECT 
        product.product_name,
        product.brand,
        stock.quantity,
        product.p_rate,
        (stock.quantity * product.p_rate)
    FROM stock
    INNER JOIN product
    ON stock.product_id = product.product_id
    """

    mycursor.execute(query)

    for row in mycursor.fetchall():
        table.insert("", "end", values=row)

# STOCK TABLE BUTTON
ttk.Button(btn_frame, text="View Stock", command=view_stock_table)\
    .grid(row=0, column=2, padx=10)




# -------------------- CSV UPLOAD --------------------
def upload():
    file = filedialog.askopenfilename(
        title="Select CSV file",
        filetypes=[("CSV files","*.csv")]
    )
    if not file:
        return

    product_q = """
    INSERT INTO product
    (product_name, brand, catagory, p_rate, s_rate, status)
    VALUES (%s,%s,%s,%s,%s,'Active')
    """

    stock_q = "INSERT INTO stock (product_id, quantity) VALUES (%s,%s)"

    with open(file,'r') as f:
        reader = c.DictReader(f)

        for row in reader:
            vals = (row['product_name'],row['brand'],row['category'],row['prate'],row['srate'])
            mycursor.execute(product_q, vals)
            pid = mycursor.lastrowid
            mycursor.execute(stock_q,(pid,0))

    mydb.commit()
    messagebox.showinfo("Success","CSV Imported")


# CSV BUTTON
ttk.Button(window, text="Import CSV", command=upload)\
    .place(x=10, y=10)


window.mainloop()
