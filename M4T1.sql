SELECT country_code AS country, COUNT(country_code) AS total_no_stores
FROM
    dim_store_details
GROUP BY
    country_code