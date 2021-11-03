## Queries with constraints

Use the `WHERE` clause to filter results from the query. The clause is applied to
each row to determine its inclusion. Complex clauses can be constructed by using
the `AND` or `OR` keywords. 

``` SQL
SELECT column
  FROM mytable
 WHERE condition
AND/OR condition2;
```

|       Operator      | Condition                                                                                             | SQL Example                                                        |
|:-------------------:|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
|  =, !=, < <=, >, >= | Standard numerical operators                                                                          | col_name != 4                                                      |
|   BETWEEN … AND …   | Number is within range of two values (inclusive)                                                      | col_name BETWEEN 1.5 AND 10.5                                      |
| NOT BETWEEN … AND … | Number is not within range of two values (inclusive)                                                  | col_name NOT BETWEEN 1 AND 10                                      |
|        IN (…)       | Number exists in a list                                                                               | col_name IN (2, 4, 6)                                              |
|      NOT IN (…)     | Number does not exist in a list                                                                       | col_name NOT IN (1, 3, 5)                                          |
|          =          | Case sensitive exact string comparison (notice the single equals)                                     | col_name = "abc"                                                   |
|       != or <>      | Case sensitive exact string inequality comparison                                                     | col_name != "abcd"                                                 |
|         LIKE        | Case insensitive exact string comparison                                                              | col_name LIKE "ABC"                                                |
|       NOT LIKE      | Case insensitive exact string inequality comparison                                                   | col_name NOT LIKE "ABCD"                                           |
|          %          | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) | col_name LIKE "%AT%" (matches "AT", "ATTIC", "CAT" or even "BATS") |
|          _          | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE)                    | col_name LIKE "AN_" (matches "AND", but not "AN")                  |
|        IN (…)       | String exists in a list                                                                               | col_name IN ("A", "B", "C")                                        |
|      NOT IN (…)     | String does not exist in a list                                                                       | col_name NOT IN ("D", "E", "F")                                    |

## Filtering and sorting query results

The `DISTINCT` keyword is used to discard duplicate rows that have duplicate 
column values

``` SQL
SELECT DISTINCT column
  FROM mytable
 WHERE condition
```

### Ordering results

Query results can be in ascending or descending order by using the `ORDER BY` clause

``` SQL
SELECT column
  FROM mytable
 WHERE condition
 ORDER BY column ASC/DESC;
```

### Limiting results to a subset

`LIMIT` and `OFFSET` clauses can be used to limit results to a certain amount of 
rows and choose where to start that limited range

``` SQL
SELECT column
  FROM mytable
 WHERE condition(s)
 ORDER BY column ASC/DESC
 LIMIT num_limit OFFSET num_offset;
```

## Multi-table queries with `JOIN`s

Database normalization prevents data from being duplicated in any single table. 
However, that can complicate the queries needed to retrieve data. `JOIN`s are used
to combine tables on common values between columns to find data from different 
tables.

`INNER JOIN` joins rows from two tables that have matching values. 

``` SQL
SELECT column, another_table_column, …
  FROM mytable
 INNER JOIN another_table 
    ON mytable.id = another_table.id
 WHERE condition(s)
 ORDER BY column, … ASC/DESC
 LIMIT num_limit OFFSET num_offset;
```

`LEFT JOIN` keeps rows from the first table regardless of whether there is a match
`RIGHT JOIN` keeps rows from the second table regardless of a match
`FULL JOIN` keeps rows from both tables regardless of a match