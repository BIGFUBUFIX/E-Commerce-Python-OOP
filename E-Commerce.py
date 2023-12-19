#Big_E_Lazapee
class Big_E_Product:
    def __init__(self,name_product,price_product,review_product):
        self.__name_product = name_product
        self.__price_product = price_product
        self.__review_product = review_product
    @property
    def name_product(self):  
        return self.__name_product
    @name_product.setter
    def name_product(self, name_product): 
        if name_product in ["Submarine","Truck","Tank","Airplane"]:
            self.__name_product = name_product
        else:
            print("Product Name Error !")
    
    @property
    def price_product(self):
        return self.__price_product
    @price_product.setter
    def price_product(self, price_product):
        if price_product() in [199,299,399]:
            self.__price_product = price_product
        else:
            print("Price Error !")
            
    @property
    def review_product(self):
        return self.__review_product
    @review_product.setter
    def review_product(self, review_product):
        if review_product() in ["8 ดาว","4.5 ดาว","4 ดาว"]:
            self.__review_product = review_product 
        else:
            print("Rating Error !")

class Big_E_Customer:
    def __init__(self,name_customer,email,password,shopping_cart):
        self.__name_customer = name_customer
        self.__email = email
        self.__password = password
        self.shopping_cart = shopping_cart

    @property
    def name_customer(self):
        return self.__name_customer
    @name_customer.setter
    def name_customer(self,name_customer):
        if name_customer() in ["Peter JunOreoChanom"]:
            self.__name_customer = name_customer
        else:
            print("Not found Name !")
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        if email() in ["Peter@kmitl.ac.th"]:
            self.__email = email
        else:
            print("Not found Email !")
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,email):
        if email() in ["Peter@kmitl.ac.th"]:
            self.__email = email
        else:
            print("Not found Email !")    
    
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password):
        if password() in [111222]:
            self.__password = password
        else:
            print("Re-Password !")    
        
class Big_E_Order:
    def __init__(self,order_id,date_order,date_recieve) :
        self.order_id = order_id
        self.date_order = date_order
        self.date_recieve = date_recieve
        
class Big_E_Payment:
    def __init__(self,credit_card):
        self.__credit_card = credit_card
    
    @property
    def credit_card(self):
        return self.__credit_card    
    @credit_card.setter
    def credit_card(self, credet_card):
        if credet_card() in ["Visa","Mastercard"]:
            self.__credit_card = credet_card
        else:
            print("Credit Card Reject")
    def Coupon_1(self):
        print('ได้รับคูปองส่วนลด 50 % ขั้นต่ำ 1 ล้านบาท') 

shopping_cart = 1
order_id = "TX14587896DS"
date_order = '15/09/2566'
date_recieve = '18/09/2566'
p1 = Big_E_Product("Submarine",199,"8 ดาว")
p2 = Big_E_Customer("Peter JunOreoChanom","Peter@kmitl.ac.th","111222",shopping_cart) 
p3 = Big_E_Payment("Visa")
p4 = Big_E_Order(order_id,date_order,date_recieve)

print("Login")
print("Email :",p2.email)
print("Password :",p2.password)
print("---------------------------------")
print("ชื่อลูกค้า :",p2.name_customer)
print("สินค้าในตะกร้า : ",shopping_cart)
print("หมายเลขคำสั่งซื้อ : ",order_id)
print("วันที่สั่งซื้อ",date_order)
print("วันที่ได้รับสินค้า",date_recieve)
print("ชื่อสินค้า : ",p1.name_product)
print("ตำหนิ : ไม่มีเครื่องยนต์")
print("ราคา : ",p1.price_product ,"บาท")
print("คะแนนรีวิว :",p1.review_product)
print("---------------------------------")
print("Creditcard : ",p3.credit_card)
p3.Coupon_1()







