
SELECT
    dept_no,
    dept_name
FROM
    departments
ORDER BY
    dept_name ASC;


SELECT
    dept_no,
    dept_name
FROM
    departments
WHERE
    dept_no = 'd005';



    dept_no,
    dept_name
FROM
    departments
WHERE
    dept_name LIKE '%Manage%';


SELECT
    COUNT(*) AS total_departments
FROM
    departments;

