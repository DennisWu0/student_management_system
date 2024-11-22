from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="db",  # MySQL container hostname
        user="root",
        password="password",
        database="student_db"
    )

# Home Page: List all students
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=students)

# Add Student Page
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_student.html')

# Delete Student Page
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_student(id):
    if request.method == 'POST':
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('delete_student.html', student_id=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
