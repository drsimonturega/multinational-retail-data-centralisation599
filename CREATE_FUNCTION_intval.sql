CREATE FUNCTION intval(character varying) RETURNS integer AS $$

SELECT
CASE
    WHEN length(btrim(regexp_replace($1, '[^0-9]', '','g')))>0 THEN btrim(regexp_replace($1, '[^0-9]', '','g'))::integer
    ELSE 0
END AS intval;

$$
LANGUAGE SQL
IMMUTABLE
RETURNS NULL ON NULL INPUT;