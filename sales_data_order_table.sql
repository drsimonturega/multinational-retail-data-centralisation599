ALTER TABLE order_table ALTER COLUMN date_uuid TYPE UUID USING date_uuid::uuid;
ALTER TABLE order_table ALTER COLUMN user_uuid TYPE UUID USING date_uuid::uuid;
ALTER TABLE order_table ALTER COLUMN card_number TYPE VARCHAR(19); 
ALTER TABLE order_table ALTER COLUMN store_code TYPE VARCHAR(12); 
ALTER TABLE order_table ALTER COLUMN product_code TYPE VARCHAR(11); 
ALTER TABLE order_table ALTER COLUMN product_quantity TYPE VARCHAR(2);