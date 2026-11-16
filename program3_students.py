from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)
def init_db():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER
        )
    """)

    conn.commit()
    conn.close()


# Add a new student
@app.route("/students", methods=["POST"])
def insert_student():
    data = request.get_json()

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, email, age) VALUES (?, ?, ?)",
        (
            data["name"],
            data["email"],
            data.get("age", 0)
        )
    )

    conn.commit()

    student_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "message": "student created",
        "id": student_id
    }), 201


# Get all students
@app.route("/students", methods=["GET"])
def get_students():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    students = [
        {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "age": row[3]
        }
        for row in rows
    ]

    return jsonify(students)


# Run the application
if __name__ == "__main__":
    init_db()
    app.run(debug=True)

