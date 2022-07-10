# This program is used to read university.txt and analyze the frequency of word occurence

# read the university courses name from univeristy.txt
def find():
    university_file = open('university.txt', 'r')
    university_name = university_file.readline()
    while university_name != '':
        program_name = university_file.readline()
        course_number = university_file.readline()
        program_name = program_name.rstrip('\n')
        course_number = course_number.rstrip('\n')
        # count the number of course
        course_number = int(course_number)
        # according to the number of the course to print course name
        for count in range(1, course_number + 1):
            course_name = university_file.readline()
            course_name = course_name.rstrip()
            print(course_name)
        university_name = university_file.readline()
    university_file.close()

find()
        
