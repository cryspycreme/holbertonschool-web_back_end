export default function updateStudentGradeByCity(students, city, newGrades) {
  return (
    students
      // filter students by city
      .filter((student) => student.location === city)
      // find matching student in newGrades
      .map((student) => {
        const gradeObj = newGrades.find(
          (grade) => grade.studentId === student.id
        );
        return {
          ...student,
          grade: gradeObj ? gradeObj.grade : 'N/A',
        };
      })
  );
}
