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

-- @block
INSERT INTO water_fountains (fountain_name, building, location_in_building, status, water_bottle_filler, latitude, longitude)
VALUES 
    ('Working', 'M3', 'Third floor beside bathroom','Working',0 , 43.473373, -80.543876),
    ('STCER', 'STC', 'First floor beside stairs','Working', 1, 43.470476, -80.543012),
    ('Nano', 'QNC', 'Beside entrance first floor','Broken',0 , 43.471150, -80.544517),
    ('Health', 'LHI', 'Second floor beside bathroom','Working',1 , 43.473255, -80.545781),
    ('mathy', 'MC', 'Fifth floor beside the bathroom','Broken', 0 , 43.472076, -80.543574),
    ('CHEM', 'C2', 'First floor beside bathroom','Broken', 1 , 43.472328, -80.542743),
    ('eng', 'E3', 'Basement beside atrium','Working', 1, 43.471296, -80.541392),
    ('bookworm', 'DP', 'Tenth floor beside elevator','Working', 1, 43.469942, -80.542431),
    ('worker', 'E7', 'Second floor beside staircase','Working', 1, 43.473212, -80.539265),
    ('lecture', 'DWE', 'Basement beside 101','Broken',0 , 43.469721, -80.540367),
    ('WWW', 'SCH', 'First floor beside W store','Working',0 ,43.469161, -80.540657),
    ('washroom', 'AL', 'Basement beside women washroom','Working', 1, 43.468726, -80.541472);
-- @block
SELECT * FROM water_fountains;
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