-- create table enrollment(
-- 	yrclosed varchar , 
-- 	year varchar, 
-- 	students5_estimated varchar
-- );

-- `year` might be datatype

create table country(
	country varchar UNIQUE,
	countrycode char(3) PRIMARY KEY, 
	region VARCHAR CHECK (region IN (
        'East Asia and Pacific',
        'Europe and Central Asia',
        'Latin America and Caribbean',
        'Middle East and North Africa',
        'North America',
        'South Asia',
        'Sub-Saharan Africa'
    )), 
	incomegroup VARCHAR CHECK (incomegroup IN (
        'Low income',
        'Lower middle income',
        'Upper middle income',
        'High income'
    ))
);


CREATE TABLE university (
    iau_id1 VARCHAR PRIMARY KEY,
    foundedyr INTEGER CHECK(foundedyr >= 0) NOT NULL,
    yrclosed INTEGER CHECK(yrclosed >= foundedyr),
    eng_name VARCHAR NOT NULL, 
    orig_name VARCHAR NOT NULL,
    private01 BOOLEAN,
    latitude FLOAT, 
    longitude FLOAT,
    phd_granting BOOLEAN,
    divisions INTEGER, 
    specialized BOOLEAN,
    countrycode CHAR(3) NOT NULL,
    FOREIGN KEY (countrycode) REFERENCES country(countrycode) ON DELETE CASCADE
);



CREATE TABLE students_accepted (
    year INTEGER CHECK(year >= 0),
    iau_id1 VARCHAR,
    students5_estimated INTEGER CHECK (students5_estimated >= 0),
    PRIMARY KEY (iau_id1, year),
    FOREIGN KEY (iau_id1) REFERENCES university(iau_id1) ON DELETE CASCADE
);