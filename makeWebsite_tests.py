#author - Jian Li & Yike Chen
import unittest
from makeWebsite import *

class Test_makeWebsite(unittest.TestCase):

    filename = ''
    def setUp(self):
        self.filename = 'resume.txt'

    def test_name_detect(self):
        #input a normal line with name in it
        name = name_detect(['Jian Li ','Shanghai  Jiao Tong ',' UPenn '])
        self.assertEqual('Jian Li',name)

        #for the raises exception
        self.assertRaises(NameError,name_detect,['jian Li','Shanghai Jiao Tong','UPenn'])
        self.assertRaises(NameError,name_detect,['2Jian Li','Shanghai Jiao Tong','UPenn'])


    def test_email_detect(self):
        emailAdd = email_detect(['Jian Li','lijian2@seas.upenn.edu','UPenn'])
        self.assertEqual('lijian2@seas.upenn.edu',emailAdd)
      

        #If there are '.COM' or '.EDU' in the address
        emailAdd2 = email_detect(['Jian Li','lijian2@seas.upenn.EDU','UPenn'])
        emailAdd3 = email_detect(['Jian Li','jiandi_li@163.COM','UPenn'])
        self.assertEqual('',emailAdd2)
        self.assertEqual('',emailAdd3)
        #If there is no string begin with a normal lowercase between '@'and the ending
        emailAdd4 = email_detect(['Jian Li','UPenn','jiandi_li@163.com'])
        self.assertEqual('',emailAdd4)

    def test_course_detect(self):
        #We should ignore the punctuation
        course1 = set(course_detect(['Jian Li','UPenn','SEAS','Courses:--:CIT590,Biomedical image analysis,Mechatronics\n','Sansom']))
        self.assertEqual(set(['CIT590','Biomedical image analysis','Mechatronics']),course1)
        course2 = set(course_detect(['Jian Li','UPenn','SEAS','Sansom','Courses,--::Robotics,Biomedical image analysis,Mechatronics\n']))
        self.assertEqual(set(['Robotics','Biomedical image analysis','Mechatronics']),course2)        

    def test_projects_detect(self):
        #there is a blank line 
        project1 = set(projects_detect(['Jian Li\n','lijian2@seas.upenn.edu','Projects\n','GRASP LAB\n','\n','Robockey\n','-----------\n']))
        self.assertEqual(set(['GRASP LAB','Robockey']),project1)
        #there are more than one blank line
        project2 = set(projects_detect(['Jian Li\n','lijian2@seas.upenn.edu','Projects\n','\n','GRASP LAB\n','\n','Robockey\n','-----------\n']))
        self.assertEqual(set(['GRASP LAB','Robockey']),project2)

    def test_education_detect(self):
        education1 = set(education_detect(['Jian Li','University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering\n','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering\n']))
        self.assertEqual(set(['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering']),education1)
        
        #If there is a blank line between these education information
        education2 = set(education_detect(['Jian Li','University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering\n','\n','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering\n']))
        self.assertEqual(set(['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering']),education2)
        
        #If there is a project done in a university in the list
        education3 = set(education_detect(['Jian Li','robockey-university of pennsylvania','University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering\n','\n','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering\n']))
        self.assertEqual(set(['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering']),education3)

unittest.main()
