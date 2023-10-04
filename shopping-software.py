class shoppingSoftware():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def outputList(self):
        print("Name of commodity:",self.name)
        print("Pice:",self.price,"naira")
        print("Quantity:",self.quantity)
        self.totalcost = int(self.price) * int(self.quantity)
        print("Total cost:",self.totalcost,"naira")

    def computeTSA(self):
        global tsa
        tsa += self.totalcost

    def outputTSA(self):
        global tsa
        print("Total Shopping Amount is:",tsa,"naira")

i = 1
tsa = 0
for i in range(1, 3):
    name = input("Enter the name of the commodity: ")
    price = input("Enter the price of the commodity: ")
    quantity = input("Enter the quantity of the commodity: ")
    good1 = shoppingSoftware(name, price, quantity)
    good1.outputList()
    good1.computeTSA()

good1.outputTSA()