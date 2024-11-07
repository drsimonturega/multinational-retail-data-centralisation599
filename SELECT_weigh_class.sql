SELECT *
    FROM dim_products;
ALTER TABLE dim_products 
    ADD COLUMN "weight_class" VARCHAR(14);
SELECT *
    FROM dim_products;
