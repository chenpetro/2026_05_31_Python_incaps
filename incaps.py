import random

class User:
    @staticmethod
    def generate():
        return random.randint(1000, 9999)

    def __init__(self, name, age, email):
        self.name = name 
        self.age = age  
        self.__email = email  # Private attribute
        self._children = []  # Protected attribute
        self.ID = self.generate()  # Unique ID for each user

        
    def get_children(self):
        return self._children

    def get_email(self):
        return self.__email
    
    def set_email(self, new_email):
        self.__email = new_email

    def change_email(self, new_email=None):
        if new_email is None:
            new_email = input("Enter new email: ")

        if new_email != self.get_email():
            self.set_email(new_email)
            print("Email updated successfully.")
            return

        print("Email is the same as the current one. No changes made.")


user1 = User("Alice", 30, "q@test.com")
print(user1.name, user1.age)  # Output: Alice 30
user2 = User("Bob", 25, "bob@test.com")
print(user2.name, user2.age)  # Output: Bob 25
user1.change_email("alice.new@test.com")  # Update without prompt
print(user1.get_children())  # Output: []


print(user1.get_email())  # Output: alice.new@test.com
print(user2.get_email())  # Output: bob@test.com

user1.change_email()  # Update with prompt
print(user1.get_email())  # Output will depend on user input