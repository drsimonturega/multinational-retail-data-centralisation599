WITH cte AS (

    SELECT month, order_table.index
    FROM
        dim_date_times
    INNER JOIN
        order_table ON order_table.date_uuid = dim_date_times.date_uuid
    GROUP BY
        order_table.date_uuid, dim_date_times.date_uuid, order_table.index
)

SELECT COUNT(cte.month) AS total_sales, month
FROM cte
GROUP BY
    month
ORDER BY
    total_sales DESC;
    
