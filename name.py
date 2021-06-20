class Mark:
    def __init__(self,name1,name2,name3):
        self.name1=str(input("enter 1:"))
        self.name2=str(input("enter 2:"))
        self.name3=str(input("enter 3:"))
    def naming(self):
        print("Hello ",self.name1)
        print("Bye ",self.name2)
        print("Good morning ",self.name3)

p=Mark("","","")
p.naming()
