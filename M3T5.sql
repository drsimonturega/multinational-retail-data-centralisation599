UPDATE dim_products
    SET still_available = True 
    WHERE still_available = 'Still_avaliable';
UPDATE dim_products
    SET still_available = False 
    WHERE still_available = 'Removed';
ALTER TABLE dim_products ALTER COLUMN product_price TYPE FLOAT USING product_price::float;
ALTER TABLE dim_products ALTER COLUMN weight TYPE FLOAT;
ALTER TABLE dim_products ALTER COLUMN "EAN" TYPE VARCHAR(17);
ALTER TABLE dim_products ALTER COLUMN product_code TYPE VARCHAR(11);
ALTER TABLE dim_products ALTER COLUMN date_added TYPE DATE USING date_added::date;
ALTER TABLE dim_products ALTER COLUMN uuid TYPE uuid USING uuid::uuid;
ALTER TABLE dim_products ALTER COLUMN still_available TYPE BOOL USING still_available::boolean;
ALTER TABLE dim_products ALTER COLUMN product_code TYPE VARCHAR(14);

SELECT
    column_name,
    data_type
FROM
    information_schema.columns
WHERE
    table_name = 'dim_products';