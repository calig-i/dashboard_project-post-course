# Cashboard Project

# re-create databases for bank accounts - DONE
# import update bank balance function - DONE

#---------TKinter------------------

# import modules
from tkinter import *
import sqlite3

# root widget
root = Tk()

root.title("Cashboard")
 
#---------------Display Balance Function---------------
def db_bal():
  def nwc():
    import sqlite3
    conn = sqlite3.connect('bank_accs.db')
    c = conn.cursor()
    c.execute("SELECT amount FROM bank_accs WHERE rowid=1")
    amounts = c.fetchall()
    return(amounts)

  nwcLabel = Label(root, text=nwc())
  nwcLabel.grid(row=3, column=2)

  def nwb():
    import sqlite3
    conn = sqlite3.connect('bank_accs.db')
    c = conn.cursor()
    c.execute("SELECT amount FROM bank_accs WHERE rowid=2")
    amounts = c.fetchall()
    return(amounts)

  nwbLabel = Label(root, text=nwb())
  nwbLabel.grid(row=4, column=2)

  def nws1():
    import sqlite3
    conn = sqlite3.connect('bank_accs.db')
    c = conn.cursor()
    c.execute("SELECT amount FROM bank_accs WHERE rowid=3")
    amounts = c.fetchall()
    return(amounts)

  nws1Label = Label(root, text=nws1())
  nws1Label.grid(row=5, column=2)

  def nws2():
    import sqlite3
    conn = sqlite3.connect('bank_accs.db')
    c = conn.cursor()
    c.execute("SELECT amount FROM bank_accs WHERE rowid=4")
    amounts = c.fetchall()
    return(amounts)

  nws2Label = Label(root, text=nws2())
  nws2Label.grid(row=6, column=2)

  def coopc1():
    import sqlite3
    conn = sqlite3.connect('bank_accs.db')
    c = conn.cursor()
    c.execute("SELECT amount FROM bank_accs WHERE rowid=5")
    amounts = c.fetchall()
    return(amounts)

  coopc1Label = Label(root, text=coopc1())
  coopc1Label.grid(row=7, column=2)

  def coopc2():
    import sqlite3
    conn = sqlite3.connect('bank_accs.db')
    c = conn.cursor()
    c.execute("SELECT amount FROM bank_accs WHERE rowid=6")
    amounts = c.fetchall()
    return(amounts)

  coopc2Label = Label(root, text=coopc2())
  coopc2Label.grid(row=8, column=2)

  def coopsv():
    import sqlite3
    conn = sqlite3.connect('bank_accs.db')
    c = conn.cursor()
    c.execute("SELECT amount FROM bank_accs WHERE rowid=7")
    amounts = c.fetchall()
    return(amounts)

  coopsvLabel = Label(root, text=coopsv())
  coopsvLabel.grid(row=9, column=2)

db_bal()

#-----------Update Database Function---------

def update_ba():
  # import modules
  import sqlite3
 
  # update database
  conn = sqlite3.connect("bank_accs.db")
  c = conn.cursor() 

  sql = "UPDATE bank_accs SET amount = ? WHERE rowid = 1" 
  c.execute(sql, (nw_curr.get(),))
  sql = "UPDATE bank_accs SET amount = ? WHERE rowid = 2"
  c.execute(sql, (nw_bills.get(),))
  sql = "UPDATE bank_accs SET amount = ? WHERE rowid = 3"
  c.execute(sql, (nw_sav1.get(),))
  sql = "UPDATE bank_accs SET amount = ? WHERE rowid = 4"
  c.execute(sql, (nw_sav2.get(),))
  sql = "UPDATE bank_accs SET amount = ? WHERE rowid = 5"
  c.execute(sql, (coop_c1.get(),))
  sql = "UPDATE bank_accs SET amount = ? WHERE rowid = 6"
  c.execute(sql, (coop_c2.get(),))
  sql = "UPDATE bank_accs SET amount = ? WHERE rowid = 7"
  c.execute(sql, (coop_sav.get(),))
  
  # query database, outputs to console to test
  c.execute("SELECT rowid, * FROM bank_accs")
  items = c.fetchall()
  for item in items:
    print(item)
  # commit and close
  conn.commit()
  conn.close()
 
# ---------------Function Name---------------

myLabeltitle = Label(root, text="Current Bank Balances")
myLabeltitle.grid(row=0, column=0, columnspan=2)

#---------------Column Headings---------------- 

myLabelb_acc = Label(root, text="Bank Account")
myLabelb_acc.grid(row=2, column=0)

myLabelin_bal = Label(root, text="Input Balance")
myLabelin_bal.grid(row=2, column=1)

myLabeldb_bal = Label(root, text="Database Balance")
myLabeldb_bal.grid(row=2, column=2)

#--------------Bank account names----------------

myLabelnw_curr = Label(root, text="Natwest Current a/c: ")
myLabelnw_curr.grid(row=3, column=0)

myLabelnw_bill = Label(root, text="Natwest Bills a/c: ")
myLabelnw_bill.grid(row=4, column=0)

myLabelnw_sav1 = Label(root, text="Natwest Savings 1 a/c: ")
myLabelnw_sav1.grid(row=5, column=0)

myLabelnw_sav2 = Label(root, text="Natwest Savings 2 a/c: ")
myLabelnw_sav2.grid(row=6, column=0)

myLabelcoop_c1 = Label(root, text="Co-op Current 1 a/c: ")
myLabelcoop_c1.grid(row=7, column=0)

myLabelcoop_c2 = Label(root, text="Co-op Current 2 a/c: ")
myLabelcoop_c2.grid(row=8, column=0)

myLabelcoop_sav = Label(root, text="Co-op Savings a/c: ")
myLabelcoop_sav.grid(row=9, column=0)

# -----------input fields---------------

# check erroneous input

# create entry (input) field
nw_curr = Entry(root, width=10, borderwidth=2)
# position field
nw_curr.grid(row=3, column=1, padx=10, pady=10)
# default field text 
nw_curr.insert(0, "£")

nw_bills = Entry(root, width=10, borderwidth=2)
nw_bills.grid(row=4, column=1, padx=10, pady=10)
nw_bills.insert(0, "£")

nw_sav1 = Entry(root, width=10, borderwidth=2)
nw_sav1.grid(row=5, column=1, padx=10, pady=10)
nw_sav1.insert(0, "£")

nw_sav2 = Entry(root, width=10, borderwidth=2)
nw_sav2.grid(row=6, column=1, padx=10, pady=10)
nw_sav2.insert(0, "£")

coop_c1 = Entry(root, width=10, borderwidth=2)
coop_c1.grid(row=7, column=1, padx=10, pady=10)
coop_c1.insert(0, "£")

coop_c2 = Entry(root, width=10, borderwidth=2)
coop_c2.grid(row=8, column=1, padx=10, pady=10)
coop_c2.insert(0, "£")

coop_sav = Entry(root, width=10, borderwidth=2)
coop_sav.grid(row=9, column=1, padx=10, pady=10)
coop_sav.insert(0, "£")

#---------------Update Button--------------

# command=lambda runs both update balance and show balance functions

updateButton = Button(root, text="Update Bank Balances", command=lambda:[update_ba(), db_bal()])

updateButton.grid(row=0, column=2, pady=20, padx=20)

root.mainloop()

"""
problems to write about:

adapting update_ba to accept field input
getting database to update labels
tring to call db_bal within update_ba
spelling lambda wrong! (lamda)

to do:

catch erroneous input - gave try and except a go, not sure how to make it work as a function
cast to float
format to 2 decimal places 

https://stackabuse.com/format-number-as-currency-string-in-python/

ignore no input, keep existing database amount


"""

