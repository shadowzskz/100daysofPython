class User:

#Below are attributes
# user1 = User()
# user1.id = "001"
# user1.username = "Sahaj"
#
# user2 = User()
# user2.id = "002"
# user2.username = "Shakya"
#
# print(user1.username)
# print(user2.username)
# To minimize such case, we use constructor

    # def __init__(self):
    #     #Init is called everytime when new obj is being called
    #     print("Print here")

# user1 = User()
# user2 = User()
#So for above case, two print is executed

##Similarly data can also be initialized
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user1 = User(1, "Sahaj")
user2 = User(2, "Shakya")
#THis show the object locations
print(user1)
print(user2)
#TO access the values
print(user1.username)
print(user2.username)