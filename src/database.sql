CREATE DATABASE nama_database;

CREATE TABLE covid_cases (
    id SERIAL PRIMARY KEY,
    date DATE,
    location_iso_code VARCHAR(10),
    location VARCHAR(100),
    new_cases INT,
    new_deaths INT,
    new_recovered INT,
    new_active_cases INT,
    total_cases INT,
    total_deaths INT,
    total_recovered INT,
    new_deaths_per_million FLOAT,
    total_deaths_per_million FLOAT,
    case_fatality_rate FLOAT,
    case_recovered_rate FLOAT,
    growth_factor_new_cases FLOAT,
    growth_factor_new_deaths FLOAT
);

COPY covid_cases(date, location_iso_code, location, new_cases, new_deaths, new_recovered, new_active_cases, total_cases, total_deaths, total_recovered, new_deaths_per_million, total_deaths_per_million, case_fatality_rate, case_recovered_rate, growth_factor_new_cases, growth_factor_new_deaths)
FROM 'datasets/MariSehat.csv'
DELIMITER ','
CSV HEADER;
