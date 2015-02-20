#author - Jian Li & Yike Chen

import unittest
from makeWebsite import *

class Test_makeWebsite(unittest.TestCase):
    
    def setUp(self):
        self.filename = 'resume.html'
        self.filename2 = 'my_test_for_HW5.txt'

    def test_isLetterLower(self):
        # input a lower case letter to see if it returns true
        letter = isLetterLower('x')
        self.assertEqual(True,letter)
        # input a number to see if it returns False
        letter2 = isLetterLower('1')
        self.assertEqual(False,letter2)
        # input a upper case letter to see if it returns false
        letter3 = isLetterLower('X')
        self.assertEqual(False,letter3)

    def test_isLetterUpper(self):
        # input a upper case letter to see if it returns true
        letter = isLetterUpper('X')
        self.assertEqual(True,letter)
        # input a number to see if it returns False
        letter2 = isLetterUpper('1')
        self.assertEqual(False,letter2)
        # input a lower case letter to see if it returns false
        letter3 = isLetterUpper('x')
        self.assertEqual(False,letter3)

    def test_name_detect(self):
        #input a normal line with name in it
        name = name_detect(['Jian Li ','Shanghai  Jiao Tong ',' UPenn '])
        self.assertEqual('Jian Li',name)
        name2 = name_detect(['Yike Chen ','Shanghai  Jiao Tong ',' UPenn '])
        self.assertEqual('Yike Chen',name2)

        #for the raises exception - if the first char is lower case or number
        self.assertRaises(NameError,name_detect,['jian Li','Shanghai Jiao Tong','UPenn'])
        self.assertRaises(NameError,name_detect,['2Jian Li','Shanghai Jiao Tong','UPenn'])
        self.assertRaises(NameError,name_detect,['yike Chen','Shanghai Jiao Tong','UPenn'])


    def test_email_detect(self):
        # test critical function
        emailAdd = email_detect(['Jian Li','lijian2@seas.upenn.edu','UPenn'])
        self.assertEqual(['lijian2@seas.upenn.edu'],emailAdd)
        emailAdd_plus = email_detect(['Jian Li','yikechen@seas.upenn.edu','UPenn'])
        self.assertEqual(['yikechen@seas.upenn.edu'],emailAdd_plus)
      
        #If there are '.COM' or '.EDU' in the address, there should be no element in the returning list
        emailAdd2 = email_detect(['Jian Li','lijian2@seas.upenn.EDU','UPenn'])
        emailAdd3 = email_detect(['Jian Li','jiandi_li@163.COM','UPenn'])
        self.assertEqual([],emailAdd2)
        self.assertEqual([],emailAdd3)

        #If there is no string begin with a normal lowercase between '@'and the ending--if there is a number or a upper case
        emailAdd4 = email_detect(['Jian Li','UPenn','jiandi_li@163.com'])
        self.assertEqual([],emailAdd4)
        emailAdd5 = email_detect(['Jian Li','UPenn','yikechen@SJTU.EDU.CN'])
        self.assertEqual([],emailAdd5)

        #If there are two email addresses in the list
        emailAdd6 = set(email_detect(['Jian Li','UPenn','lijian2@seas.upenn.edu','jiandi_li@gmail.com']))
        self.assertEqual(set(['lijian2@seas.upenn.edu','jiandi_li@gmail.com']),emailAdd6)
        emailAdd7 = set(email_detect(['Jian Li','UPenn','lijian2@seas.upenn.edu','jiandi_li@gmail.com','yikechen@seas.upenn.edu']))
        self.assertEqual(set(['lijian2@seas.upenn.edu','jiandi_li@gmail.com','yikechen@seas.upenn.edu']),emailAdd7)


    def test_course_detect(self):
        #easy cases:no punctions after the 'Courses'
        course1 = set(course_detect(['Jian Li','UPenn','SEAS','CoursesCIT590,Biomedical image analysis,Mechatronics\n','Sansom']))
        self.assertEqual(set(['CIT590','Biomedical image analysis','Mechatronics']),course1)
        course2 = set(course_detect(['Jian Li','UPenn','SEAS','Sansom','Courses Robotics,Biomedical image analysis,Mechatronics\n']))
        self.assertEqual(set(['Robotics','Biomedical image analysis','Mechatronics']),course2)    
        

        #If there are punctuations after the 'Courses',we should ignore the punctuations
        course3 = set(course_detect(['Jian Li','UPenn','SEAS','Courses:--:CIT590,Biomedical image analysis,Mechatronics\n','Sansom']))
        self.assertEqual(set(['CIT590','Biomedical image analysis','Mechatronics']),course3)
        course4 = set(course_detect(['Jian Li','UPenn','SEAS','Sansom','Courses,--::Robotics,Biomedical image analysis,Mechatronics\n']))
        self.assertEqual(set(['Robotics','Biomedical image analysis','Mechatronics']),course4)        


    def test_projects_detect(self):
        project1 = set(projects_detect(['Jian Li\n','lijian2@seas.upenn.edu','Projects\n','GRASP LAB\n','Robockey\n','-----------\n']))
        self.assertEqual(set(['GRASP LAB','Robockey']),project1)
        project2 = set(projects_detect(['Yike Chen\n','yikechen@seas.upenn.edu','Projects\n','Puma Light Painting\n','Robockey\n','-----------\n']))
        self.assertEqual(set(['Puma Light Painting','Robockey']),project2)
        
        #there is a blank line 
        project3 = set(projects_detect(['Jian Li\n','lijian2@seas.upenn.edu','Projects\n','GRASP LAB\n','\n','Robockey\n','-----------\n']))
        self.assertEqual(set(['GRASP LAB','Robockey']),project3)
        project4 = set(projects_detect(['Jian Li\n','lijian2@seas.upenn.edu','\n','Projects\n','GRASP LAB\n','Robockey\n','-----------\n']))
        self.assertEqual(set(['GRASP LAB','Robockey']),project4)

        #there are more than one blank line
        project5 = set(projects_detect(['Jian Li\n','lijian2@seas.upenn.edu','Projects\n','\n','GRASP LAB\n','\n','Robockey\n','-----------\n']))
        self.assertEqual(set(['GRASP LAB','Robockey']),project5)
        project6 = set(projects_detect(['Jian Li\n','\n','lijian2@seas.upenn.edu','Projects\n','\n','GRASP LAB\n','\n','Robockey\n','-----------\n']))
        self.assertEqual(set(['GRASP LAB','Robockey']),project6)

    def test_education_detect(self):
        # test critical function
        education1 = set(education_detect(['Jian Li','University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering\n','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering\n']))
        self.assertEqual(set(['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering']),education1)
        education2 = set(education_detect(['Yike Chen','University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering\n']))
        self.assertEqual(set(['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering']),education2)

        
        #If there is a blank line between these education information
        education3 = set(education_detect(['Jian Li','University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering\n','\n','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering\n']))
        self.assertEqual(set(['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering']),education3)
        education4 = set(education_detect(['Yike Chen','University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering\n','\n','University in China-Bachelor of Science in Mechanical Engineering']))
        self.assertEqual(set(['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering','University in China-Bachelor of Science in Mechanical Engineering']),education4)
        
        #If there is a project done in a university in the list, this should not be returned!
        education5 = set(education_detect(['Jian Li','robockey-university of pennsylvania','University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering\n','\n','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering\n']))
        self.assertEqual(set(['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering','Shanghai Jiao Tong University,Shanghai, China  -  Bachelor of Science in Mechanical Engineering']),education5)
        education6 = set(education_detect(['Yike Chen','robockey-university of pennsylvania','University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering\n','\n','University in China-Bachelor of Science in Mechanical Engineering']))
        self.assertEqual(set(['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engneering','University in China-Bachelor of Science in Mechanical Engineering']),education6)
        


    #The following are tests for writing part!
    def test_surround_block(self):
        htmlBlock1 = surround_block('div',['Jian Li'])
        self.assertEqual(['<','div','>\n','J','i','a','n',' ','L','i','\n</','div','>\n'],htmlBlock1)
        htmlBlock2 = surround_block('div',['Yike Chen'])
        self.assertEqual(['<','div','>\n','Y','i','k','e',' ','C','h','e','n','\n</','div','>\n'],htmlBlock2)

        #if there are more than one element in the argument list
        htmlBlock3 = surround_block('div',['Jian Li','UPenn'])
        self.assertEqual(['<','div','>\n','J','i','a','n',' ','L','i','U','P','e','n','n','\n</','div','>\n'],htmlBlock3)
        htmlBlock4 = surround_block('div',['Yike Chen','UPenn'])
        self.assertEqual(['<','div','>\n','Y','i','k','e',' ','C','h','e','n','U','P','e','n','n','\n</','div','>\n'],htmlBlock4)


    def test_initial_step_write(self):
        f_initial = open(self.filename2,'w')
        initial_step_write(f_initial)
        f_initial.close()
        f_initial_r = open(self.filename2)
        lines = f_initial_r.readlines()
        f_initial_r.close()
        self.assertTrue('<div id="page-wrap">\n' in lines)
        self.assertFalse('</div>\n' in lines)
        self.assertFalse('</body>\n' in lines)
        self.assertFalse('</html>\n' in lines)
        self.assertFalse('<div id="page-wrap">' in lines)
        
        


    def test_final_step_write(self):
        f_final = open(self.filename2,'w')
        final_step_write(f_final)
        f_final.close()
        f_final_r = open(self.filename2)
        lines = f_final_r.readlines()
        f_final_r.close()
        self.assertTrue('</div>\n' in lines)
        self.assertTrue('</body>\n' in lines)
        self.assertTrue('</html>\n' in lines)
        self.assertFalse('<div id="page-wrap">\n' in lines)
        self.assertFalse('</div>' in lines)
        self.assertFalse('</body>' in lines)
        self.assertFalse('</html>' in lines)


    def test_write_basic_info(self):
        f_basic = open(self.filename2,'w')
        write_basic_info(f_basic,'Jian Li',['lijian2@seas.upenn.edu'])
        f_basic.close()
        f_basic_r = open(self.filename2)
        lines = f_basic_r.readlines()
        f_basic_r.close()
        self.assertTrue('Jian Li\n' in lines)
        self.assertTrue('lijian2@seas.upenn.edu\n' in lines)
        #second test
        f_basic2 = open(self.filename2,'w')
        write_basic_info(f_basic2,'Yike Chen',['yikechen@seas.upenn.edu'])
        f_basic2.close()
        f_basic_r2 = open(self.filename2)
        lines = f_basic_r2.readlines()
        f_basic_r2.close()
        self.assertTrue('Yike Chen\n' in lines)
        self.assertTrue('yikechen@seas.upenn.edu\n' in lines)

    def test_write_education_info(self):
        f_education = open(self.filename2,'w')
        write_education_info(f_education,['University of Pennsylvania','Shanghai Jiao Tong University'])
        f_education.close()
        f_education_r = open(self.filename2)
        lines = f_education_r.readlines()
        f_education_r.close()
        self.assertTrue('Education\n' in lines)
        self.assertTrue('University of Pennsylvania\n' in lines)
        self.assertTrue('Shanghai Jiao Tong University\n' in lines)
        #second test
        f_education2 = open(self.filename2,'w')
        write_education_info(f_education2,['University of Pennsylvania','Cornell University'])
        f_education2.close()
        f_education_r2 = open(self.filename2)
        lines = f_education_r2.readlines()
        f_education_r2.close()
        self.assertTrue('Education\n' in lines)
        self.assertTrue('University of Pennsylvania\n' in lines)
        self.assertTrue('Cornell University\n' in lines)



    def test_write_project_info(self):
        f_project = open(self.filename2,'w')
        write_project_info(f_project,['Robockey','PUMA Light Painting'])
        f_project.close()
        f_project_r = open(self.filename2)
        lines = f_project_r.readlines()
        f_project_r.close()
        self.assertTrue('Projects\n' in lines)
        self.assertTrue('Robockey\n' in lines)
        self.assertTrue('PUMA Light Painting\n' in lines)
        #second test
        f_project2 = open(self.filename2,'w')
        write_project_info(f_project2,['Orchestra','PUMA'])
        f_project2.close()
        f_project_r2 = open(self.filename2)
        lines = f_project_r2.readlines()
        f_project_r2.close()
        self.assertTrue('Projects\n' in lines)
        self.assertTrue('Orchestra\n' in lines)
        self.assertTrue('PUMA\n' in lines)

        


    def test_write_course_info(self):
        f_course = open(self.filename2,'w')
        write_course_info(f_course,['CIT590','MEAM513','ENM510'])
        f_course.close()
        f_course_r = open(self.filename2)
        lines = f_course_r.readlines()
        f_course_r.close()
        self.assertTrue('Courses\n' in lines)
        self.assertTrue('CIT590,MEAM513,ENM510\n' in lines)
        #second test
        f_course2 = open(self.filename2,'w')
        write_course_info(f_course2,['Programming Languages and Techniques','Feedback Control','Foundation of Engineering Math'])
        f_course2.close()
        f_course_r2 = open(self.filename2)
        lines = f_course_r2.readlines()
        f_course_r2.close()
        self.assertTrue('Courses\n' in lines)
        self.assertTrue('Programming Languages and Techniques,Feedback Control,Foundation of Engineering Math\n' in lines)


    def test_resume_write(self):
        f_resume = open(self.filename2,'w')
        resume_write(f_resume,'Jian Li',['lijian2@seas.upenn.edu'],['Programming Languages and Techniques','Feedback Control','Foundation of Engineering Math'],['Robockey','PUMA Light Painting'],['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engineering'])
        f_resume.close()
        f_resume_r = open(self.filename2)
        lines = f_resume_r.readlines()
        f_resume_r.close()
        self.assertTrue('Jian Li\n' in lines)
        self.assertTrue('lijian2@seas.upenn.edu\n' in lines)
        self.assertTrue('Education\n' in lines)
        self.assertTrue('University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engineering\n' in lines)
        self.assertTrue('Projects\n' in lines)
        self.assertTrue('Robockey\n' in lines)
        self.assertTrue('PUMA Light Painting\n' in lines)
        self.assertTrue('Courses\n' in lines)
        self.assertTrue('Programming Languages and Techniques,Feedback Control,Foundation of Engineering Math\n' in lines)
        #second test
        f_resume2 = open(self.filename2,'w')
        resume_write(f_resume2,'Yike Chen',['yikechen@seas.upenn.edu'],['Programming Languages and Techniques','IPD'],['Robockey','PUMA Light Painting'],['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engineering'])
        f_resume2.close()
        f_resume_r2 = open(self.filename2)
        lines = f_resume_r2.readlines()
        f_resume_r2.close()
        self.assertTrue('Yike Chen\n' in lines)
        self.assertTrue('yikechen@seas.upenn.edu\n' in lines)
        self.assertTrue('Education\n' in lines)
        self.assertTrue('University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Engineering\n' in lines)
        self.assertTrue('Projects\n' in lines)
        self.assertTrue('Robockey\n' in lines)
        self.assertTrue('PUMA Light Painting\n' in lines)
        self.assertTrue('Courses\n' in lines)
        self.assertTrue('Programming Languages and Techniques,IPD\n' in lines)
        
        
unittest.main()
