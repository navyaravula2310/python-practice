class itemType:
    def read(self):
        self.name = str(input("Enter name : "))
        self.deposit = int(input("Enter deposit : "))
        self.cost = int(input("Enter cost per day : "))
    def display(self):
        print(self.name , self.deposit , self.cost)
        
depositor1 = itemType()
depositor1.read()
print("Depositor1 details")
depositor1.display()