class Building:
	def number_room(self, bedroom, bathroom):
		self.bedroom = bedroom
		self.bathroom = bathroom
		print("the number of bedroom " + self.bedroom + " the number of bathroom " + self.bathroom)

class Apartment(Building):
	def number_of_hall(self,bedroom,bathroom,hall):
		super().number_room(bedroom,bathroom)
		self.hall = hall
		print("the number of bedroom " + self.bedroom + " the number of bathroom " + self.bathroom +" the number of hall "+ self.hall)

class House(Building):
	def garden_area(self,bedroom,bathroom,garden):
		super().number_room(bedroom,bathroom)
		self.garden= garden
		print("the number of bedroom " + self.bedroom + " the number of bathroom " + self.bathroom + " the area of garden " + self.garden)

class Commercial(Building):
	def number_parking(self,bedroom,bathroom,parking):
		super().number_room(bedroom,bathroom)
		self.parking= parking
		print("the number of bedroom " + self.bedroom + " the number of bathroom " + self.bathroom + " the area of garden " + self.parking)


a = Apartment()
a.number_of_hall("13","3","5")
b = House()
b.garden_area("15","4","2")
c = Commercial()
c.number_parking("20","5","1")

