# This program is used to write the txt file about Marketing Master program.
# Define main()
def main():
    another = 'y'
    university_file = open('university.txt', 'w')
    while another == 'y' or another == 'Y':
        university_name = input('Enter the university name: ')
        program_name = input('Enter the program name: ')
        num_course = int(input('Enter the number of the course: '))
        university_file.write(university_name + '\n')
        university_file.write(program_name+'\n')
        university_file.write(str(num_course)+'\n')
        for count in range (1, num_course +1):
            marketing_course_name = input('Enter the name of marketing_course_name #' + str(count) + ':')
            university_file.write(marketing_course_name + '\n')
            count = count + 1
    
            
        another = input('Enter y or Y for yes, and others for no: ')
    university_file.close()

    print('The university data are recored to university.txt')




main()