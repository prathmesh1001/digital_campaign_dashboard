-- 1. Remove duplicates
DELETE FROM table_name WHERE id NOT IN (SELECT MIN(id) FROM table_name GROUP BY column1, column2); -- removes duplicate rows

-- 2. Remove NULLs
DELETE FROM table_name WHERE column_name IS NULL; -- deletes rows with NULL

-- 3. Replace NULL with default
UPDATE table_name SET column_name = 'default_value' WHERE column_name IS NULL; -- fills missing values

-- 4. Trim spaces
UPDATE table_name SET column_name = TRIM(column_name); -- removes extra spaces

-- 5. Change data type
ALTER TABLE table_name MODIFY column_name INT; -- converts column type

-- 6. Standardize text (lowercase)
UPDATE table_name SET column_name = LOWER(column_name); -- makes text lowercase

-- 7. Remove special characters
UPDATE table_name SET column_name = REGEXP_REPLACE(column_name, '[^a-zA-Z0-9 ]', ''); -- removes symbols

-- 8. Fix wrong values
UPDATE table_name SET column_name = 'CorrectValue' WHERE column_name = 'WrongValue'; -- corrects wrong entries

-- 9. Add a new column
ALTER TABLE table_name ADD COLUMN new_column VARCHAR(50); -- creates new column

-- 10. Remove unused column
ALTER TABLE table_name DROP COLUMN old_column; -- deletes unnecessary column