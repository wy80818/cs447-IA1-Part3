DROP DATABASE wy80818_school_db;
CREATE DATABASE wy80818_school_db;
USE wy80818_school_db;
CREATE TABLE students (student_id INT PRIMARY KEY, name VARCHAR(100),credits INT);
CREATE TABLE instructors (instructor_id INT PRIMARY KEY,name VARCHAR(100),department VARCHAR(100));
CREATE TABLE courses (course_id INT PRIMARY KEY,title VARCHAR(100),instructor_id INT,FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id));
CREATE TABLE enrollment (enrollment_id INT AUTO_INCREMENT PRIMARY KEY,student_id INT,course_id INT,enrollment_semester VARCHAR(100),enrollment_grade VARCHAR(1),FOREIGN KEY (student_id) REFERENCES students(student_id),FOREIGN KEY (course_id) REFERENCES courses(course_id));
