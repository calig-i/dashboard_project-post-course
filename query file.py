"""

from tkinter import *
import sqlite3

# root widget
root = Tk()

import sqlite3

conn = sqlite3.connect("test.db")

c = conn.cursor()

c.execute("""CREATE TABLE test (
         account_name text,
         amount real 
    )""")

rows = [
  ['Natwest Current a/c', '0.00'],
  ['Natwest Bills a/c', '0.00'],
  ['Natwest Savings 1 a/c', '0.00'],
  ['Natwest Savings 2 a/c', '0.00'],
  ['Co op Current 1 a/c', '0.00'],
  ['Co op Current 2 a/c', '0.00'],
  ['Co op Savings a/c', '0.00']
]

c.executemany("INSERT INTO test VALUES(?,?)", rows)

c.execute("SELECT rowid, *  FROM test")

items = c.fetchall()
for item in items:
  print(item)

conn.commit()

conn.close()

"""
# db balance label function

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

# call db balance label function
db_bal()

# update bank balance function

def update_ba():
  # import modules
  import sqlite3
 
  # update database
  conn = sqlite3.connect("bank_accs.db")
  c = conn.cursor() 

  sql = "UPDATE bank_accs SET amount = ? WHERE rowid = 1" 
  c.execute(sql, (nw_curr.get(),))

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

# -----------input fields---------------

# create entry (input) field
nw_curr = Entry(root, width=10, borderwidth=2)
# position field
nw_curr.grid(row=3, column=1, padx=10, pady=10)
# default field text 
nw_curr.insert(0, "£")

#---------------Update Button--------------

updateButton = Button(root, text="Update Bank Balances", command=update_ba)

updateButton.grid(row=0, column=2, pady=20, padx=20)

#---------------------------------------------

root.mainloop()

"""