class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        self.following +=1


user1 = User("001","Sahaj")
user2 = User("002","Shakya")
user1.follow(user2)
print(f"User 1 follow count: {user1.followers}")
print(f"User 1 following count: {user1.following}")
print(f"User 2 follow count: {user2.followers}")
print(f"User 2 following count: {user2.following}")