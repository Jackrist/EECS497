CREATE DATABASE lost_and_found;

USE lost_and_found;

-- Table for users
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    -- Add more user-related fields
);

-- Table for lost items
CREATE TABLE lost_items (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    item_name VARCHAR(100) NOT NULL,
    description TEXT,
    date_lost DATE,
    location VARCHAR(100),
    -- Add more item-related fields
);

-- Table for notification preferences
CREATE TABLE notification_preferences (
    user_id INT PRIMARY KEY,
    item_pickup BOOLEAN,
    item_dropoff BOOLEAN,
    new_messages BOOLEAN,
    -- Add more notification types
);