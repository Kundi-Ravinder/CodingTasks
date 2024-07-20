SELECT first_name ,course_name,teacher_name
from Student LEFT OUTER JOIN Course
WHERE mark >= 70;