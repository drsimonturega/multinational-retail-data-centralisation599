ALTER TABLE dim_card_details ALTER COLUMN card_number TYPE VARCHAR(22);
ALTER TABLE dim_card_details ALTER COLUMN expiry_date TYPE VARCHAR(5);
ALTER TABLE dim_card_details ALTER COLUMN date_payment_confirmed TYPE date;
SELECT
    column_name,
    data_type
FROM
    information_schema.columns
WHERE
    table_name = 'dim_card_details';