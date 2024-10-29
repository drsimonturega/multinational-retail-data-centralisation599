ALTER TABLE order_table ALTER COLUMN product_quantity TYPE SMALLINT;
ALTER TABLE order_table ALTER COLUMN product_code TYPE VARCHAR(14);
ALTER TABLE order_table ALTER COLUMN store_code TYPE VARCHAR(12);
ALTER TABLE order_table ALTER COLUMN card_number TYPE VARCHAR(22);
ALTER TABLE order_table ALTER COLUMN user_uuid TYPE uuid USING user_uuid::uuid;
SELECT
    column_name,
    data_type
FROM
    information_schema.columns
WHERE
    table_name = 'order_table';