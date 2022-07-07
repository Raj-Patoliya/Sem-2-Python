#Student Class 
class Student:
    def __init__(self,id,name,marks1,marks2,marks3):
      self.id = id
      self.name = name
      self.marks1 = marks1
      self.marks2 = marks2
      self.marks3 = marks3
    def display(self):
      print("\n\tId : ",self.id)
      print("\n\tName : ",self.name)
      print("\n\tMarks 1 : ",self.marks1)
      print("\n\tMarks 2 : ",self.marks2)
      print("\n\tMarks 3 : ",self.marks3)