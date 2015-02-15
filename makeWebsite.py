#author - Jian Li & Yike Chen
def name_detect(list_of_lines):
    '''get the name from the resume..'''
    resumeName = list_of_lines[0].rstrip().strip()
    if (resumeName)[0] not in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
        raise NameError('Please write your name with proper capitalization')
    else:
        return resumeName

def email_detect(list_of_lines):
    '''get the email address from the file'''
    for line in list_of_lines:
        lineReal = line.rstrip().lstrip()
        if '@' in lineReal:
            if (lineReal[-4:-1]+lineReal[-1]) == '.com' or (lineReal[-4:-1]+lineReal[-1]) == '.edu':
                for i in range(0,len(lineReal)):
                    if lineReal[i] == '@':
                        numStart = i
                strOfEmail = lineReal[numStart+1:(len(lineReal)- 4)]
                if strOfEmail[0] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
                    return lineReal
    return ''

def course_detect(list_of_lines):
    '''get the courses from the file'''
    courseNameList = []
    for line in list_of_lines:
        lineReal = line.rstrip().lstrip()
        if 'Courses' in lineReal:
            for i in range(7,len(lineReal)):
                if (lineReal[i] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']) or (lineReal[i] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']):
                    firstCourseWord = i
                    break
            courses = lineReal[firstCourseWord:len(lineReal)]
            courseNameList.extend(courses.split(','))
    return courseNameList
            
def projects_detect(list_of_lines):
    '''detect projects in the file'''
    projectList = []
    for i in range(0,len(list_of_lines)):
        if 'Projects' in (list_of_lines[i]):
            projectNum = i
            break
    for i in range(projectNum+1,len(list_of_lines)):
        projectName= list_of_lines[i].strip().lstrip()
        if len(projectName)>0:
            if '----------' not in projectName:
                projectList.append(projectName)
            elif '----------' in projectName:
                break  
    return projectList

def education_detect(list_of_lines):
    '''get the education information from the file'''
    educationList = []
    for line in list_of_lines:
        if ('University' in line or 'university' in line) and ('Bachelor' in line or 'bachelor' in line or 'Master' in line or 'master' in line or 'Doctor' in line or 'doctor' in line):
            lineReal = line.strip().lstrip()
            if len(lineReal) > 0:
                educationList.append(lineReal)
    return educationList
    
            
    

def main():
    filename = raw_input('Please enter a file you want to open:')
    f = open(filename)
    lines = f.readlines()
    resumeName = name_detect(lines)
    resumeEmail = email_detect(lines)
    resumeCourse = course_detect(lines)
    resumeProject = projects_detect(lines)
    resumeEducation = education_detect(lines)
    f.close()
    print resumeName
    print resumeEmail
    print resumeCourse
    print resumeProject
    print resumeEducation

if __name__ =="__main__":
    main()
