UPDATE dim_products
    SET weight_class = 'Light'
    WHERE weight < 2;
UPDATE dim_products
    SET weight_class = 'Mid_Sized'
    WHERE weight >= 2 AND weight < 40;
UPDATE dim_products
    SET weight_class = 'Heavy'
    WHERE weight >= 40 AND weight < 140; 
UPDATE dim_products
    SET weight_class = 'Truck_Required'
    WHERE weight >= 140; 
SELECT  weight, weight_class 
    FROM dim_products
    WHERE weight_class = 'Truck_Required';