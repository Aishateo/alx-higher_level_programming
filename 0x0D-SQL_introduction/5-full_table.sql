-- Print the full table description for 'first_table' from the specified database
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM information_schema.columns
WHERE TABLE_SCHEMA = 'mysql'
  AND TABLE_NAME = 'first_table';
