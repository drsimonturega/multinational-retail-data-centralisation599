SELECT
     expiry_date
   , length(expiry_date)
FROM
    dim_card_details
GROUP BY
    expiry_date
ORDER BY
    length(expiry_date) desc
LIMIT 1;