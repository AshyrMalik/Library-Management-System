class Member:
    def __init__(self,first_name,last_name,age,id):
        self.first_name= first_name
        self.last_name=last_name
        self.age=age
        self.id=id


    def display_member(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Age: {self.age}")
        

    def update_member(self,first_name=None,last_name=None,age=None,id=None):
        if first_name:
            self.first_name=first_name
        if last_name:
            self.last_name=last_name
        if age:
            self.age=age
        if id:
            self.id=id

