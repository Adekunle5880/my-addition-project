num1 = 2
num2 = 5
num3 = 10

if num1 > num2 and num2 < num3:
    print('num1 is greater!')
     
else:
    print('num2 is greater!')

class computer:
    def __init__(self, manufacturer, price, mfd):
        sele.manufacturer = manufacturer
        self.price = price
        self.mfd = mfd

    def show_price(self):
        print(self.price)



class Laptop(computer, electronics):
    def __init__(self, name, colour, ram, hdd):
        self.name = name
        self.colour = colour
        self.ram = ram
        self.hdd = hdd
            
    def switch_on(self):
        print('turning on the laptop')

    def properties(self):
        print(self.name, self.colour, self.ram, self.hdd)

laptop1 = laptop('lenovo', 'black', '4gb', '500gb')
laptop2 = laptop('hp', 'silver', '2gb', '1000gb')
