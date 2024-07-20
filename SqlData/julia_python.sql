SELECT first_name, last_name,teacher_name 
FROM Student LEFT OUTER JOIN Course 
where teacher_name = 'Julia Python';