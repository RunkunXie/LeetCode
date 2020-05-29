#### Progress

##### By Difficulty

Easy: 176, 175, 181, 1179 | 183, 196, 182, 1241 | 197, 603, 597, 1142

Mid: 177 | 178



##### \175. Combine Two Tables

```mysql
# my sol

SELECT p.firstname, p.lastname, a.city, a.state
    FROM person as p
    LEFT JOIN address as a ON p.personid = a.personid
;
```



##### \176. Second Highest Salary

```mysql
# ans Subselect

SELECT
    (SELECT DISTINCT Salary
        FROM Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```

```mysql
# ans IFNULL

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
# online sol

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



##### \178. Rank Scores

```mysql
# online sol

SELECT S1.Score, COUNT(S2.Score) AS "Rank"
    FROM 
        Scores AS S1,
        (SELECT DISTINCT Score FROM Scores) AS S2
    WHERE S1.Score <= S2.Score
    GROUP BY S1.Id 
    ORDER BY S1.Score DESC
```

```mysql
# online sol w. variable

SELECT
    Score,
    @rank := @rank + (@prev <> (@prev := Score)) "Rank"
FROM
    Scores,
    (SELECT @rank := 0, @prev := -1) init
ORDER BY Score DESC
```



##### \180. Consecutive Numbers

```mysql
# MY JOIN SOL

SELECT DISTINCT L1.NUM AS ConsecutiveNums
    FROM LOGS AS L1
    JOIN LOGS AS L2 ON L1.ID = L2.ID + 1
    JOIN LOGS AS L3 ON L1.ID = L3.ID - 1
    WHERE L1.NUM = L2.NUM AND L2.NUM = L3.NUM 
```



##### \181. Employees Earning More Than Their Managers

```mysql
# my sol

SELECT E1.Name as Employee
    FROM Employee as E1
    JOIN Employee as E2 ON E1.ManagerId = E2.Id
    WHERE E1.Salary > E2.Salary
;
```



##### \182. Duplicate Emails

```mysql
# my sol

SELECT DISTINCT p1.Email
    FROM Person as P1, Person as P2
    WHERE P1.Email = P2.Email and P1.ID != P2.ID
```

```mysql
# GROUP BY, HAVING sol

select Email
from Person
group by Email
having count(Email) > 1;
```



##### \183. Customers Who Never Order

```mysql
# my JOIN sol

SELECT Name as Customers
    FROM Customers as C
    LEFT JOIN Orders as O ON C.Id = O.CustomerId
    WHERE ISNULL(O.Id)
```

```mysql
# ans, subselect

select customers.name as 'Customers'
from customers
where customers.id not in (
    select customerid from orders
);
```



##### \196. Delete Duplicate Emails

```mysql
# ans

DELETE p1 FROM Person p1, Person p2
    WHERE p1.Email = p2.Email AND p1.Id > p2.Id
```



##### \197. Rising Temperature

```mysql
# my sol under online hint, 436ms

SELECT W1.ID 
FROM WEATHER AS W1, WEATHER AS W2 
WHERE W2.RecordDate = ADDDATE(W1.RecordDate, INTERVAL -1 DAY) AND W1.Temperature > W2.temperature
```

```mysql
# ans, 888ms

SELECT W1.ID
    FROM WEATHER AS W1
    JOIN WEATHER AS W2 
        ON W2.RecordDate = ADDDATE(W1.RecordDate, INTERVAL -1 DAY) 
            AND W1.Temperature > W2.temperature
```



##### \597. Friend Requests I: Overall Acceptance Rate

```mysql
# my CASE sol

SELECT (
    CASE
        WHEN COUNT(R.sender_id) = 0 THEN 0
        ELSE
            ROUND(COUNT(DISTINCT A.requester_id, A.accepter_id) / 
                 COUNT(DISTINCT R.sender_id, R.send_to_id), 2) 
    END) AS accept_rate
    FROM request_accepted AS A, friend_request AS R
```

```mysql
# answer, IFNULL

SELECT (
    IFNULL(ROUND(COUNT(DISTINCT A.requester_id, A.accepter_id) / 
                 COUNT(DISTINCT R.sender_id, R.send_to_id), 2), 0)) AS accept_rate
    FROM request_accepted AS A, friend_request AS R
```



##### \603. Consecutive Available Seats

```mysql
# my sol

SELECT C1.SEAT_ID, C2.SEAT_ID, C3.SEAT_ID
    FROM CINEMA AS C1
    LEFT JOIN CINEMA AS C2 ON C2.SEAT_ID - 1 = C1.SEAT_ID
    LEFT JOIN CINEMA AS C3 ON C3.SEAT_ID + 1 = C1.SEAT_ID 
    WHERE C1.FREE = 1 AND (C2.FREE = 1 OR C3.FREE = 1)
    ORDER BY C1.SEAT_ID
```

```mysql
# ans using JOIN, ABS
SELECT DISTINCT C1.SEAT_ID
    FROM CINEMA AS C1
    JOIN CINEMA AS C2 
    ON ABS(C2.SEAT_ID - C1.SEAT_ID) = 1
    WHERE C1.FREE = 1 AND C2.FREE = 1
    ORDER BY C1.SEAT_ID
```



##### \1142. User Activity for the Past 30 Days II

```mysql
# ONLINE SOL

SELECT IFNULL(ROUND(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 0) 
    AS average_sessions_per_user
    FROM Activity
    WHERE DATEDIFF("2019-07-27", activity_date) < 30
```



##### \1179. Reformat Department Table

```mysql
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



##### \1241. Number of Comments per Post

```mysql
# my sol under hint

SELECT DISTINCT
    S1.sub_id AS post_id,
    (SELECT COUNT(DISTINCT(S2.sub_id)) FROM Submissions AS S2 WHERE S2.parent_id = S1.sub_id) AS number_of_comments
FROM Submissions AS S1
WHERE parent_id IS NULL
ORDER BY post_id
```



##### \1350. Students With Invalid Departments

```mysql
# MY SOL

SELECT ID, NAME
    FROM STUDENTS
    WHERE department_id NOT IN (
        SELECT ID FROM DEPARTMENTS
    )
```

