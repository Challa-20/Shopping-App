#puneeth kumar's part- file handling, listing the data of phone models and features, printing details and displaying photos of phones under the input range, exception handling
#challa sruthi's part- defining functions for the mainMenu, error handling, excpetion handling, loops, lists
#shruti parmar's part- makePayment function, dictionary, list error handling, loops


from PIL import Image                                                                                 #imports module to process images of mobile phones

print("""Hello welcome to the samsung mobile shopping zone
We have the new collection of the samsung mobiles
at what range of costs would you like to choose sir/madam? """)                                       #opening welcome message of the website gets printed  

cost = int(input("Under: "))                                                                           #takes input of budget from the user for displaying phones under that price range
print()

                                                                                                      #mobiles and their features listed acoording to costs in a list called 'item'
item = ['m11','m02s','A12','m12','m31','m31s','m51','m42','f62','A9','note10_lite','A72']              
# under 10k

m11 = ["4GB ram, 64GB storage, Android 10 operating system, Black colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 5000mAh, Cellular technology 4G,"
      "Front camera single 8MP(F2.0), Back camera triple 13MP(F1.8)+5MP(F2.2)+2MP(F2.4)"
      "Qualcomm SDM450-F01 processor octa core,infinity o display,",
      "Price ₹9,999"]

m02s = ["4GB ram, 64GB storage, Android 10 operating system, Black colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 5000mAh, Cellular technology 4G,"
      "Front camera single 5MP(F2.2), Back camera triple 13MP(F2.2)+2MP(F2.4)+2MP(F2.4)"
      "qualcomm SDM450 processor octa core, TFT-LCD infinity v cut display,",
      "Price ₹9,999"]

#under15k

A12 = ["4GB ram, 64GB storage, Android 10 operating system, Blue colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 5000mAh, Cellular technology 4G,"
      "Front camera single 8MP(F2.2), Back camera quad 48MP(F1.8)+5MP(F2.2)+2MP(F2.4)+2MP(F2.4)"
      "MTK6765(G35) processor octa core, HD+TFT infinity v cut display,",
      "Price ₹12,999"]

m12 = ["4GB ram, 64GB storage, Android 11 operating system, Blue colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 6000mAh, Cellular technology 4G,"
      "Front camera single 8MP(F2.2), Back camera quad 48MP(F2.0)+5MP(F2.2)+2MP(F2.4)+2MP(F2.4)"
      "exynos850 processor octa core, TFT-LCD infinity v cut display,",
      "Price ₹10,999"]

#under20k

m31 = ["8GB ram, 128GB storage, Android 10 operating system, Blue colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 6000mAh, Cellular technology 4G,"
      "Front camera single 32MP(F2.0), Back camera quad 64MP(F1.8)+8MP(F2.2)+5MP(F2.2)+5MP(F2.4)"
      "exynos9611 processor octa core, super Amoled infinity U cut display,",
      "Price ₹16,999"]

m31s = ["8GB ram, 128GB storage, Android 10 operating system, Blue colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 6000mAh, Cellular technology 4G,"
      "Front camera single 32MP(F2.2), Back camera quad 64MP(F1.8)+12MP(F2.2)+5MP(F2.4)+5MP(F2.4)"
      "exynos9611 processor octa core, super Amoled infinity O display,",
      "Price ₹18,999"]

#under25k

m51 = ["6GB ram, 128GB storage, Android 10 operating system, Blue colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 7000mAh, Cellular technology 4G,"
      "Front camera single 32MP(F2.2), Back camera quad 64MP(F1.8)+12MP(F2.2)+5MP(F2.4)+5MP(F2.4)"
      "qualcomm SD730G processor octa core, super Amoled plus infinity O display,",
      "Price ₹20,999"]

m42 = ["8GB ram, 128GB storage, Android 11 operating system, Black colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 5000mAh, Cellular technology 5G,"
      "Front camera single 20MP(F2.2), Back camera quad 48MP(F1.8)+8MP(F2.2)+5MP(F2.4)+5MP(F2.4)"
      "qualcomm SDM750G processor octa core, super Amoled infinity U cut display,",
      "Price ₹23,999"]

#under30k

f62 = ["8GB ram, 128GB storage, Android 10 operating system, Blue colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 7000mAh, Cellular technology 4G,"
      "Front camera single 32MP(F2.0), Back camera quad 64MP(F1.8)+12MP(F2.2)+5MP(F2.2)+5MP(F2.4)"
      "exynos9825 processor octa core, super Amoled infinity O display,",
      "Price ₹25,396"]

A9 = ["8GB ram, 128GB storage, Android 8 operating system, Black colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 3800mAh, Cellular technology 4G,"
      "Front camera single 24MP optical zoom upto 2x, Back camera quad 24MP+5MP+10MP+8MP auto focus, digital zoom upto 10x"
      "qualcomm SDM660 processor octa core, super Amoled display,",
      "Price ₹28,955"]

#under35k

note10_lite = ["6GB ram, 128GB storage, Android 10 operating system, Black colour, 16.4cm height,"
      "Lithium-ion battery, battery capacity 4500mAh, Cellular technology 4G,"
      "Front camera single 32MP(F2.0), Back camera triple 12MP(F2.2)+12MP(F1.7)AF Dual pixel +12MP(F2.4) OIS 2x zoom, S pen"
      "exynos9810 processor octa core, super Amoled infinity O display,",
      "Price ₹31,999"]

#under40k

A72 = ["8GB ram, 256GB storage, Android 11 operating system, Blue colour, 16.5cm height,"
      "Lithium-ion battery, battery capacity 5000mAh, Cellular technology 4G,"
      "Front camera single 32MP(F2.2), Back camera quad 64MP(F1.8)OIS AF(F1.8)+12MP(F2.2)+8MP(F2.4)AT Tele 3x+5MP(F2.4)"
      "SMD720G processor octa core, super Amoled plus infinity o display 90Hz refresh rate,",
      "Price ₹37,999"]




price_item = {'m02s':9999, 'm12':10999, 'm11':9999,                
              'A12':12999, 'm31':16999, 'm31s':18999,
              'm51':20999, 'm42':23999, 'f62':25396,
              'A9':28955, 'note10_lite':31999, 'A72':37999}                                                  #using a dictionary to assign prices to a particular mobile phone model




if (8500<= cost <= 10000):                                                                                   #using if else conditions to print the name, price and details and to
  print("The available options and their features are:")                                                     #display the pictures of the mobile phone models according to the 
  print("m11:",m11)                                                                                          #price range input given by the user.
  print(price_item['m11'])                                                                                   #here, the dictionary which was used to assign prices is used  
  try :                                                                                                      
    img = Image.open(r"m11.JPEG")                                                                            #the error handling has been used here to prevent the code from stopping 
    img.show()                                                                                               #in case the image does not open
  except IOError :
    pass
  print("m02s:",m02s)
  print(price_item['m02s'])
  try :
    img = Image.open(r"m02s.JPEG")
    img.show()
  except IOError :
    pass
elif 10000 < cost <= 15000:
  print("The available options and their features are:")
  print("m11:",m11)                                                                                          
  print(price_item['m11'])                                                                                  
  try :                                                                                                      
    img = Image.open(r"m11.JPEG")                                                                            
    img.show()                                                                                               
  except IOError :
    pass
  print("m02s:",m02s)
  print(price_item['m02s'])
  try :
    img = Image.open(r"m02s.JPEG")
    img.show()
  except IOError :
    pass
  print("A12:",A12)
  print(price_item['A12'])
  try :
    img = Image.open(r"A12.JPEG")
    img.show()
  except IOError :
    pass
  print("m12:",m12)
  print(price_item['m12'])
  try :
    img = Image.open(r"m12.JPEG")
    img.show()
  except IOError :
    pass
elif 15000 < cost <= 20000:
  print("The available options and their features are:")
  print("m11:",m11)                                                                                          
  print(price_item['m11'])                                                                                  
  try :                                                                                                      
    img = Image.open(r"m11.JPEG")                                                                            
    img.show()                                                                                               
  except IOError :
    pass
  print("m02s:",m02s)
  print(price_item['m02s'])
  try :
    img = Image.open(r"m02s.JPEG")
    img.show()
  except IOError :
    pass
  print("A12:",A12)
  print(price_item['A12'])
  try :
    img = Image.open(r"A12.JPEG")
    img.show()
  except IOError :
    pass
  print("m12:",m12)
  print(price_item['m12'])
  try :
    img = Image.open(r"m12.JPEG")
    img.show()
  except IOError :
    pass
  print("m31:",m31)
  print(price_item['m31'])
  try :
    img = Image.open(r"m31.JPEG")
    img.show()
  except IOError :
    pass
  print("m31s:",m31s)
  print(price_item['m31s'])
  try :
    img = Image.open(r"m31s.JPEG")
    img.show()
  except IOError :
    pass
elif 20000< cost <= 25000:
  print("The available options and their features are:")
  print("m11:",m11)                                                                                          
  print(price_item['m11'])                                                                                  
  try :                                                                                                      
    img = Image.open(r"m11.JPEG")                                                                            
    img.show()                                                                                               
  except IOError :
    pass
  print("m02s:",m02s)
  print(price_item['m02s'])
  try :
    img = Image.open(r"m02s.JPEG")
    img.show()
  except IOError :
    pass
  print("A12:",A12)
  print(price_item['A12'])
  try :
    img = Image.open(r"A12.JPEG")
    img.show()
  except IOError :
    pass
  print("m12:",m12)
  print(price_item['m12'])
  try :
    img = Image.open(r"m12.JPEG")
    img.show()
  except IOError :
    pass
  print("m31:",m31)
  print(price_item['m31'])
  try :
    img = Image.open(r"m31.JPEG")
    img.show()
  except IOError :
    pass
  print("m31s:",m31s)
  print(price_item['m31s'])
  try :
    img = Image.open(r"m31s.JPEG")
    img.show()
  except IOError :
    pass
  print("m51:",m51)
  print(price_item['m51'])
  try :
    img = Image.open(r"m51.JPEG")
    img.show()
  except IOError :
    pass
  print("m42:",m42)
  print(price_item['m42'])
  try :
    img = Image.open(r"m42.JPEG")
    img.show()
  except IOError :
    pass

elif 25000< cost <= 30000:
  print("The available options and their features are:")
  
  print("m11:",m11)                                                                                          
  print(price_item['m11'])                                                                                  
  try :                                                                                                      
    img = Image.open(r"m11.JPEG")                                                                            
    img.show()                                                                                               
  except IOError :
    pass
  print("m02s:",m02s)
  print(price_item['m02s'])
  try :
    img = Image.open(r"m02s.JPEG")
    img.show()
  except IOError :
    pass
  print("A12:",A12)
  print(price_item['A12'])
  try :
    img = Image.open(r"A12.JPEG")
    img.show()
  except IOError :
    pass
  print("m12:",m12)
  print(price_item['m12'])
  try :
    img = Image.open(r"m12.JPEG")
    img.show()
  except IOError :
    pass
  print("m31:",m31)
  print(price_item['m31'])
  try :
    img = Image.open(r"m31.JPEG")
    img.show()
  except IOError :
    pass
  print("m31s:",m31s)
  print(price_item['m31s'])
  try :
    img = Image.open(r"m31s.JPEG")
    img.show()
  except IOError :
    pass
  print("m51:",m51)
  print(price_item['m51'])
  try :
    img = Image.open(r"m51.JPEG")
    img.show()
  except IOError :
    pass
  print("m42:",m42)
  print(price_item['m42'])
  try :
    img = Image.open(r"m42.JPEG")
    img.show()
  except IOError :
    pass
  print("f62:",f62)
  print(price_item['f62'])
  try :
    img = Image.open(r"f62.JPEG")
    img.show()
  except IOError :
    pass
  print("A9:", A9)
  print(price_item['A9'])
  try :
    img = Image.open(r"A9.JPEG")
    img.show()
  except IOError :
    pass
elif 30000 < cost <= 35000:
  print("The available options and their features are:")
  print("m11:",m11)                                                                                          
  print(price_item['m11'])                                                                                  
  try :                                                                                                      
    img = Image.open(r"m11.JPEG")                                                                            
    img.show()                                                                                               
  except IOError :
    pass
  print("m02s:",m02s)
  print(price_item['m02s'])
  try :
    img = Image.open(r"m02s.JPEG")
    img.show()
  except IOError :
    pass
  print("A12:",A12)
  print(price_item['A12'])
  try :
    img = Image.open(r"A12.JPEG")
    img.show()
  except IOError :
    pass
  print("m12:",m12)
  print(price_item['m12'])
  try :
    img = Image.open(r"m12.JPEG")
    img.show()
  except IOError :
    pass
  print("m31:",m31)
  print(price_item['m31'])
  try :
    img = Image.open(r"m31.JPEG")
    img.show()
  except IOError :
    pass
  print("m31s:",m31s)
  print(price_item['m31s'])
  try :
    img = Image.open(r"m31s.JPEG")
    img.show()
  except IOError :
    pass
  print("m51:",m51)
  print(price_item['m51'])
  try :
    img = Image.open(r"m51.JPEG")
    img.show()
  except IOError :
    pass
  print("m42:",m42)
  print(price_item['m42'])
  try :
    img = Image.open(r"m42.JPEG")
    img.show()
  except IOError :
    pass
  print("f62:",f62)
  print(price_item['f62'])
  try :
    img = Image.open(r"f62.JPEG")
    img.show()
  except IOError :
    pass
  print("A9:", A9)
  print(price_item['A9'])
  try :
    img = Image.open(r"A9.JPEG")
    img.show()
  except IOError :
    pass
  print("note10_lite:",note10_lite)
  print(price_item['note10_lite'])
  try :
    img = Image.open(r"note10_lite.JPEG")
    img.show()
  except IOError :
    pass
  
elif 35000< cost:
  print("The available options and their features are:")
  print("m11:",m11)                                                                                          
  print(price_item['m11'])                                                                                  
  try :                                                                                                      
    img = Image.open(r"m11.JPEG")                                                                            
    img.show()                                                                                               
  except IOError :
    pass
  print("m02s:",m02s)
  print(price_item['m02s'])
  try :
    img = Image.open(r"m02s.JPEG")
    img.show()
  except IOError :
    pass
  print("A12:",A12)
  print(price_item['A12'])
  try :
    img = Image.open(r"A12.JPEG")
    img.show()
  except IOError :
    pass
  print("m12:",m12)
  print(price_item['m12'])
  try :
    img = Image.open(r"m12.JPEG")
    img.show()
  except IOError :
    pass
  print("m31:",m31)
  print(price_item['m31'])
  try :
    img = Image.open(r"m31.JPEG")
    img.show()
  except IOError :
    pass
  print("m31s:",m31s)
  print(price_item['m31s'])
  try :
    img = Image.open(r"m31s.JPEG")
    img.show()
  except IOError :
    pass
  print("m51:",m51)
  print(price_item['m51'])
  try :
    img = Image.open(r"m51.JPEG")
    img.show()
  except IOError :
    pass
  print("m42:",m42)
  print(price_item['m42'])
  try :
    img = Image.open(r"m42.JPEG")
    img.show()
  except IOError :
    pass
  print("f62:",f62)
  print(price_item['f62'])
  try :
    img = Image.open(r"f62.JPEG")
    img.show()
  except IOError :
    pass
  print("A9:", A9)
  print(price_item['A9'])
  try :
    img = Image.open(r"A9.JPEG")
    img.show()
  except IOError :
    pass
  print("note10_lite:",note10_lite)
  print(price_item['note10_lite'])
  try :
    img = Image.open(r"note10_lite.JPEG")
    img.show()
  except IOError :
    pass
  print("A72:",A72)
  print(price_item['A72'])
  try :
    img = Image.open(r"A72.JPEG")
    img.show()
  except IOError :
    pass
elif cost<=0:                                                                                           #these last three elif else blocks are used as exception handling
  print("Please enter a valid price range")                                                             #so that the printed message does not sound absurb for any invalid input cases
elif 0<=cost<=999:
  print("Real mobiles do not cost that less.\nPlease enter a higher price range")
else:
  print("sorry we do not have any mobile phone models at that range.\n9999 is the staring range.")                                       







shopping_list = []                                                                                 #making empty lists to append later on
bill = []

def mainMenu():                                                                                    #function for main menu: 
  while True:                                                                                      #when called, displays the options that the user can choose from

    print()
    print(''' Select a option that you would like to do from the following:

    1. view shopping list 
    2. Add item to the shopping list
    3. Remove item from shopping list
    4. Check if item is on the shopping list
    5. How many items on the shopping list
    6. Clear the shopping list
    7. To make payment
    8. To exit
    ''')

    selection = input("Make your selection: ")                                                     #the input number calls the respective function
    print()

    if selection == '1':
      print("m11, m02s, A12, m12, m31, m31s, m51, m42, f62, A9, note10_lite, A72")
      displaylist()
    elif selection == '2':
      addItem()
    elif selection == '3':
      removeItem()
    elif selection == '4':
      checkItem()
    elif selection == '5':
      listlength()
    elif selection == '6':
      clearlist()
    elif selection == '7':
      makepayment()
    elif selection == '8':
      print("Thank You!\nHoping to see you here again")
      break
    else:
      print("*Give a proper selection*")


def displaylist():                                                                                  #functions for each of the main menu options that the user can select
  print()
  print("***Shopping List***")
  for i in shopping_list:
    print(i)

def addItem():
  obj = input("Enter an item that you would like to add to your shopping list: ")
  if obj in item:
    shopping_list.append(obj)
    bill.append(price_item[obj])                                                                      #appends the item from the item list to shopping list according to the input given
    print('*' + obj + " has been added to your shopping list" + '*')                               
  else:
    print("Sorry, we do not have that item")                                                       #if the item is not there in the item list, this message will be printed
def removeItem():
  obj = input("Enter an item from the list you would like to remove: ")
  if obj in shopping_list:
    shopping_list.remove(obj)                                                                      #to remove an item from the previously appended shopping list
    print('*' + obj + " is removed from your shopping list" + '*')                           
  else: 
    print("You don't have this in your shopping list")                                           #to avoid the error if user tries removing something that they don't have in list

def checkItem():
  obj = input("Enter the item you would like to check: ")                                         #to check if the user has a particular item in the shopping list
  if obj in shopping_list:
    print('*Yes, ' + obj + ' is on the shopping list*')
  else:
    print('*No, ' + obj + ' is not on the shopping list*')
  print("Your shopping list:", shopping_list)
def listlength():
  if len(shopping_list) == 0:
    print("Your shopping list is empty")                                                          #to check the number of items on the list
  if len(shopping_list) == '1':
    print("*There is", len(shopping_list),"item on the shopping list*")
  else:
    print("*There are", len(shopping_list), "items on the shopping list*")
  print("Your shopping list:", shopping_list)

def clearlist():                                                                                  #to clear the shopping list
  shopping_list.clear()
  print("*The shopping list has been cleared*")

def makepayment():
  for obj in shopping_list:                                                                         #three major payment methods used on online shoopping websites
    bill = price_item[obj]
    print ("your bill is: ", bill)
    payMethod = int(input("Enter 1 for EMI payment, 2 for Card payment and 3 for cash or cheque"))
    while True:
      if payMethod == 1:
        x = int(input("In how many installments would you like to pay?"))
        print("Each of your installments will cost", round((bill+0.05*bill)/x))
        print("EMI method is only available for online payments")
        break
      elif payMethod == 2:
        y = int(input("Enter your card details: "))
        print ('You have successfully paid by card')
        break
      elif payMethod == 3:
        print("you have successfully paid the cash")
        break
      else:
        print("please choose a number in 1, 2 and 3")
        return payMethod
        break


mainMenu()                                                                        #calling the main menu function which gives us option to input and call any function of our choice
