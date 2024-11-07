SELECT DISTINCT ON (country_code)
    country_code,
    SUM(staff_numbers) OVER (PARTITION BY country_code) AS total_staff
FROM
    dim_store_details