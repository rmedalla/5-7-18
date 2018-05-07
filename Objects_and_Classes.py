class Person():
    greeting_count = 0
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 1


    def greet(self, other_person):
        
        print(f"Hello {other_person.name}, I am {self.name}")
        
    def getGreetNumber(self):
        Person.greeting_count += 1
        print(self.greeting_count)

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone}")

    def add_friend(self, friends):
        self.friends.append(self.name)
        print(self.friends)

    def num_friends(self, friends):
        print(len(self.friends))


sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

#jordan.add_friend(sonny)
#jordan.num_friends(jordan)
#print(len(jordan.friends))

#prints the NAME, EMAIL, PHONE from the class Person
#print(sonny.name, sonny.email, sonny.phone)
#print(jordan.name, jordan.email, jordan.phone)
#PRINTS GREETINGS
#Person.greet(sonny, jordan)
#Person.greet(jordan, sonny)

#PRINTS CONTACT INFO
#print(sonny.email, sonny.phone)
#print(jordan.email, jordan.phone)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year
    
    def print_info(self):
        print(self.year, self.make, self.model)




car = Vehicle("Nissan", "Leaf", "2015")

# print(car.make, car.model, car.year)

#car.print_info()
#sonny.print_contact_info()

#Adding using .append
#jordan.friends.append(sonny)
#sonny.friends.append(jordan)

