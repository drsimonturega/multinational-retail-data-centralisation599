ALTER TABLE dim_date_times ALTER COLUMN month TYPE VARCHAR(2);
ALTER TABLE dim_date_times ALTER COLUMN day TYPE VARCHAR(2);
ALTER TABLE dim_date_times ALTER COLUMN year TYPE VARCHAR(4);
ALTER TABLE dim_date_times ALTER COLUMN time_period TYPE VARCHAR(10);
ALTER TABLE dim_date_times ALTER COLUMN date_uuid TYPE uuid USING date_uuid::uuid;
SELECT
    column_name,
    data_type
FROM
    information_schema.columns
WHERE
    table_name = 'dim_date_times';