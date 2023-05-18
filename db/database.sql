CREATE DATABASE IF NOT EXISTS flighttracker
USE flighttracker

CREATE TABLE IF NOT EXISTS users {
  uuid SERIAL PRIMARY KEY,
  username VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL,
  password VARCHAR(100) NOT NULL,
  device_code VARCHAR(7) DEFAULT "0000000"
  createdAt TIMESTAMP DEFAULT now(),
  updatedAt TIMESTAMP DEFAULT now()
}

CREATE TABLE IF NOT EXISTS flight_logs {
  uuid SERIAL PRIMARY KEY,
  device_code VARCHAR(7) NOT NULL,
  start_time int NOT NULL,
  total_time int NOT NULL
  createdAt TIMESTAMP DEFAULT now(),
  updatedAt TIMESTAMP DEFAULT now()
}

CREATE TABLE IF NOT EXISTS devices {
  uuid SERIAL PRIMARY KEY,
  serial_number VARCHAR(255) NOT NULL,
  ip_address VARCHAR(255) NOT NULL,
  device_name VARCHAR(100) NOT NULL,
  device_code VARCHAR(7) NOT NULL,
  createdAt TIMESTAMP DEFAULT now(),
  updatedAt TIMESTAMP DEFAULT now()
}

CREATE TABLE IF NOT EXISTS known_serials {
  uuid SERIAL PRIMARY KEY,
  serial_number VARCHAR(255) NOT NULL,
  device_code VARCHAR(7) NOT NULL
}

INSERT INTO known_serials (serial_number) VALUES ('21AH250C99EV34')