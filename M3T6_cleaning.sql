DELETE FROM dim_date_times
    WHERE (day ~* '[a-z]') is true;
SELECT *
    FROM dim_date_times
    WHERE (day ~* '[a-z]') is true;
