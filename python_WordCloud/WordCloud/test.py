import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def main():
    text = find()
    x, y = np.ogrid[:300, :300]

    mask = (x - 150) ** 2 + (y - 150) ** 2 > 130 ** 2
    mask = 255 * mask.astype(int)

    exclude = {'Marketing','and','in','of','Marketing','the','for','a','to','I','II'}
    wc = WordCloud(background_color="white", repeat=False, mask=mask, stopwords=exclude)
    wc.generate(text)
    wc.to_file("text.png")

    plt.axis("off")
    plt.imshow(wc, interpolation="bilinear")

    plt.show()


def find():
    university_file = open('university.txt', 'r')
    university_name = university_file.readline()
    result = ''
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
            course_name = course_name.rstrip('\n')
            result += course_name
        university_name = university_file.readline()
    university_file.close()
    return result



main()