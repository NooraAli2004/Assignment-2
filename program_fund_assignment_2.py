# -*- coding: utf-8 -*-
"""program fund assignment #2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_F3AisVR92KOvcMWtvO9l6lehPd5otHL
"""

class Artwork: #create a class called artwork
    def __init__(self, title, artist, date, significance): #define its attributes
        self.title = title #defining values of attributes when they are being called
        self.artist = artist
        self.date = date
        self.significance = significance

class Exhibition: #create a class called exhibition
    def __init__(self, name, location, artworks): #define its attributes
        self.name = name #defining values of attributes when they are being called
        self.location = location
        self.artworks = artworks

class Museum: #create a class called museum
    def __init__(self):
        self.artworks = [] #creating empty lists to store artwork
        self.exhibitions = [] #creating empty lists to store exhibitions

    def add_artwork(self, artwork): #defining a method to append the artwork in the empty list
        self.artworks.append(artwork)

    def create_exhibition(self, name, location, artworks): #defining a method within the museum class to add exhibitions to the list
        exhibition = Exhibition(name, location, artworks) #creating exhibition objects
        self.exhibitions.append(exhibition) #appending them

    def display_artworks(self): #defining a method to display the artwork
        for artwork in self.artworks: #for loop that goes over all the artwork
            print(f"Title: {artwork.title}") #prints each of the attributes of the artwork
            print(f"artist: {artwork.artist}")
            print(f"Date: {artwork.date}")
            print(f"Significance: {artwork.significance}\n")

    def display_exhibitions(self): #defining a method to display the exhibitions
        for exhibition in self.exhibitions: #creating for loop that goes over all the artwork
            print(f"Exhibition Name: {exhibition.name}") #prints each of the attributes of the exhibitions
            print(f"Location: {exhibition.location}")
            print("Artworks:")
            for artwork in exhibition.artworks: #creating a for loop that goes over all the artwork in the exhibition
                print(f"\t{artwork.title} from {artwork.artist}") #printing the information of the artwork
            print()

class Ticket: #creating a class called ticket
    def __init__(self, event, location, duration, visitors, price): #defining all its attributes
        self.event = event  #defining values of attributes when they are being called
        self.location = location
        self.duration = duration
        self.visitors = visitors
        self.price = price

class VisitorManagementSystem: #creating a class for managing the visitors
    def __init__(self):
        self.visitors = [] #creating an empty list to append visitors
        self.tickets = []#creating an empty list to append visitors

    def add_visitor(self, visitor): #defining a method within the class
        self.visitors.append(visitor) #appending new visitors to the list

    def purchase_ticket(self, event, location, duration, visitors, price): #defining a method for purchasing tickets
        ticket = Ticket(event, location, duration, visitors, price) #creating an object and giving it parameters
        self.tickets.append(ticket) #appending ticket to the list

    def display_visitors(self): #defining a method for displaying all the visitor information
        for visitor in self.visitors: #creating for loop iterating through all the information
            print(f"Name: {visitor.name}") #printing the information
            print(f"Age: {visitor.age}")
            print(f"Category: {visitor.category}")
            print()

    def display_tickets(self): #defining a method for displaying all the ticket information
        for ticket in self.tickets: #for loop iterating through all the ticket information
            print(f"Event: {ticket.event}") #printing the information
            print(f"Location: {ticket.location}")
            print(f"Duration: {ticket.duration}")
            print("Visitors:")
            for visitor in ticket.visitors: #for loop iterating through every visitor and the ticket they hold
                print(f"\tName: {visitor.name}, Age: {visitor.age}, Category: {visitor.category}") #printing each visitor and their ticket and the category their in
            print(f"Price: {ticket.price} AED") #printing ticket price
            print()

class Visitor: #creating class called visitor
    def __init__(self, name, age, category): #define its attributes
        self.name = name #defining values of attributes when they are being called
        self.age = age
        self.category = category

def calculate_ticket_price(visitor): #defining a function for calculating the price of each visitor
    if visitor.category in ["Child", "Teacher", "Student", "Senior"]: #if any of the visitor is eligible for these categories then they get a free ticket
        return 0 #returning 0 AED
    elif visitor.category == "Group": #if the visitor falls in the group category they get a discount
        return 0.5 * 63  # 50% discount of the original price
    else:
        return 63  #or else returning the original price

def apply_vat(price): #defining a function that applies a VAT to the ticket price.
    return price * 1.05  #  returns the ticket price multiplied by 1.05 to apply a 5% VAT

# Sample usage:
if __name__ == "__main__":
    # Creating Museum
    louvre = Museum()

    # Adding Artworks
    artwork1 = Artwork("Lion braclet", "anonymous artisan from Iran", "ca. 800-600 BCE", "Iconic jewellery")
    artwork2 = Artwork("Sphinx", "Greek empire", "c. 500-600 BCE", "Ancient Greek sculpture")
    artwork3 = Artwork("Bodhisattva", "anonymous artisan from India", "c. 100-300 BCE", "religious indian sculpture")

    louvre.add_artwork(artwork1)
    louvre.add_artwork(artwork2)
    louvre.add_artwork(artwork3)

    # Creating Exhibitions
    exhibition1 = Exhibition("First Great Powers", "Permanent Galleries", [artwork1])
    exhibition2 = Exhibition("Civilizations and Empires", "Exhibiton Halls", [artwork2])

    louvre.create_exhibition("First Great Powers", "Permanent Galleries", [artwork1])
    louvre.create_exhibition("Civilizations and Empires", "Exhibiton Halls", [artwork2])

    # Displaying Artworks and Exhibitions
    print("All Artworks in Louvre Museum:")
    louvre.display_artworks()

    print("\nAll Exhibitions in Louvre Museum:")
    louvre.display_exhibitions()

    # Visitor Management and Ticketing
    visitor_system = VisitorManagementSystem()

    visitor1 = Visitor("Noora", 20, "Adult")
    visitor2 = Visitor("Hind", 16, "Student")
    visitor3 = Visitor("Hessa", 65, "Senior")
    visitor4 = Visitor("Maryam", 35, "Group")

    visitor_system.add_visitor(visitor1) #adding visitors
    visitor_system.add_visitor(visitor2)
    visitor_system.add_visitor(visitor3)
    visitor_system.add_visitor(visitor4)

    ticket_price1 = calculate_ticket_price(visitor1) #calcluating their tickets
    ticket_price2 = calculate_ticket_price(visitor2)
    ticket_price3 = calculate_ticket_price(visitor3)
    ticket_price4 = calculate_ticket_price(visitor4)

    ticket_price1 = apply_vat(ticket_price1) #applying the VAT
    ticket_price2 = apply_vat(ticket_price2)
    ticket_price3 = apply_vat(ticket_price3)
    ticket_price4 = apply_vat(ticket_price4)

    visitor_system.purchase_ticket("Exhibition", "Permanent Galleries", "2 hours", [visitor1], ticket_price1) #displaying ticket infromation
    visitor_system.purchase_ticket("Exhibition", "Exhibiton Hall", "2 hours", [visitor2], ticket_price2)
    visitor_system.purchase_ticket("Exhibition", "Permanent Galleries", "2 hours", [visitor3], ticket_price3)
    visitor_system.purchase_ticket("Exhibition", "Outdoor Space", "2 hours", [visitor4], ticket_price4)

    print("\nAll Visitors:")
    visitor_system.display_visitors()

    print("\nAll Tickets Purchased:")
    visitor_system.display_tickets()

# Test Case: Addition of new art to the museum
def test_add_artwork():
    louvre = Museum()
    artwork = Artwork("The Starry Night", "Vincent van Gogh", "1889", "Iconic painting")
    louvre.add_artwork(artwork)
    if artwork in louvre.artworks:
        print("New artwork added:", artwork.title, "by", artwork.artist)
    else:
        print("Artwork not found")


# Test Case: Opening of a new exhibition at the museum
def test_create_exhibition():
    louvre = Museum()
    artworks = [
        Artwork("The Starry Night", "Vincent van Gogh", "1889", "Iconic painting"),
        Artwork("Mona Lisa", "Leonardo da Vinci", "c. 1503–1506", "Iconic portrait")]
    louvre.create_exhibition("Masterpieces", "Gallery 1", artworks)
    if len(louvre.exhibitions) == 1:
        exhibition = louvre.exhibitions[0]
        print("New exhibition opened at the Louvre Museum called:", exhibition.name, "At", exhibition.location )
        print("Artworks in the exhibition:")
        for artwork in exhibition.artworks:
            print("\tTitle:", artwork.title)
            print("\tArtist:", artwork.artist)
            print("\tDate:", artwork.date)
            print("\tSignificance:", artwork.significance)
            print()
    else:
        print("Exhibition not found")




# Test Case: purchase and Display of payment receipts for purchasing tickets for one person
def test_display_tickets():
    visitor_system = VisitorManagementSystem()
    visitor = Visitor("Ayesha", 20, "Adult")
    visitor_system.add_visitor(visitor)
    ticket_price = calculate_ticket_price(visitor)
    ticket_price_with_vat = apply_vat(ticket_price)
    visitor_system.purchase_ticket("Exhibition", "Gallery 1", "2 hours", [visitor], ticket_price_with_vat)
    if len(visitor_system.tickets) == 1 and visitor_system.tickets[0].price == ticket_price_with_vat:
        print("Payment receipts for purchasing tickets for an individual:")
        ticket = visitor_system.tickets[0]
        print("Visitors:")
        for visitor in ticket.visitors:
            print("\tName:", visitor.name)
            print("\tCategory:", visitor.category)
        print("Price:", ticket.price, "AED")
    else:
        print("Payment failed")

#displaying tickets for multiple people
def test_display_tickets_group():
    visitor_system = VisitorManagementSystem()

    visitors = [
        Visitor("Noora", 30, "Adult"),
        Visitor("Hind", 25, "Adult"),
        Visitor("Hessa", 16, "Student"),
        Visitor("Maryam", 70, "Senior")]

    # Adding visitors to the system
    for visitor in visitors:
        visitor_system.add_visitor(visitor)

    # Purchasing tickets for all visitors
    total_price = 0
    for visitor in visitors:
        ticket_price = calculate_ticket_price(visitor)
        ticket_price_with_vat = apply_vat(ticket_price)
        visitor_system.purchase_ticket("Exhibition", "Gallery 1", "2 hours", [visitor], ticket_price_with_vat)
        total_price += ticket_price_with_vat

    # Displaying purchase details
    if len(visitor_system.tickets) == len(visitors):
        print("Purchase receipts for all tickets in a group:")
        for ticket in visitor_system.tickets:
            print("Visitors:")
            for visitor in ticket.visitors:
                print("\tName:", visitor.name)
                print("\tCategory:", visitor.category)
            print("Price:", ticket.price, "AED")
        print("Total Price for all tickets:", total_price, "AED")
    else:
        print("Purchase failed")





# Running the test cases
if __name__ == "__main__":
    test_add_artwork()
    test_create_exhibition()
    test_display_tickets()
    test_display_tickets_group()