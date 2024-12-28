#initiate a class
class employee:
    #special method/magic method/dunder method
    def __init__(self):
        #Yeh object bante hi call ho jaayega(matlab iske andar ka saara data turant call hoga object bante hi, yeh speciality hai constructor ki...yeh baat khaas isliye hai kyun ki real world mei kuchh cheezein aisi hoti hain jo tum chahte ho ki software open hote hi apne aap ho jaayein jaise ki instagram open karte hi uske database se connect ho jaaye app, to yeh sab cheezein constructor ke andar hi define kari jaati hain)
        self.id=1
        self.salary=120000
        self.designation="Data Scientist"  
    def travel(self,destination):
        #Yeh apne aap call nahin hoga
        print(f"Employee is now travelling to {destination}")


#Creating an object/instance of the class
aman=employee()
print(aman.salary)
aman.travel("Agra")