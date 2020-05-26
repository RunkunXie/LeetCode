##### \175. Combine Two Tables

SELECT p.firstname, p.lastname, a.city, a.state
    FROM person as p
    LEFT JOIN address as a ON p.personid = a.personid

;



##### \176. Second Highest Salary

SELECT
    (SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;



##### \177. Nth Highest Salary

