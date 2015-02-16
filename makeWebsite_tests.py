#author - Jian Li & Yike Chen
import unittest
from makeWebsite import *

class Test_makeWebsite(unittest.TestCase):

    filename = ''
    def setUp(self):
        self.filename = 'resume.html'
        self.filename2 = 'my_test_for_HW5.txt'
        

    def test_name_detect(self):
        #input a normal line with name in it
        name = name_detect(['Jian Li ','Shanghai  Jiao Tong ',' UPenn '])
        self.assertEqual('Jian Li',name)

        #for the raises exception
        self.assertRaises(NameError,name_detect,['jian Li','Shanghai Jiao Tong','UPenn'])
        self.assertRaises(NameError,name_detect,['2Jian Li','Shanghai Jiao Tong','UPenn'])


    def test_email_detect(self):
        emailAdd = email_detect(['Jian Li','lijian2@seas.upenn.edu','UPenn'])
        self.assertEqual(['lijian2@seas.upenn.edu'],emailAdd)
      

        #If there are '.COM' or '.EDU' in the address
        emailAdd2 = email_detect(['Jian Li','lijian2@seas.upenn.EDU','UPenn'])
        emailAdd3 = email_detect(['Jian Li','jiandi_li@163.COM','UPenn'])
        self.assertEqual([],emailAdd2)
        self.assertEqual([],emailAdd3)
        #If there is no string begin with a normal lowercase between '@'and the ending
        emailAdd4 = email_detect(['Jian Li','UPenn','jiandi_li@163.com'])
        self.assertEqual([],emailAdd4)
        #If there are two email addresses in the list
        emailAdd5 = set(email_detect(['Jian Li','UPenn','lijian2@seas.upenn.edu','jiandi_li@gmail.com']))
        self.assertEqual(set(['lijian2@seas.upenn.edu','jiandi_li@gmail.com']),emailAdd5)

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

    def test_surround_block(self):
        htmlBlock = surround_block('div',['Jian Li'])
        self.assertEqual(['<','div','>\n','J','i','a','n',' ','L','i','\n</','div','>\n'],htmlBlock)

        #if there are more than one element in the argument list
        htmlBlock2 = surround_block('div',['Jian Li','UPenn'])
        self.assertEqual(['<','div','>\n','J','i','a','n',' ','L','i','U','P','e','n','n','\n</','div','>\n'],htmlBlock2)

    def test_initial_step(self):
        f_initial = open(self.filename)
        lines = f_initial.readlines()
        f_initial.close()
        self.assertTrue('<div id="page-wrap">\n' in lines)

    def test_final_step(self):
        f_final = open(self.filename)
        lines = f_final.readlines()
        f_final.close()
        self.assertTrue('</div>\n' in lines)
        self.assertTrue('</body>\n' in lines)
        self.assertTrue('</html>\n' in lines)

    def test_basic_info(self):
        f_basic = open(self.filename2,'w')
        basic_info(f_basic,'Jian Li',['lijian2@seas.upenn.edu'])
        f_basic.close()
        f_basic_r = open(self.filename2)
        lines = f_basic_r.readlines()
        f_basic_r.close()
        self.assertTrue('Jian Li\n' in lines)
        self.assertTrue('lijian2@seas.upenn.edu\n' in lines)

    def test_education_info(self):
        f_education = open(self.filename2,'w')
        education_info(f_education,['University of Pennsylvania','Shanghai Jiao Tong University'])
        f_education.close()
        f_education_r = open(self.filename2)
        lines = f_education_r.readlines()
        f_education_r.close()
        self.assertTrue('Education\n' in lines)
        self.assertTrue('University of Pennsylvania\n' in lines)
        self.assertTrue('Shanghai Jiao Tong University\n' in lines)

    def test_project_info(self):
        f_project = open(self.filename2,'w')
        project_info(f_project,['Robockey','PUMA Light Painting'])
        f_project.close()
        f_project_r = open(self.filename2)
        lines = f_project_r.readlines()
        f_project_r.close()
        self.assertTrue('Projects\n' in lines)
        self.assertTrue('Robockey\n' in lines)
        self.assertTrue('PUMA Light Painting\n' in lines)

    def test_course_info(self):
        f_course = open(self.filename2,'w')
        course_info(f_course,['CIT590','MEAM513','ENM510'])
        f_course.close()
        f_course_r = open(self.filename2)
        lines = f_course_r.readlines()
        f_course_r.close()
        self.assertTrue('Courses\n' in lines)
        self.assertTrue('CIT590,\n' in lines)
        self.assertTrue('MEAM513,\n' in lines)
        self.assertTrue('ENM510\n' in lines)

    def test_resume_open(self):
        f_resume = open(self.filename)
        lines = f_resume.readlines()
        f_resume.close()
        self.assertTrue('Jian Li\n' in lines)
        self.assertTrue('lijian2@seas.upenn.edu\n' in lines)
        self.assertTrue('Education\n' in lines)
        self.assertTrue('University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engineering\n' in lines)
        self.assertTrue('Shanghai Jiao Tong University, Shanghai, China  -  Bachelor of Science in Mechanical Engineering\n' in lines)
        self.assertTrue('Projects\n' in lines)
        self.assertTrue('Robockey, University of Pennsylvania, USA - Project member, designed 3 robots to play hockey in the rink, and finally we won the 6th place of all 24 teams.\n' in lines)
        self.assertTrue('PUMA Light Painting - Using MATLAB to solve the inverse kinematics of the puma robot and make it draw a picture that we wanted!\n' in lines)
        self.assertTrue('Courses\n' in lines)
        self.assertTrue('Programming Languages and Techniques,\n' in lines)
        self.assertTrue(' Feedback Control,\n' in lines)
        self.assertTrue(' Foundation of Engineering Math\n' in lines)
        
unittest.main()
