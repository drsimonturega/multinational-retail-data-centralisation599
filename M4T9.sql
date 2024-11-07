WITH cte AS (

    SELECT timestamp, 
        intval(month) AS int_month, 
        intval(year) AS int_year,
        intval(day) AS int_day,
        order_table.index, order_table.date_uuid, 
        order_table.product_code, order_table.product_quantity

    FROM
        dim_date_times
    INNER JOIN
        order_table ON order_table.date_uuid = dim_date_times.date_uuid
    GROUP BY
        order_table.date_uuid, dim_date_times.date_uuid, order_table.index,
        order_table.product_code, order_table.product_quantity
),
w_prod AS (
    SELECT  cte.date_uuid, cte.timestamp,
            MAKE_DATE(cte.int_year, cte.int_month, cte.int_day) AS date,
            cte.product_code, cte.product_quantity,
            dim_products.product_price, cte.int_year AS year,
            (dim_products.product_price * cte.product_quantity) AS sales_value
            
            
        FROM
            dim_products
        INNER JOIN
            cte ON cte.product_code = dim_products.product_code
        GROUP BY
            cte.date_uuid, cte.timestamp,
            cte.product_code, cte.product_quantity,
            dim_products.product_price,cte.int_year,
            date
),
p_time AS(
SELECT TO_TIMESTAMP(date || ' ' || timestamp, 'YYYY-MM-DD HH24:MI:SS') AS f_stamp,
    year
FROM w_prod
),
n_time AS(
    SELECT year,
        f_stamp,
        lead(f_stamp) OVER (PARTITION BY year ORDER BY f_stamp) AS next_time
    FROM
        p_time
),
ave_time AS(
    SELECT year, 
        next_time - f_stamp AS time_bewteen
    FROM
        n_time
)

SELECT year,
    AVG(time_bewteen) AS actual_time_taken
FROM
    ave_time
GROUP BY
    year
ORDER BY
    actual_time_taken DESC;




