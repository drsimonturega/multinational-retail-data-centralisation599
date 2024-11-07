--view primary key
SELECT conrelid::regclass AS table_name,
       conname AS primary_key, 
       pg_get_constraintdef(oid)
       -- lets see what this does
       --conrelid::regclass,
       --conname,
       --pg_get_constraintdef(oid)
FROM   pg_constraint 
WHERE  contype = 'f' 
AND    connamespace = 'public'::regnamespace   
ORDER  BY conrelid::regclass::text, contype DESC; 