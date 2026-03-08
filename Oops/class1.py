#Basic concept of oops concept
class Place:
    country = ""

    def __init__(self, city, state):
        self.city = city
        self.state = state

    def mango(self):
        print(f"{self.city} best for mango. WHich is based on {Place.country}.")

Place.country = "India"

place1_obj = Place("Malda", "WB")

#outside class
def mango1(area):
        print(f"{area} best for man.")
    
place1_obj.mango()
mango1("Kaj")


