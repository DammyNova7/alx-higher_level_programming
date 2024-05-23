-- prints the full description of a the table first_table.
SELECT *
FROM information_schema.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';

