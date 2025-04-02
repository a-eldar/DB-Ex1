import csv
from io import TextIOWrapper
from zipfile import ZipFile

# opens file.
# enrollment_outfile = open("enrollment.csv", 'w' , encoding='UTF8')
# enrollment_outwriter = csv.writer(enrollment_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)


ENROLLMENT_COLUMNS = [
    "country",
    "countrycode",
    "region",
    "incomegroup",
    "iau_id1",
    "eng_name",
    "orig_name",
    "foundedyr",
    "yrclosed",
    "private01",
    "latitude",
    "longitude",
    "phd_granting",
    "divisions",
    "specialized",
    "year",
    "students5_estimated"
]
INDEX_OF = {col: i for i, col in enumerate(ENROLLMENT_COLUMNS)}
UNIVERSITY_COLUMNS = [
    "iau_id1",
    "foundedyr",
    "yrclosed",
    "eng_name",
    "orig_name",
    "private01",
    "latitude",
    "longitude",
    "phd_granting",
    "divisions",
    "specialized",
    "countrycode"
]
COUNTRY_COLUMNS = [
    "country",
    "countrycode",
    "region",
    "incomegroup"
]
STUDENTS_ACCEPTED_COLUMNS = [
    "year",
    "iau_id1",
    "students5_estimated"
]




def parse_file_to_tables(university_outwriter, country_outwriter, students_accepted_outwriter, infile):
    """Goes over each row in the file and writes to the tables using the outwriters

    Args:
        university_outwriter (_writer): writer for university table
        country_outwriter (_writer): writer for country table
        students_accepted_outwriter (_writer): writer for students_accepted table
        infile (IO(bytes)): the file to parse
    """
    reader = csv.reader(TextIOWrapper(infile, 'utf-8'))
    # According to exercise notes (Q3e):
    # For some universities, not all the info is present in every row.
    # For those universities, the whole info appears in the last row.
    # So we'll go in reverse to ensure we get all of the info.
    reader = reversed(list(reader))
    university_set = set()
    country_set = set()
    students_accepted_set = set()
    for row in reader:
                # TO DO splits row into the different csv table files
        if row[INDEX_OF["iau_id1"]] == "iau_id1":
            continue
        
        if row[INDEX_OF["iau_id1"]] not in university_set:
            university_row = [row[INDEX_OF[col]] for col in UNIVERSITY_COLUMNS]
            university_outwriter.writerow(university_row)
            university_set.add(row[INDEX_OF["iau_id1"]])
                
        if row[INDEX_OF["countrycode"]] not in country_set:
            country_row = [row[INDEX_OF[col]] for col in COUNTRY_COLUMNS]
            country_outwriter.writerow(country_row)
            country_set.add(row[INDEX_OF["countrycode"]])
                
        if (row[INDEX_OF["iau_id1"]], row[INDEX_OF["year"]]) not in students_accepted_set:
            students_accepted_row = [row[INDEX_OF[col]] for col in STUDENTS_ACCEPTED_COLUMNS]
            students_accepted_outwriter.writerow(students_accepted_row)
            students_accepted_set.add((row[INDEX_OF["iau_id1"]], row[INDEX_OF["year"]]))
    


# process_file goes over all rows in original csv file, and sends each row to process_row()
def process_file():
    university_outfile = open("university.csv", 'w' , encoding='UTF8')
    university_outwriter = csv.writer(university_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    country_outfile = open("country.csv", 'w' , encoding='UTF8')
    country_outwriter = csv.writer(country_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
    students_accepted_outfile = open("students_accepted.csv", 'w' , encoding='UTF8')
    students_accepted_outwriter = csv.writer(students_accepted_outfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)

    university_outwriter.writerow(UNIVERSITY_COLUMNS)
    country_outwriter.writerow(COUNTRY_COLUMNS)
    students_accepted_outwriter.writerow(STUDENTS_ACCEPTED_COLUMNS)

    with ZipFile('enrollment.zip') as zf:
        with zf.open('enrollment.csv', 'r') as infile:
            parse_file_to_tables(university_outwriter, country_outwriter, students_accepted_outwriter, infile)


    # enrollment_outfile.close()
    university_outfile.close()
    country_outfile.close()
    students_accepted_outfile.close()

# return the list of all tables
def get_names():
    return ["country", "university", "students_accepted"]


if __name__ == "__main__":
    process_file()

