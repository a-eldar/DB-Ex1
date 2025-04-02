-- create table enrollment(
-- 	yrclosed varchar , 
-- 	year varchar, 
-- 	students5_estimated varchar
-- );

-- `year` might be datatype

create table university(
	iau_id1 varchar PRIMARY KEY,
	foundedyr integer CHECK(foundedyr >= 0) NOT NULL,
	yrclosed integer CHECK(yrclosed >= foundedyr),
	eng_name varchar NOT NULL, 
	orig_name varchar NOT NULL,
	private01 boolean,
	latitude float, 
	longitude float,
	phd_granting boolean,
	divisions integer, 
	specialized boolean,
	countrycode char(3) NOT NULL,
	FOREIGN KEY(countrycode) REFERENCES country(countrycode) ON DELETE CASCADE,
);

create table country(
	country varchar UNIQUE,
	countrycode char(3) PRIMARY KEY, 
	region varchar CHECK(region in (
		"East Asia and Pacific",
	 	"Europe and Central Asia",
		"Latin America and Caribbean",
		"Middle East and North Africa",
		"North America",
		"South Asia",
		"Sub-Saharan Africa"
		)), 
	incomegroup varchar CHECK(incomegroup in (
		"Low income",
		"Lower middle income",
		"Upper middle income",
		"High income"
	)),
);



create table students_accepted(
	year integer CHECK(year >= 0),
	iau_id1 varchar,
	students5_estimated integer CHECK (students5_estimated >= 0),
	PRIMARY KEY(iau_id1, year),
	FOREIGN KEY(iau_id1) REFERENCES university(iau_id1) ON DELETE CASCADE
);