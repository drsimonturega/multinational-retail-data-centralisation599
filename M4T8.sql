WITH cte AS (

    SELECT year, order_table.index, month
    FROM
        dim_date_times
    INNER JOIN
        order_table ON order_table.date_uuid = dim_date_times.date_uuid
    GROUP BY
        order_table.date_uuid, dim_date_times.date_uuid, order_table.index
)
, 
n_tab AS (
    SELECT COUNT(cte.year) AS total_sales, 
    year, month
FROM 
    cte
GROUP BY
    year, month 
)

SELECT DISTINCT ON (month)
    total_sales,  year, month
FROM
    n_tab
GROUP BY
    year, month, total_sales
ORDER BY
    month, total_sales DESC;

