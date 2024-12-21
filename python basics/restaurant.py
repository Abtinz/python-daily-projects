class restaurant() :
  def __init__(self,name,lastname,addres,phoneNumber,role) :
      self.name=name
      self.lastname=lastname
      self.addres=addres
      self.phone=phoneNumber
      self.role=role

  def printInfo(self):
      print("--------------------------------")
      print("Personal information")
      print(f"NAME : {self.name}")
      print(f"Lastname : {self.lastname}")
      print(f"Addres : {self.addres}")
      print(f"Phone : {self.phone}")
      print(f"Role : {self.role}")

class Customer(restaurant) :
     def __init__(self, name, lastname, addres, phoneNumber, role,order,takingout):
         super().__init__(name, lastname, addres, phoneNumber, role)
         self.order=order
         self.takingout=takingout

     def printCustomer(self) :
       super().printInfo()
       print("--------------------------------")
       print(f"Order Name : {self.order}")
       print("Order status :", end=" ")
       if self.takingout == 1 : print("taking out") 
       else : print("serving in restaurant")
       print("--------------------------------")

class supplier(restaurant):
    def __init__(self, name, lastname, addres, phoneNumber, role,barcode,product,brand):
         super().__init__(name, lastname, addres, phoneNumber, role)
         self.barcode=barcode
         self.product=product
         self.brand=brand

    def printSup(self) :
       super().printInfo()
       print("--------------------------------")
       print(f"Product Name : {self.product}")
       print(f"Product Barcode : {self.barcode}")
       print(f"Company : {self.brand}")
       print("--------------------------------")
    
class Representation(restaurant):
    def __init__(self, name, lastname, addres, phoneNumber, role,managerName,rent) :
         super().__init__(name, lastname, addres, phoneNumber, role)
         self.manager = managerName
         self.rent = rent

    def printRepresentation(self) :
       super().printInfo()
       print("--------------------------------")
       print(f"Manager : {self.manager}")
       print(f"Rent amount : {self.rent}")
       print("--------------------------------")

def main() :
    print("welcome to our restaurant")
    print("please enter your information")
    name=input('name :')
    lastname = input('lastname :')
    phoneNumber = input('phoneNumber :')
    addres=input('addres :')
    while 1==1 :
        print("pick your role :")
        print("1) Customer")
        print("2) Supplier")
        print("3) Representation")
        choice = input()
        if choice == "1" : 
            CustomerFunc(name,lastname,phoneNumber,addres,"Customer")
            break
        elif choice == "2" : 
            supplierFunc(name,lastname,phoneNumber,addres,"Supplier")
            break
        elif choice == "3" : 
            RepresentationFunc(name,lastname,phoneNumber,addres,"Representation")
            break
        else : print("ERROR !")


def CustomerFunc(name,lastname,phoneNumber,addres,role) :
    order = input('Oreder name :')
    taking = 0
    while 1 == 1 :
      print("will you serve your order in our restaurant ? \n1)yes\netc)no")
      choice = input()
      if choice == "1" : 
            taking = 1
            break
      elif choice == "2" : 
            taking = 0
            break
    person = Customer(name, lastname, addres, phoneNumber, role,order,taking)  
    person.printCustomer()


def supplierFunc(name,lastname,phoneNumber,addres,role) :
    product = input('Product Name : ')
    barcode = input('Barcode Name : ')
    brand = input('Company : ')
    person = supplier( name, lastname, addres, phoneNumber, role,barcode,product,brand)  
    person.printSup()

def RepresentationFunc(name,lastname,phoneNumber,addres,role) :
    manager = input('manager Name : ') 
    rent = input('rent amount (per month) : ')
    person = Representation(name, lastname, addres, phoneNumber, role,manager,rent)  
    person.printRepresentation()

main()
