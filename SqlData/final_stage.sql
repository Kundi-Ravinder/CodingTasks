SELECT email, course_level
from Student INNER JOIN Course on Student.stu_subject_code = Course.course_code 
WHERE course_level = 3;