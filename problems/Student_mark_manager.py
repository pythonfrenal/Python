





class student:
   def __init__ (self):
      self.mark=[]

   def add_marks(self,mark):
      self.mark.append(mark)

   def calculate_average(self):
      return sum(self.mark) / len(self.mark)
   
   def result(self):
      average=self.calculate_average()
      print("Average marks:", average)


      if average >=50:
         print("pass")
      else:
         print("Fail")

marks = [55,85,25,68]
student=student()

for mark in marks:
   student.add_marks(mark)

student.result()


   

   
      
      
      
