class CreditCard:

	def make_payment(self,amount):
		self.amount = amount
		print(self.amount)

	def get_customer(self,customer):
		self.customer = customer
		print(self.customer)

	def get_bank(self,bank):
		self.bank= bank
		print(self.bank) 
 
	def get_account(self,customer,bank,balance_limit): 
		self.customer = customer
		self.bank= bank
		self.balance_limit = balance_limit
		print(self.customer + " " + self.bank + " " + self.balance_limit)

	def get_balance(self,balance): 
		self.balance = balance
		print(self.balance)

	def get_limit(self,balance_limit):
		self.balance_limit = balance_limit
		print(balance_limit) 

	def charge(self,price):
		self.price = price
		print(price)

c = CreditCard()
c.make_payment("1000")
c.get_customer("Hari") 
c.get_bank("NIC ASIA") 
c.get_account("Sherrif","NIBL","2000")
c.get_balance("4000") 
c.get_limit("6000") 
c.charge("500")

class PredatoryCreditCard:
	def charge(self,price,annual_percentage_rate):
		self.price = price
		self.annual_percentage_rate = annual_percentage_rate
		print("price: " + self.price + " annual percentage rate: " + self.annual_percentage_rate)

p = PredatoryCreditCard()
p.charge("1024","1.24")


