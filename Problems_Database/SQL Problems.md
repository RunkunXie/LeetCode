##### \175. Combine Two Tables

```mysql
# Write your MySQL query statement below

SELECT p.firstname, p.lastname, a.city, a.state
    FROM person as p
    LEFT JOIN address as a ON p.personid = a.personid

;
```



##### \176. Second Highest Salary

```mysql
# Write your MySQL query statement below

SELECT
    (SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```

```mysql
# Write your MySQL query statement below

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
# Write your MySQL query statement below

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



##### \181. Employees Earning More Than Their Managers

```mysql
# Write your MySQL query statement below

SELECT E1.Name as Employee
    FROM Employee as E1
    JOIN Employee as E2 ON E1.ManagerId = E2.Id
    WHERE E1.Salary > E2.Salary
;
```



##### \1179. Reformat Department Table

```mysql
# Write your MySQL query statement below
# my JOIN sol

SELECT DISTINCT
    D.id, 
    D1.revenue as Jan_Revenue,
    D2.revenue as Feb_Revenue,
    D3.revenue as Mar_Revenue,
    D4.revenue as Apr_Revenue,
    D5.revenue as May_Revenue,
    D6.revenue as Jun_Revenue,
    D7.revenue as Jul_Revenue,
    D8.revenue as Aug_Revenue,
    D9.revenue as Sep_Revenue,
    D10.revenue as Oct_Revenue,
    D11.revenue as Nov_Revenue,
    D12.revenue as Dec_Revenue

FROM Department as D
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Jan') as D1 ON D.id = D1.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Feb') as D2 ON D.id = D2.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Mar') as D3 ON D.id = D3.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Apr') as D4 ON D.id = D4.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'May') as D5 ON D.id = D5.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Jun') as D6 ON D.id = D6.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Jul') as D7 ON D.id = D7.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Aug') as D8 ON D.id = D8.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Sep') as D9 ON D.id = D9.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Oct') as D10 ON D.id = D10.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Nov') as D11 ON D.id = D11.id
    LEFT JOIN (SELECT DISTINCT id, revenue FROM Department WHERE month = 'Dec') as D12 ON D.id = D12.id
```

```mysql
# Write your MySQL query statement below
# online GROUP BY sol

SELECT DISTINCT 
    id, 
    MAX(CASE WHEN month = 'Jan' THEN revenue ELSE null END) AS Jan_Revenue,
    MAX(CASE WHEN month = 'Feb' THEN revenue ELSE null END) AS Feb_Revenue,
    MAX(CASE WHEN month = 'Mar' THEN revenue ELSE null END) AS Mar_Revenue,
    MAX(CASE WHEN month = 'Apr' THEN revenue ELSE null END) AS Apr_Revenue,
    MAX(CASE WHEN month = 'May' THEN revenue ELSE null END) AS May_Revenue,
    MAX(CASE WHEN month = 'Jun' THEN revenue ELSE null END) AS Jun_Revenue,
    MAX(CASE WHEN month = 'Jul' THEN revenue ELSE null END) AS Jul_Revenue,
    MAX(CASE WHEN month = 'Aug' THEN revenue ELSE null END) AS Aug_Revenue,
    MAX(CASE WHEN month = 'Sep' THEN revenue ELSE null END) AS Sep_Revenue,
    MAX(CASE WHEN month = 'Oct' THEN revenue ELSE null END) AS Oct_Revenue,
    MAX(CASE WHEN month = 'Nov' THEN revenue ELSE null END) AS Nov_Revenue,
    MAX(CASE WHEN month = 'Dec' THEN revenue ELSE null END) AS Dec_Revenue
FROM Department
GROUP BY id
```



