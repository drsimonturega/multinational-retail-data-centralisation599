SELECT
    column_name,
    data_type
FROM
    information_schema.columns
WHERE
    table_name = 'dim_products';
ALTER TABLE dim_products ALTER COLUMN weight TYPE double precision USING weight::double precision;
SELECT
    column_name,
    data_type
FROM
    information_schema.columns
WHERE
    table_name = 'dim_products';