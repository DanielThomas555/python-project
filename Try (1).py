import os
from termcolor import colored

# System call
os.system("")

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self): 
		return "Name :%20s  Age: %3d " % (self.name, self.age)


class TicketVendor:	
	def __init__(self):
		print("happy movie ticket booking")
		self.x = int(input("\t\tEnter Rows:"))
		self.y = int(input("\t\tEnter Cols:"))	
		self.list_of_persons = []
		if(self.x * self.y > 60):
			self.Front = self.x//2
		else:
			self.Front = 0
		self.list_sel = [] 
		self.CurrentIncome = 0
		self.TotalIncome = 0

	def buy_info(self, price):
		name = input("\t\t Enter Name : ")
		age = int(input("\t\t Enter Age : "))
		Person1 = Person(name, age)
		self.TotalIncome += price
		self.list_of_persons.append(Person1)

	def buy(self):
		self.ins = int(input("\t\tEnter No. of tickets:"))
		self.view()
		self.CurrentIncome = 0
		for i in range(self.ins):
			sel = input("\t\tEnter Seat selection : ")
			if(sel in self.list_sel):
				print("\t\tSeat already taken")
				break
			elif(ord(sel[0])-65 < self.Front):
				self.CurrentIncome += 10
				self.buy_info(10)
				print("\t\tValue = $10")
			else:
				self.CurrentIncome += 8
				print("\t\tValue = $8")
				self.buy_info(8)
			self.list_sel.append(sel)

		print("\n\t\tSeats selected : ", self.list_sel)
		print("\t\tCurrentIncome : ", self.CurrentIncome)


	def view(self):
		print("*"*50)
		for i in range(self.x):
			if( i == self.Front):
				print("_________________________________________________")
			for j in range(self.y):
				if(chr(65+i)+str(j) in self.list_sel ):
					print(" ",colored(chr(65+i)+str(j), 'red'),end =" ")
				else:
					print(" ",chr(65+i)+str(j),end=" ")
			print("\n")
		print("*"*50)

	def statistics(self):		
		print("\t\tTotal Income ",self.TotalIncome)

	def show_usr_info(self):
		for i in self.list_of_persons:
			print(i)

Ticket_Vendor = TicketVendor()
while True:
	print("""

		1.	View Seats
		2.	Buy Ticket
		3. 	Statistics
		4.	Show Booked Ticket (User Info) 
		0.	Exit

		""")
	Menu_selection = int(input("Enter Choice : "))
	if(Menu_selection == 0):
		exit()
	elif(Menu_selection == 1):
		Ticket_Vendor.view()
	elif(Menu_selection == 2):
		Ticket_Vendor.buy()
	elif(Menu_selection == 3):
		Ticket_Vendor.statistics()
	elif(Menu_selection == 4):
		Ticket_Vendor.show_usr_info()



