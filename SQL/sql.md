## Order of operations

``` SQL
SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
  FROM mytable
  JOIN another_table
    ON mytable.column = another_table.column
 WHERE constraint_expression
 GROUP BY column
HAVING constraint_expression
 ORDER BY column ASC/DESC
 LIMIT count OFFSET count;
```

1. FROM and JOINs
The FROM clause, and subsequent JOINs are first executed to determine the total 
working set of data that is being queried. This includes subqueries in this 
clause, and can cause temporary tables to be created under the hood containing 
all the columns and rows of the tables being joined.

2. WHERE
Once we have the total working set of data, the first-pass WHERE constraints are
applied to the individual rows, and rows that do not satisfy the constraint are
discarded. Each of the constraints can only access columns directly from the 
tables requested in the FROM clause. Aliases in the SELECT part of the query are 
not accessible in most databases since they may include expressions dependent on 
parts of the query that have not yet executed.

3. GROUP BY
The remaining rows after the WHERE constraints are applied are then grouped based 
on common values in the column specified in the GROUP BY clause. As a result of 
the grouping, there will only be as many rows as there are unique values in that 
column. Implicitly, this means that you should only need to use this when you 
have aggregate functions in your query.

4. HAVING
If the query has a GROUP BY clause, then the constraints in the HAVING clause are 
then applied to the grouped rows, discard the grouped rows that don't satisfy the 
constraint. Like the WHERE clause, aliases are also not accessible from this step 
in most databases.

5. SELECT
Any expressions in the SELECT part of the query are finally computed.

6. DISTINCT
Of the remaining rows, rows with duplicate values in the column marked as DISTINCT 
will be discarded.

7. ORDER BY
If an order is specified by the ORDER BY clause, the rows are then sorted by the 
specified data in either ascending or descending order. Since all the expressions 
in the SELECT part of the query have been computed, you can reference aliases in 
this clause.

8. LIMIT / OFFSET
Finally, the rows that fall outside the range specified by the LIMIT and OFFSET 
are discarded, leaving the final set of rows to be returned from the query.

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

## Querying with expressions

You can use expressions to transform raw data to suit your purposes with math or
string functions. 

``` SQL
SELECT particle_speed / 2.0 AS half_particle_speed
  FROM physics_data
 WHERE ABS(particle_position) * 10.0 > 500;
```

The `AS` keyword is used to give column or table names an alias

``` SQL
SELECT column AS better_column_name, …
  FROM a_long_widgets_table_name AS mywidgets
  JOIN widget_sales
    ON mywidgets.id = widget_sales.widget_id;
```

## Aggregates

Aggregate functions are used to summarize data from a column into a single value.

Here are some common aggregate functions

| Function                | Description                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COUNT(*), COUNT(column) | A common function used to counts the number of rows in the group if no column name is specified. Otherwise, count the number of rows in the group with non-NULL values in the specified column. |
| MIN(column)             | Finds the smallest numerical value in the specified column for all rows in the group.                                                                                                           |
| MAX(column)             | Finds the largest numerical value in the specified column for all rows in the group.                                                                                                            |
| AVG(column)             | Finds the average numerical value in the specified column for all rows in the group.                                                                                                            |
| SUM(column)             | Finds the sum of all numerical values in the specified column for the rows in the group.                                                                                                        |

If used with the `GROUP BY` clause, the aggregate will apply to the groups not 
the entire column

The `HAVING` clause is used to apply certain limiting conditions to the groups 
formed by the `GROUP BY` clause

``` SQL
SELECT group_by_column, AGG_FUNC(column_expression) AS aggregate_result_alias, …
  FROM mytable
 WHERE condition
 GROUP BY column
HAVING group_condition;
```