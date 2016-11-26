# -*- coding: utf-8 -*-
# Created on <add the date here>
# For use in Scientific Python course
# Topic: objects
# @author: <add your name here>
# @organisation: IMPACS, Aberystwyth University

"""
Script for exercises on objects
"""

import university

def main():
    department = university.Department("Computer Science")
    student1 = university.Student("Artur", "Kobieta", 12, 120,2.50)
    student2 = university.Student("Kuba", "Chlopiec", 13, 135,3.00)
    student3 = university.Student("Kondziu", "Kobieta", 72, 156,1.00)
    student4 = university.Student("Dalia","Woman",20,170,5.00)
    
    department.students.append(student1)
    department.students.append(student2)
    department.students.append(student3)
    department.students.append(student4)
    
    print (department.name)
    department.list_students()
    pfact = university.PeopleFactory()
    random_people = pfact.generate_random_people(10,university.Person)
    print(random_people)
    personal_statistic = university.PersonalStatistics(random_people)
    personal_statistic.report()
    
    
    sfact = university.PeopleFactory()
    random_people2 = sfact.generate_random_people(10,university.Person)
    personal_statistic2 = university.PersonalStatistics(random_people2)
    personal_statistic2.report()
    
    
    random_people_evry = sfact.generate_random_people(300,cls=university.Person)
     
    department.students.append(random_people_evry)   
    department.list_students()
    
if __name__ == "__main__":
    main()



