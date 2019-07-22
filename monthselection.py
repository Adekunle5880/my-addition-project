# create a dictionary of months
months = {'january':31,
         'february':28,
         'march':31,
         'april':30,
         'may':31,
         'june':30,
         'july':31,
         'august':31,
         'september':30,
         'october':31,
         'november':30,
         'december':31,}

#create a function called 'month28' that returns the name of the month with 28 days
#do the same for month30
#do the same for month31
def month31(month):
    value = [key for key, value in months.items() if value ==31]
    return value
print(month31(months))

def month30(month):
    value = [key for key, value in months.items() if value == 30]
    return value
print (month30(months))

def month28(month):
    value = [key for key, value in months.items() if value == 28]
    return value
print(month28(months))
     
