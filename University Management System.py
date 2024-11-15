import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",
    user="root",      # Your MySQL username
    password="piyush",  # Your MySQL password
    database="university"   # The name of your database
)

cursor = conn.cursor()

# Function to add a new student
def add_student():
    student_id = entry_student_id.get()
    name = entry_name.get()
    enrollment = entry_enrollment.get()
    course = entry_course.get()
    fee = entry_fee.get()
    contact = entry_contact.get()
    email = entry_email.get()
    address = entry_address.get()

    if student_id and name and enrollment:
        try:
            cursor.execute("INSERT INTO students (student_id, name, enrollment, course, fee, contact, email, address) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                           (student_id, name, enrollment, course, fee, contact, email, address))
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error adding student: {err}")
    else:
        messagebox.showerror("Error", "Please fill out all required fields")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    listbox.delete(0, tk.END)  # Clear the listbox
    for record in records:
        listbox.insert(tk.END, record)

# Function to delete a student by ID
def delete_student():
    student_id = entry_student_id.get()
    if student_id:
        cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()
        messagebox.showinfo("Success", "Student deleted successfully!")
    else:
        messagebox.showerror("Error", "Please enter a Student ID")

# Function to update student details
def update_student():
    student_id = entry_student_id.get()
    name = entry_name.get()
    enrollment = entry_enrollment.get()
    course = entry_course.get()
    fee = entry_fee.get()
    contact = entry_contact.get()
    email = entry_email.get()
    address = entry_address.get()

    if student_id:
        cursor.execute("""
            UPDATE students 
            SET name=%s, enrollment=%s, course=%s, fee=%s, contact=%s, email=%s, address=%s
            WHERE student_id=%s""",
            (name, enrollment, course, fee, contact, email, address, student_id))
        conn.commit()
        messagebox.showinfo("Success", "Student details updated successfully!")
    else:
        messagebox.showerror("Error", "Please enter a Student ID")

# GUI Setup
root = tk.Tk()
root.title("University Management System")

# Labels and entry fields for student information
tk.Label(root, text="Student ID").grid(row=0, column=0)
entry_student_id = tk.Entry(root)
entry_student_id.grid(row=0, column=1)

tk.Label(root, text="Name").grid(row=1, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=1, column=1)

tk.Label(root, text="Enrollment").grid(row=2, column=0)
entry_enrollment = tk.Entry(root)
entry_enrollment.grid(row=2, column=1)

tk.Label(root, text="Course").grid(row=3, column=0)
entry_course = tk.Entry(root)
entry_course.grid(row=3, column=1)

tk.Label(root, text="Fee").grid(row=4, column=0)
entry_fee = tk.Entry(root)
entry_fee.grid(row=4, column=1)

tk.Label(root, text="Contact").grid(row=5, column=0)
entry_contact = tk.Entry(root)
entry_contact.grid(row=5, column=1)

tk.Label(root, text="Email").grid(row=6, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=6, column=1)

tk.Label(root, text="Address").grid(row=7, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=7, column=1)

# Listbox to display students
listbox = tk.Listbox(root, height=10, width=100)
listbox.grid(row=8, column=0, columnspan=2)

# Buttons for actions
tk.Button(root, text="Add Student", command=add_student).grid(row=9, column=0)
tk.Button(root, text="View Students", command=view_students).grid(row=9, column=1)
tk.Button(root, text="Delete Student", command=delete_student).grid(row=10, column=0)
tk.Button(root, text="Update Student", command=update_student).grid(row=10, column=1)

root.mainloop()

# Close the database connection when done
conn.close()
