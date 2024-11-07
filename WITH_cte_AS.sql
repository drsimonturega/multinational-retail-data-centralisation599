WITH cte AS (
    SELECT store_type, order_table.index, order_table.product_quantity
    FROM
        dim_store_details
    INNER JOIN
        order_table ON order_table.store_code = dim_store_details.store_code
    GROUP BY
        store_type, order_table.store_code, dim_store_details.store_code,
        order_table.index, order_table.product_quantity
)

SELECT *
FROM cte