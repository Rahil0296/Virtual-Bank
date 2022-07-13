import pandas 

print('\t\t\t\tWelcome to KJ Bank! ')

Bank = { }   #dict

#Creating a class BankAccount 

class BankAccount():
    def password(self):

        #Entering passsword and checking its strength

        import re
        print('''\n\nENTER A PASSWORD FOR YOUR ACCOUNT;
        Conditions:
1.Minimum 8 characters maximum 15 characters.
2.The alphabets must be between [a-z]
3.At least one alphabet should be of Upper Case [A-Z]
4.At least 1 number or digit between [0-9].
5.At least 1 character from [ _ or @ or $ or & or #].''')
        print("\nFor example-acSd@32q")

        while True:
           password_i = input('\n\nCreate password ')
           i = password_i
           lowercase_letter = re.search('[a-z]', i)
           uppercase_letter = re.search('[A-Z]', i)
           number = re.search('[0-9]', i)
           special = re.search('[@,#,$]', i)
           
           #using re to check strength of password

           if lowercase_letter and uppercase_letter and number and special:

               if len(i) in range(8, 15):

                   self.password_final = i
                   print('Congratulations! This has been set as your password ')
                   break

               else:
                   print('Error! Password is not long enough')
                   continue

        print(self.password_final)
        return self.password_final


    def details(self):
        #Asking for age and generating debit card number
        #Once the number has been generated,the holder name and the corresponding number is added to the dictionary Bank

        Name = input('Please Enter your name: ')
        age = int(input('Please Enter your age: '))
        if age>= 18:
            print('\nYou are eligible to have a bank account! ')
            import random
            #using random to generate debit card number
            id = random.randint(1000, 9999)
            debit = '4896 7505 5500 ' + str(id)
            self.debit = debit
            print('\nYour Debit card number is ', debit)
            print('''\nPlease Use this number to make payments from savings account.
Also enter password till it is approved.''')
            return debit
        else:
            print('\nSorry. You are too young to have an individual account! ')

    
    #Asking for initial deposit amount    
    def Balance(self):
        balance = int(input('\nPlease Enter initial deposit Rs'))
        return balance
    
    #Generating a random credit card number
    def Credit_Card(self):
        import random
         #using random to generate credit card number
        parts = []
        part1 = random.randint(4000, 5000)
        parts.append(part1)

        for part in range(0, 3):
            part = random.randint(1000, 10000)
            parts.append(part)

        card_num = (' '.join([str(part) for part in parts]))

        print('\n\tYour Credit card number is: ' ,card_num)
        self.cardno = card_num
        return card_num

person = BankAccount()
person.details()

#Shopping
def shopping(cred,p):
    import pandas
    initialdeposit = person.Balance()

    print("\n\n\t\t\t$$$$$$$$$$$$   SHOPPING BASKET   $$$$$$$$$$$$$$$$$$")

    print('''\nTo shop enter the (number) corresponding to 
the item you would like to purchase 
and type (end) to stop shopping''')

                   #using pandas to generate table of shopping list

    print("*********************************")
    data = [(1, 'Pulses','Rs 1000'),
    (2, 'Flour','Rs 800'),
    (3, 'Shirt','Rs 5000'),
    (4,'Pant','Rs 5000'),
    (5, 'Coat',' Rs 8000'),
    (6, 'Laptop','Rs 40000'),
    (7, 'TV','Rs 30000'),
    (8, 'Speaker','Rs 5000'),
    (9, 'Mobile','Rs 20000'),
    (10, 'Headphones','Rs 1500')]
    df=pandas.DataFrame(data,columns=["Number", "Item", "Price"])
    print(df)
    print("**********************************")

    inventory = {"1": 1000, "2": 800, "3": 5000, "4": 5000, "5": 8000, "6": 40000, "7": 30000, "8": 5000, "9": 20000,
                 "10": 1500}

    basket = []
    total = []
    shop_item = input("What do you want to purchase??--")
    while shop_item != "end":
        if shop_item in inventory:
            basket.append(shop_item)
            shop_item = input("Anything else???--If not then type end...")
        else:
            print("We dont sell this item! Sorry!")
            break
    for i in basket:
        total.append(inventory[i])
    billamount = sum(total)

    #Payment by either credit or debit card
    n = int(input("\nEnter by which card you would like to pay--Credit(1) /Debit(2)--"))
    if n == 1:
      if cred!=0:
          while True:
              credit_card = input('\nEnter your credit card number: ')

              if credit_card == person.cardno:
                  Creditamount = billamount
                  break

              else:
                  print('\nPlease enter correct credit card number: ')
                  continue

          while True:
              password_check = input('\nEnter your password: ')

              if password_check == person.password_final:

                  print("\n\nYour bill is Rs ", billamount)
                  return Creditamount
              else:
                  print('Incorrect password')
                  continue

      elif cred == 0:
          #if you dont have a credit card and want to pay by credit card,you will be directed to pay with debit card instead
          print('You do not have a credit card with our bank so we will proceed with transaction from your debit account ')
          while True:
              debit_no = input('Enter your debit card number to make transaction: ')
              if debit_no == person.debit:
                  if billamount > initialdeposit:
                      print("Transaction cannot be done")
                  else:
                      balance = initialdeposit - billamount
                      print("The amount to be paid is Rs", billamount)
                      print("Your remaining balance is Rs", balance)
                      print("Thank you for shopping!!!")
                      return 0
                  break

              else:
                  print('Entered debit card number is invalid ')
                  continue

      while True:
          #payment using credit card
          credit_card = input('Enter credit card number: ')

          if credit_card == person.cardno:
              Creditamount = billamount
              break

          else:
              print('Please enter correct credit card number: ')
              continue

      while True:
          password_check = input('\nEnter your password: ')

          if password_check == person.password_final:

              print("\n\nYour bill is Rs ", billamount)
              return Creditamount
          else:
              print('Incorrect password!')
              continue
    else:

      while True:
          #payment using debit card
          debit_no = input('Enter your debit card number to make transaction: ')
          if debit_no == person.debit:
              if billamount > initialdeposit:
                  print("Transaction cannot be done!")
              else:
                  balance = initialdeposit - billamount
                  print("\nThe amount to be paid is Rs", billamount)
                  print("\nThe balance is Rs", balance)
                  print("\nThanks for shopping!!!")
                  return 0
              break

          else:
              print('Entered debit card number is invalid! ')
              continue

choice = input('\n\nDo you want a credit card? Enter(yes/no)--')
if choice.lower() == 'yes' :
    m = person.Credit_Card()
    n = person.password()
    t = shopping(m, n)

else:
    n = person.password()
    shopping(0,n)
