### Some queries just for testing purpose.

1.  Natural Language: "Retrieve all data from the employees table."
    Expected SQL Query: SELECT * FROM employees;

2.  Natural Language: "Find all employees whose salary is greater than 6000."
    Expected SQL Query: SELECT * FROM employees WHERE salary > 6000;

3.  JOIN Tables:
    Natural Language: "Show employee names and their department names."
    Expected SQL Query:
                        SELECT employees.name, departments.name 
                        FROM employees 
                        JOIN departments ON employees.department_id = departments.id;

4.  Aggregating with COUNT
    Natural Language: "How many employees are in the sales department?"
    Expected SQL Query:
                        SELECT COUNT(*) 
                        FROM employees 
                        WHERE department = 'sales';

5.  Sorting Data
    Natural Language: "List all employees ordered by their hire date."
    Expected SQL Query:
                        SELECT * 
                        FROM employees 
                        ORDER BY hire_date;

6.  Using GROUP BY
    Natural Language: "Find the total salary for each department."
    Expected SQL Query:
                        SELECT department, SUM(salary) 
                        FROM employees 
                        GROUP BY department;

7.  LIMIT Query
    Natural Language: "Retrieve the top 10 highest paid employees."
    Expected SQL Query:
                        SELECT * 
                        FROM employees 
                        ORDER BY salary DESC 
                        LIMIT 10;
                        UPDATE Query

8.  Natural Language: "Update the salary of employees in the HR department by 5%."
    Expected SQL Query:
                        UPDATE employees 
                        SET salary = salary * 1.05 
                        WHERE department = 'HR';
                        DELETE Query


9.  Natural Language: "Delete employees who haven't been promoted in the last 5 years."
    Expected SQL Query:
                        DELETE FROM employees 
                        WHERE last_promotion_date < DATE_SUB(CURRENT_DATE, INTERVAL 5 YEAR);
                        HAVING Clause


10. Natural Language: "Find departments where the average salary is more than 5000."
    Expected SQL Query:
                        SELECT department, AVG(salary) 
                        FROM employees 
                        GROUP BY department 
                        HAVING AVG(salary) > 5000;
