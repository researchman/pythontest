'''
class people:
    name = "";
    age = 0;
    weight = 0.0
    def __init__(self,name,age,weight):
        self.name = name;
        self.age = age;
        self.weight = weight;
    
    def speak(self):
        print("my name is %s,my age is %d,my weight is %.3fkg"%(self.name,self.age,self.weight));

class student(people):
    grade = 0;
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w);
        self.grade = g;

    def speak(self):
        print("my name is %s,my age is %d,my grade is %d"%(self.name,self.age,self.grade));


p = people("brandon",34,61.2);
p.speak();

s = student("jack",16,40.5,6);
s.speak();
'''

'''
import glob;
print(glob.glob("*.py"));
'''

from datetime import date;
now = date.today();
birthday = date(1983,9,11);
age = now - birthday;
print(age.days);
#print(age._day);
#print(age.year);

