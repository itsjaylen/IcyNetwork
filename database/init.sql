-- init.sql

-- Create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20) UNIQUE,
    phone_number_verified BOOLEAN DEFAULT FALSE,
    email_verified BOOLEAN DEFAULT FALSE,
    hashed_password VARCHAR(100) NOT NULL,
    salt VARCHAR(100) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT current_timestamp,
    global_banned BOOLEAN DEFAULT FALSE,
    role VARCHAR(100) DEFAULT 'user',
    active BOOLEAN DEFAULT TRUE,
    api_key VARCHAR(100) UNIQUE,
    profile_picture VARCHAR(200)
);

-- Create the servers table
CREATE TABLE servers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description VARCHAR(255),
    region VARCHAR(20) NOT NULL DEFAULT 'us-east',
    verification_level INTEGER NOT NULL DEFAULT 0,
    default_message_notifications INTEGER NOT NULL DEFAULT 0,
    explicit_content_filter INTEGER NOT NULL DEFAULT 0,
    afk_channel_id INTEGER REFERENCES channels(id),
    afk_timeout INTEGER NOT NULL DEFAULT 300,
    icon VARCHAR(255),
    banner VARCHAR(255),
    splash VARCHAR(255),
    system_channel_id INTEGER REFERENCES channels(id),
    system_channel_flags INTEGER NOT NULL DEFAULT 0,
    owner_id INTEGER REFERENCES users(id)
);
