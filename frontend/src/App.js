import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [students, setStudents] = useState([]);
  const [instructors, setInstructors] = useState([]);
  const [courses, setCourses] = useState([]);
  const [enrollments, setEnrollments] = useState([]);

  const [studentId, setStudentId] = useState('');
  const [studentName, setStudentName] = useState('');
  const [studentCredits, setStudentCredits] = useState('');

  const [instructorId, setInstructorId] = useState('');
  const [instructorName, setInstructorName] = useState('');
  const [instructorDept, setInstructorDept] = useState('');

  const [courseId, setCourseId] = useState('');
  const [courseTitle, setCourseTitle] = useState('');
  const [courseInstructorId, setCourseInstructorId] = useState('');

  const [enrollmentId, setEnrollmentId] = useState('');
  const [enrollmentStudentId, setEnrollmentStudentId] = useState('');
  const [enrollmentCourseId, setEnrollmentCourseId] = useState('');
  const [enrollmentSemester, setEnrollmentSemester] = useState('');
  const [enrollmentGrade, setEnrollmentGrade] = useState('');

  const [dbMessage, setDbMessage] = useState('');

  useEffect(() => {
    fetchStudents();
    fetchInstructors();
    fetchCourses();
    fetchEnrollments();
  }, []);

  const fetchStudents = async () => {
    const response = await axios.get('http://localhost:5000/get_students');
    setStudents(response.data);
  };

  const fetchInstructors = async () => {
    const response = await axios.get('http://localhost:5000/get_instructors');
    setInstructors(response.data);
  };

  const fetchCourses = async () => {
    const response = await axios.get('http://localhost:5000/get_courses');
    setCourses(response.data);
  };

  const fetchEnrollments = async () => {
    const response = await axios.get('http://localhost:5000/get_enrollments');
    setEnrollments(response.data);
  };

  const addStudent = async () => {
    const studentData = { student_id: studentId, name: studentName, credits: studentCredits };
    await axios.post('http://localhost:5000/add_student', studentData);
    fetchStudents();
  };

  const updateStudent = async () => {
    const studentData = { student_id: studentId, name: studentName, credits: studentCredits };
    await axios.put('http://localhost:5000/update_student', studentData);
    fetchStudents();
  };

  const removeStudent = async () => {
    await axios.delete('http://localhost:5000/remove_student', { data: { student_id: studentId } });
    fetchStudents();
  };

  const addInstructor = async () => {
    const instructorData = { instructor_id: instructorId, name: instructorName, department: instructorDept };
    await axios.post('http://localhost:5000/add_instructor', instructorData);
    fetchInstructors();
  };

  const updateInstructor = async () => {
    const instructorData = { instructor_id: instructorId, name: instructorName, department: instructorDept };
    await axios.put('http://localhost:5000/update_instructor', instructorData);
    fetchInstructors();
  };

  const removeInstructor = async () => {
    await axios.delete('http://localhost:5000/remove_instructor', { data: { instructor_id: instructorId } });
    fetchInstructors();
  };

  const addCourse = async () => {
    const courseData = { course_id: courseId, title: courseTitle, instructor_id: courseInstructorId };
    await axios.post('http://localhost:5000/add_course', courseData);
    fetchCourses();
  };

  const updateCourse = async () => {
    const courseData = { course_id: courseId, title: courseTitle, instructor_id: courseInstructorId };
    await axios.put('http://localhost:5000/update_course', courseData);
    fetchCourses();
  };

  const removeCourse = async () => {
    await axios.delete('http://localhost:5000/remove_course', { data: { course_id: courseId } });
    fetchCourses();
  };

  const addEnrollment = async () => {
    const enrollmentData = { enrollment_id: enrollmentId, student_id: enrollmentStudentId, course_id: enrollmentCourseId, semester: enrollmentSemester, grade: enrollmentGrade };
    await axios.post('http://localhost:5000/add_enrollment', enrollmentData);
    fetchEnrollments();
  };

  const updateEnrollment = async () => {
    const enrollmentData = { enrollment_id: enrollmentId, student_id: enrollmentStudentId, course_id: enrollmentCourseId, semester: enrollmentSemester, grade: enrollmentGrade };
    await axios.put('http://localhost:5000/update_enrollment', enrollmentData);
    fetchEnrollments();
  };

  const removeEnrollment = async () => {
    await axios.delete('http://localhost:5000/remove_enrollment', { data: { enrollment_id: enrollmentId } });
    fetchEnrollments();
  };

  const initializeDatabase = async () => {
    try {
      const response = await axios.post('http://localhost:5000/init_db');
      window.location.reload();
      setDbMessage(response.data.message);
    } catch (error) {
      setDbMessage('Error initializing the database.');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>School Database Management</h1>

        {/* Initialize Database Button */}
        <button onClick={initializeDatabase}>Initialize/Reset Database</button>
        {dbMessage && <p>{dbMessage}</p>}

        {/* Students Section */}
        <h2>Students</h2>
        <div>
          <input
            type="text"
            placeholder="Student ID"
            value={studentId}
            onChange={(e) => setStudentId(e.target.value)}
          />
          <input
            type="text"
            placeholder="Name"
            value={studentName}
            onChange={(e) => setStudentName(e.target.value)}
          />
          <input
            type="number"
            placeholder="Credits"
            value={studentCredits}
            onChange={(e) => setStudentCredits(e.target.value)}
          />
          <button onClick={addStudent}>Add Student</button>
          <button onClick={updateStudent}>Update Student</button>
          <button onClick={removeStudent}>Remove Student</button>
        </div>

        <h3>Existing Students:</h3>
        <ul>
          {students.map((student) => (
            <li key={student.student_id}>
              {student.name} (ID: {student.student_id}, Credits: {student.credits})
            </li>
          ))}
        </ul>

        {/* Instructors Section */}
        <h2>Instructors</h2>
        <div>
          <input
            type="text"
            placeholder="Instructor ID"
            value={instructorId}
            onChange={(e) => setInstructorId(e.target.value)}
          />
          <input
            type="text"
            placeholder="Name"
            value={instructorName}
            onChange={(e) => setInstructorName(e.target.value)}
          />
          <input
            type="text"
            placeholder="Department"
            value={instructorDept}
            onChange={(e) => setInstructorDept(e.target.value)}
          />
          <button onClick={addInstructor}>Add Instructor</button>
          <button onClick={updateInstructor}>Update Instructor</button>
          <button onClick={removeInstructor}>Remove Instructor</button>
        </div>

        <h3>Existing Instructors:</h3>
        <ul>
          {instructors.map((instructor) => (
            <li key={instructor.instructor_id}>
              {instructor.name} (ID: {instructor.instructor_id}, Department: {instructor.department})
            </li>
          ))}
        </ul>

        {/* Courses Section */}
        <h2>Courses</h2>
        <div>
          <input
            type="text"
            placeholder="Course ID"
            value={courseId}
            onChange={(e) => setCourseId(e.target.value)}
          />
          <input
            type="text"
            placeholder="Title"
            value={courseTitle}
            onChange={(e) => setCourseTitle(e.target.value)}
          />
          <input
            type="text"
            placeholder="Instructor ID"
            value={courseInstructorId}
            onChange={(e) => setCourseInstructorId(e.target.value)}
          />
          <button onClick={addCourse}>Add Course</button>
          <button onClick={updateCourse}>Update Course</button>
          <button onClick={removeCourse}>Remove Course</button>
        </div>

        <h3>Existing Courses:</h3>
        <ul>
          {courses.map((course) => (
            <li key={course.course_id}>
              {course.title} (ID: {course.course_id}, Instructor ID: {course.instructor_id})
            </li>
          ))}
        </ul>

        {/* Enrollments Section */}
        <h2>Enrollments</h2>
        <div>
          <input
            type="text"
            placeholder="Enrollment ID"
            value={enrollmentId}
            onChange={(e) => setEnrollmentId(e.target.value)}
          />
          <input
            type="text"
            placeholder="Student ID"
            value={enrollmentStudentId}
            onChange={(e) => setEnrollmentStudentId(e.target.value)}
          />
          <input
            type="text"
            placeholder="Course ID"
            value={enrollmentCourseId}
            onChange={(e) => setEnrollmentCourseId(e.target.value)}
          />
          <input
            type="text"
            placeholder="Semester"
            value={enrollmentSemester}
            onChange={(e) => setEnrollmentSemester(e.target.value)}
          />
          <input
            type="text"
            placeholder="Grade"
            value={enrollmentGrade}
            onChange={(e) => setEnrollmentGrade(e.target.value)}
          />
          <button onClick={addEnrollment}>Add Enrollment</button>
          <button onClick={updateEnrollment}>Update Enrollment</button>
          <button onClick={removeEnrollment}>Remove Enrollment</button>
        </div>

        <h3>Existing Enrollments:</h3>
        <ul>
          {enrollments.map((enrollment) => (
            <li key={enrollment.enrollment_id}>
              Student ID: {enrollment.student_id}, Course ID: {enrollment.course_id}, 
              Semester: {enrollment.enrollment_semester}, Grade: {enrollment.enrollment_grade}
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;
