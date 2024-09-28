-- -- @block
-- ALTER TABLE water_fountains 
-- RENAME COLUMN name to fountain_name;

-- -- @block
-- UPDATE water_fountains 
-- SET latitude = 43.472329, longitude = -80.546754
-- WHERE id = 3;
-- -- @block
-- ALTER TABLE water_fountains 
-- ADD latitude FLOAT

-- -- @block
-- SELECT * FROM water_fountains
-- -- @block
-- SELECT * FROM Users
-- INNER JOIN water_fountains_rating
-- ON Users.id = water_fountains_rating.user_id

-- -- @block
-- SELECT AVG(taste)
-- FROM water_fountains_rating
-- WHERE water_fountain_id = 3;
-- -- @block
-- SELECT user_id, water_fountain_id, taste, texture FROM water_fountains_rating;

-- -- @block
-- INSERT INTO water_fountains_rating (user_id, water_fountain_id, taste, texture)
-- VALUES
--     (1, 1, 4.5, 3),
--     (3, 2, 2, 2.1),
--     (2, 3, 5, 5),
--     (4, 3, 5, 5);
-- -- @block
-- SELECT id, fountain_name, building, location_in_building, status, water_bottle_filler FROM water_fountains;
-- -- @block
-- INSERT INTO Water_Fountains (name, building, location_in_building, status, water_bottle_filler)
-- VALUES 
--     ('Jerry', 'SJU', 'Floor 2', 'Working', 1),
--     ('Irene''s favorite', 'RCH', 'Basement', 'Working', 1),
--     ('PACtrick', 'PAC', 'Main Entrance', 'Working', 1);

-- -- @block
-- SELECT id, username, WATIAM, bio FROM users;

-- -- @block
-- INSERT INTO Users (username, WATIAM, bio)
-- VALUES 
--     ('be.creative', 'a6zhuang', 'water enthusiast'),
--     ('greenpants ', 'l753wang', 'lloloolooploops'),
--     ('emily', 'e3qi', 'o h h'),
--     ('duckduckgoose', 'chjin', 'i love geese');

-- -- @block 
-- CREATE TABLE Water_fountains_rating (
--     id INT AUTO_INCREMENT,
--     user_id INT NOT NULL,
--     water_fountain_id INT NOT NULL,
--     taste FLOAT,
--     texture FLOAT,
--     PRIMARY KEY(id),
--     FOREIGN KEY (user_id) REFERENCES Users(id),
--     FOREIGN KEY (water_fountain_id) REFERENCES Water_fountains_rating(id)
-- );

-- -- @block
-- CREATE TABLE Water_Fountains(
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     building VARCHAR(3),
--     location_in_building TEXT,
--     total_bottles_filled INT,
--     status VARCHAR (255),
--     water_bottle_filler BOOLEAN
-- );

-- -- @block 
-- CREATE TABLE Users(
--     id INT PRIMARY KEY AUTO_INCREMENT,
--     username VARCHAR(255),
--     WATIAM VARCHAR(255) NOT NULL UNIQUE,    
--     bio TEXT
-- );