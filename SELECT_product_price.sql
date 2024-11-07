SELECT product_price
    FROM dim_products;
UPDATE dim_products
    SET
        product_price = left(product_price, 1);
SELECT product_price
    FROM dim_products;