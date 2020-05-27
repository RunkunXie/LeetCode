##### \175. Combine Two Tables

```mysql
SELECT p.firstname, p.lastname, a.city, a.state
    FROM person as p
    LEFT JOIN address as a ON p.personid = a.personid

;
```



##### \176. Second Highest Salary

```mysql
SELECT
    (SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```

```mysql
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
```



##### \177. Nth Highest Salary

```mysql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N - 1;
    RETURN (
        SELECT DISTINCT Salary
            FROM Employee
            ORDER BY Salary DESC
            LIMIT 1 OFFSET M
    );
END
```





