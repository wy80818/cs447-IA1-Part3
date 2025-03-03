from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = 'wy80818_school_db'

mysql = MySQL(app)

# Initialize the database
@app.route('/init_db', methods=['POST', 'GET'])
def init_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("DROP DATABASE IF EXISTS wy80818_school_db;")
        cur.execute("CREATE DATABASE wy80818_school_db;")
        cur.execute("USE wy80818_school_db;")
        
        cur.execute("""
        CREATE TABLE students (
            student_id INT PRIMARY KEY,
            name VARCHAR(100),
            credits INT
        );
        """)
        
        cur.execute("""
        CREATE TABLE instructors (
            instructor_id INT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        );
        """)
        
        cur.execute("""
        CREATE TABLE courses (
            course_id INT PRIMARY KEY,
            title VARCHAR(100),
            instructor_id INT,
            FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
        );
        """)
        
        cur.execute("""
        CREATE TABLE enrollment (
            enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT,
            course_id INT,
            enrollment_semester VARCHAR(100),
            enrollment_grade VARCHAR(1),
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            FOREIGN KEY (course_id) REFERENCES courses(course_id)
        );
        """)
        
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Database initialized successfully!"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add student
@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    student_id = data.get('student_id')
    name = data.get('name')
    credits = data.get('credits')
    
    if not student_id or not name or credits is None:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (student_id, name, credits) VALUES (%s, %s, %s)",
                    (student_id, name, credits))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Student added successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Update student
@app.route('/update_student', methods=['PUT'])
def update_student():
    data = request.get_json()
    student_id = data.get('student_id')
    name = data.get('name')
    credits = data.get('credits')
    
    if not student_id or not name or credits is None:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE students
            SET name = %s, credits = %s
            WHERE student_id = %s
        """, (name, credits, student_id))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Student updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Remove student
@app.route('/remove_student', methods=['DELETE'])
def remove_student():
    data = request.get_json()
    student_id = data.get('student_id')
    
    if not student_id:
        return jsonify({"error": "Missing student ID"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Student removed successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Add instructor
@app.route('/add_instructor', methods=['POST'])
def add_instructor():
    data = request.get_json()
    instructor_id = data.get('instructor_id')
    name = data.get('name')
    department = data.get('department')

    if not instructor_id or not name or not department:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO instructors (instructor_id, name, department) VALUES (%s, %s, %s)",
                    (instructor_id, name, department))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Instructor added successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Update instructor
@app.route('/update_instructor', methods=['PUT'])
def update_instructor():
    data = request.get_json()
    instructor_id = data.get('instructor_id')
    name = data.get('name')
    department = data.get('department')

    if not instructor_id or not name or not department:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE instructors
            SET name = %s, department = %s
            WHERE instructor_id = %s
        """, (name, department, instructor_id))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Instructor updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Remove instructor
@app.route('/remove_instructor', methods=['DELETE'])
def remove_instructor():
    data = request.get_json()
    instructor_id = data.get('instructor_id')
    
    if not instructor_id:
        return jsonify({"error": "Missing instructor ID"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM instructors WHERE instructor_id = %s", (instructor_id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Instructor removed successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Add course
@app.route('/add_course', methods=['POST'])
def add_course():
    data = request.get_json()
    course_id = data.get('course_id')
    title = data.get('title')
    instructor_id = data.get('instructor_id')

    if not course_id or not title or not instructor_id:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO courses (course_id, title, instructor_id) VALUES (%s, %s, %s)",
                    (course_id, title, instructor_id))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Course added successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Update course
@app.route('/update_course', methods=['PUT'])
def update_course():
    data = request.get_json()
    course_id = data.get('course_id')
    title = data.get('title')
    instructor_id = data.get('instructor_id')

    if not course_id or not title or not instructor_id:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE courses
            SET title = %s, instructor_id = %s
            WHERE course_id = %s
        """, (title, instructor_id, course_id))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Course updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Remove course
@app.route('/remove_course', methods=['DELETE'])
def remove_course():
    data = request.get_json()
    course_id = data.get('course_id')
    
    if not course_id:
        return jsonify({"error": "Missing course ID"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM courses WHERE course_id = %s", (course_id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Course removed successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Add enrollment
@app.route('/add_enrollment', methods=['POST'])
def add_enrollment():
    data = request.get_json()
    enrollment_id = data.get('enrollment_id')
    student_id = data.get('student_id')
    course_id = data.get('course_id')
    semester = data.get('semester')
    grade = data.get('grade')

    if not enrollment_id or not student_id or not course_id or not semester or not grade:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO enrollment (enrollment_id, student_id, course_id, enrollment_semester, enrollment_grade) VALUES (%s, %s, %s, %s, %s)",
                    (enrollment_id, student_id, course_id, semester, grade))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Enrollment added successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Update enrollment
@app.route('/update_enrollment', methods=['PUT'])
def update_enrollment():
    data = request.get_json()
    enrollment_id = data.get('enrollment_id')
    student_id = data.get('student_id')
    course_id = data.get('course_id')
    semester = data.get('semester')
    grade = data.get('grade')

    if not enrollment_id or not student_id or not course_id or not semester or not grade:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE enrollment
            SET student_id = %s, course_id = %s, enrollment_semester = %s, enrollment_grade = %s
            WHERE enrollment_id = %s
        """, (student_id, course_id, semester, grade, enrollment_id))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Enrollment updated successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Remove enrollment
@app.route('/remove_enrollment', methods=['DELETE'])
def remove_enrollment():
    data = request.get_json()
    enrollment_id = data.get('enrollment_id')
    
    if not enrollment_id:
        return jsonify({"error": "Missing enrollment ID"}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM enrollment WHERE enrollment_id = %s", (enrollment_id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({"message": "Enrollment removed successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Get students, instructors, courses, and enrollments (same as previously)
@app.route('/get_students', methods=['GET'])
def get_students():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students")
        students = cur.fetchall()
        cur.close()

        # Convert tuples to dictionaries for easier handling in React
        student_list = [{"student_id": row[0], "name": row[1], "credits": row[2]} for row in students]
        
        return jsonify(student_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_instructors', methods=['GET'])
def get_instructors():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM instructors")
        instructors = cur.fetchall()
        cur.close()

        # Convert tuples to dictionaries for easier handling in React
        instructor_list = [{"instructor_id": row[0], "name": row[1], "department": row[2]} for row in instructors]
        
        return jsonify(instructor_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_courses', methods=['GET'])
def get_courses():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM courses")
        courses = cur.fetchall()
        cur.close()

        # Convert tuples to dictionaries for easier handling in React
        course_list = [{"course_id": row[0], "title": row[1], "instructor_id": row[2]} for row in courses]
        
        return jsonify(course_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/get_enrollments', methods=['GET'])
def get_enrollments():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM enrollment")
        enrollments = cur.fetchall()
        cur.close()

        # Convert tuples to dictionaries for easier handling in React
        enrollment_list = [{"enrollment_id": row[0], "student_id": row[1], "course_id": row[2], 
                            "enrollment_semester": row[3], "enrollment_grade": row[4]} for row in enrollments]
        
        return jsonify(enrollment_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
