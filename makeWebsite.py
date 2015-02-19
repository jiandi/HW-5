#author - Jian Li & Yike Chen
import string

def isLetterLower(letter):
    '''check if the letter is lower case'''
    if letter in string.ascii_lowercase:
        return True
    else:
        return False


def isLetterUpper(letter):
    '''Check if the letter is uppercase'''
    if letter in string.ascii_uppercase:
        return True
    else:
        return False


def name_detect(list_of_lines):
    '''get the name from the resume..'''
    #return a string
    resumeName = list_of_lines[0].rstrip().lstrip()
    if not isLetterUpper(resumeName[0]):
        raise NameError('Please write your name with proper capitalization')
    else:
        return resumeName

def email_detect(list_of_lines):
    '''get the email address from the file'''
    #return a list
    emailAddress=[]
    for line in list_of_lines:
        lineReal = line.rstrip().lstrip()
        if '@' in lineReal:
            #see if the line has .com or .edu in it
            if (lineReal[-4:-1]+lineReal[-1]) == '.com' or (lineReal[-4:-1]+lineReal[-1]) == '.edu':
                for i in range(0,len(lineReal)):
                    if lineReal[i] == '@':
                        numStart = i
                strOfEmail = lineReal[numStart+1:(len(lineReal)- 4)]
                #judge if the first letter after @ is lower case
                if isLetterLower(strOfEmail[0]):
                    emailAddress.append(lineReal)
    return emailAddress

def course_detect(list_of_lines):
    '''get the courses from the file'''
    #return a list
    courseNameList = []
    for line in list_of_lines:
        lineReal = line.rstrip().lstrip()
        if 'Courses' in lineReal:
            for i in range(7,len(lineReal)):
                # let the index start from after course, and detect the fisrt letter, either lower or upper case
                if isLetterLower(lineReal[i])or isLetterUpper(lineReal[i]):
                    firstCourseWord = i
                    break
            #get the line of course and split it into courses
            courses = lineReal[firstCourseWord:len(lineReal)]
            courseNameList.extend(courses.split(','))
    return courseNameList
            
def projects_detect(list_of_lines):
    '''detect projects in the file'''
    #return a list
    projectList = []
    for i in range(0,len(list_of_lines)):
        if 'Projects' in (list_of_lines[i]):
            projectNum = i
            break
    #let the pointer start from after of title of Project
    for i in range(projectNum+1,len(list_of_lines)):
        projectName= list_of_lines[i].strip().lstrip()
        if len(projectName)>0:
            # append project name
            if '----------' not in projectName:
                projectList.append(projectName)
            elif '----------' in projectName:
                break  
    return projectList

def education_detect(list_of_lines):
    '''get the education information from the file'''
    #return a list
    educationList = []
    for line in list_of_lines:
        #detect key words
        if ('University' in line or 'university' in line) and ('Bachelor' in line or 'bachelor' in line or 'Master' in line or 'master' in line or 'Doctor' in line or 'doctor' in line):
            lineReal = line.strip().lstrip()
            if len(lineReal) > 0:
                educationList.append(lineReal)
    return educationList

def surround_block(tag,lst):
    '''A function that surrounds some text(lists) in an html file'''
    lists=['<']
    lists.append(tag)
    lists.append('>\n')
    # this subfunction is able to take a list of strings and surround them with tag
    for element in lst:
        lists.extend(element)
    lists.append('\n</')
    lists.append(tag)
    lists.append('>\n')
    return lists

#The following functions are about writing html!   
def initial_step_write(f):
    '''write the first line of html'''
    f.write('<div id="page-wrap">\n\n')
    
    
def final_step_write(f):
    '''Conclude the html with these lines'''
    f.write('</div>\n')
    f.write('</body>\n')
    f.write('</html>\n')
    

def write_basic_info(f,name,email):
    '''write basic information into the html file--name and email'''
    basic_information=[]
    Name = surround_block('h1',name)
    basic_information.extend(Name)
    # include multiple emails each with surround block, store them in basic information
    # and then surround basic information in a block
    for mail in email:
        basic_information.extend(surround_block('p',mail))
    basic_information = surround_block('div',basic_information)
    f.writelines(basic_information)


def write_education_info (f,education):
    '''write education information'''
    edu_info=[]
    f.write('<div>\n')
    title = surround_block('h2','Education')
    f.writelines(title)
    # include multiple education background each with surround block, store them in education information
    # and then surround education information in a block
    for edu in education:
        edu_info.extend(surround_block('li',edu))
    edu_info = surround_block('ul',edu_info)
    f.writelines(edu_info)
    f.write('</div>\n\n')

def write_project_info (f,project):
    '''write project information'''
    project_info=[]
    f.write('<div>\n')
    title = surround_block('h2','Projects')
    f.writelines(title)
    # include multiple project each with surround block, store them in project information
    # and then surround project information in a block
    for projects in project:
        project_info.extend(surround_block('li',surround_block('p',projects)))
    project_info = surround_block('ul',project_info)
    f.writelines(project_info)
    f.write('</div>\n\n')

def write_course_info (f,course):
    '''write course information'''
    course_info=[]
    f.write('<div>\n')
    title = surround_block('h3','Courses')
    f.writelines(title)

    # include multiple course with surround block, using +',' to solve the separation problem
    # The last course does not require a ',' to conclude it
    for i in range(0,len(course)-1):
        course[i] = course[i]+','
    course_info.extend(surround_block('span',course))
    f.writelines(course_info)
    f.write('</div>\n\n')


def resume_write(f,name,email,course,project,education):
    '''Write all the information to the html file'''
    #name is a string, other arguments are lists
    #write each information in the resume step by step
    initial_step_write(f)
    write_basic_info(f,name,email)
    write_education_info (f,education)
    write_project_info(f,project)
    write_course_info(f,course)
    final_step_write(f)


def main():
    '''Main function, which reads date from txt file and write into html'''
    filename = raw_input('Please enter a file you want to open:')
##    filename = 'resume.txt'
    f = open(filename)
    lines = f.readlines()
    Name = name_detect(lines)
    Email = email_detect(lines)
    Course = course_detect(lines)
    Project = projects_detect(lines)
    Education = education_detect(lines)
    f.close()
    #print all the informtion in the resume.txt
    print Name
    print Email
    print Course
    print Project
    print Education

    #Then for the writing html part
    filename_html = raw_input('Please enter a html file you want to write into:')
    f = open(filename_html,'r+')
    lines = f.readlines()
    f.seek(0)
    f.truncate()
    del lines[-1]
    del lines[-1]
    f.writelines(lines)
    resume_write(f,Name,Email,Course,Project,Education)
    f.close()
    
    

if __name__ =="__main__":
    main()
