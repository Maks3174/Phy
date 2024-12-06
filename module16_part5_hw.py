import redis
import json

#1
class SocialNetwork:
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    def add_user(self, username, password, full_name, email):
        if self.r.hexists(f"user:{username}", "username"):
            return "User already exists."
        user_data = {
            "username": username,
            "password": password,
            "full_name": full_name,
            "email": email,
            "friends": json.dumps([]),
            "posts": json.dumps([])
        }
        self.r.hmset(f"user:{username}", user_data)
        return "User added successfully."

    def delete_user(self, username):
        if not self.r.hexists(f"user:{username}", "username"):
            return "User does not exist."
        self.r.delete(f"user:{username}")
        return "User deleted successfully."

    def edit_user_info(self, username, full_name=None, email=None):
        if not self.r.hexists(f"user:{username}", "username"):
            return "User does not exist."
        if full_name:
            self.r.hset(f"user:{username}", "full_name", full_name)
        if email:
            self.r.hset(f"user:{username}", "email", email)
        return "User information updated successfully."

    def search_user_by_name(self, full_name):
        keys = self.r.keys("user:*")
        users = []
        for key in keys:
            user_data = self.r.hgetall(key)
            if user_data["full_name"] == full_name:
                users.append(user_data)
        return users

    def view_user_info(self, username):
        if not self.r.hexists(f"user:{username}", "username"):
            return "User does not exist."
        user_data = self.r.hgetall(f"user:{username}")
        user_data["friends"] = json.loads(user_data["friends"])
        user_data["posts"] = json.loads(user_data["posts"])
        return user_data

    def view_user_friends(self, username):
        if not self.r.hexists(f"user:{username}", "username"):
            return "User does not exist."
        friends = json.loads(self.r.hget(f"user:{username}", "friends"))
        return friends

    def view_user_posts(self, username):
        if not self.r.hexists(f"user:{username}", "username"):
            return "User does not exist."
        posts = json.loads(self.r.hget(f"user:{username}", "posts"))
        return posts

    def add_friend(self, username, friend_username):
        if not self.r.hexists(f"user:{username}", "username") or not self.r.hexists(f"user:{friend_username}",
                                                                                    "username"):
            return "User does not exist."
        friends = json.loads(self.r.hget(f"user:{username}", "friends"))
        if friend_username not in friends:
            friends.append(friend_username)
            self.r.hset(f"user:{username}", "friends", json.dumps(friends))
        return "Friend added successfully."

    def add_post(self, username, post_content):
        if not self.r.hexists(f"user:{username}", "username"):
            return "User does not exist."
        posts = json.loads(self.r.hget(f"user:{username}", "posts"))
        posts.append(post_content)
        self.r.hset(f"user:{username}", "posts", json.dumps(posts))
        return "Post added successfully."


if __name__ == "__main__":
    sn = SocialNetwork()

    print(sn.add_user("john_doe", "password123", "John Doe", "john@example.com"))
    print(sn.add_user("jane_doe", "password456", "Jane Doe", "jane@example.com"))

    print(sn.add_friend("john_doe", "jane_doe"))

    print(sn.add_post("john_doe", "Hello, this is my first post!"))

    print(sn.view_user_info("john_doe"))
    print(sn.view_user_friends("john_doe"))
    print(sn.view_user_posts("john_doe"))

    print(sn.edit_user_info("john_doe", full_name="Johnathan Doe"))

    print(sn.search_user_by_name("Jane Doe"))

    print(sn.delete_user("john_doe"))


#2
class LiteratureMuseum:
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

    def add_user(self, username, password):
        if self.r.hexists(f"user:{username}", "username"):
            return "User already exists."
        user_data = {
            "username": username,
            "password": password
        }
        self.r.hmset(f"user:{username}", user_data)
        return "User added successfully."

    def add_exhibit(self, exhibit_id, title, description, related_people, category):
        if self.r.hexists(f"exhibit:{exhibit_id}", "exhibit_id"):
            return "Exhibit already exists."
        exhibit_data = {
            "exhibit_id": exhibit_id,
            "title": title,
            "description": description,
            "related_people": json.dumps(related_people),
            "category": category
        }
        self.r.hmset(f"exhibit:{exhibit_id}", exhibit_data)
        for person in related_people:
            self.r.sadd(f"person:{person}:exhibits", exhibit_id)
        return "Exhibit added successfully."

    def delete_exhibit(self, exhibit_id):
        if not self.r.hexists(f"exhibit:{exhibit_id}", "exhibit_id"):
            return "Exhibit does not exist."
        exhibit_data = self.r.hgetall(f"exhibit:{exhibit_id}")
        related_people = json.loads(exhibit_data["related_people"])
        for person in related_people:
            self.r.srem(f"person:{person}:exhibits", exhibit_id)
        self.r.delete(f"exhibit:{exhibit_id}")
        return "Exhibit deleted successfully."

    def edit_exhibit(self, exhibit_id, title=None, description=None, related_people=None, category=None):
        if not self.r.hexists(f"exhibit:{exhibit_id}", "exhibit_id"):
            return "Exhibit does not exist."
        if title:
            self.r.hset(f"exhibit:{exhibit_id}", "title", title)
        if description:
            self.r.hset(f"exhibit:{exhibit_id}", "description", description)
        if related_people:
            old_related_people = json.loads(self.r.hget(f"exhibit:{exhibit_id}", "related_people"))
            for person in old_related_people:
                self.r.srem(f"person:{person}:exhibits", exhibit_id)
            self.r.hset(f"exhibit:{exhibit_id}", "related_people", json.dumps(related_people))
            for person in related_people:
                self.r.sadd(f"person:{person}:exhibits", exhibit_id)
        if category:
            self.r.hset(f"exhibit:{exhibit_id}", "category", category)
        return "Exhibit updated successfully."

    def view_exhibit_info(self, exhibit_id):
        if not self.r.hexists(f"exhibit:{exhibit_id}", "exhibit_id"):
            return "Exhibit does not exist."
        exhibit_data = self.r.hgetall(f"exhibit:{exhibit_id}")
        exhibit_data["related_people"] = json.loads(exhibit_data["related_people"])
        return exhibit_data

    def view_all_exhibits(self):
        keys = self.r.keys("exhibit:*")
        exhibits = []
        for key in keys:
            exhibit_data = self.r.hgetall(key)
            exhibit_data["related_people"] = json.loads(exhibit_data["related_people"])
            exhibits.append(exhibit_data)
        return exhibits

    def view_people_related_to_exhibit(self, exhibit_id):
        if not self.r.hexists(f"exhibit:{exhibit_id}", "exhibit_id"):
            return "Exhibit does not exist."
        related_people = json.loads(self.r.hget(f"exhibit:{exhibit_id}", "related_people"))
        return related_people

    def view_exhibits_related_to_person(self, person):
        exhibit_ids = self.r.smembers(f"person:{person}:exhibits")
        exhibits = []
        for exhibit_id in exhibit_ids:
            exhibit_data = self.r.hgetall(f"exhibit:{exhibit_id}")
            exhibit_data["related_people"] = json.loads(exhibit_data["related_people"])
            exhibits.append(exhibit_data)
        return exhibits

    def view_exhibits_by_category(self, category):
        keys = self.r.keys("exhibit:*")
        exhibits = []
        for key in keys:
            exhibit_data = self.r.hgetall(key)
            if exhibit_data["category"] == category:
                exhibit_data["related_people"] = json.loads(exhibit_data["related_people"])
                exhibits.append(exhibit_data)
        return exhibits


if __name__ == "__main__":
    lm = LiteratureMuseum()

    print(lm.add_user("admin", "adminpassword"))

    print(lm.add_exhibit("1", "Exhibit One", "Description of Exhibit One", ["Person A", "Person B"], "Book"))
    print(lm.add_exhibit("2", "Exhibit Two", "Description of Exhibit Two", ["Person B", "Person C"], "Manuscript"))

    print(lm.view_exhibit_info("1"))

    print(lm.edit_exhibit("1", title="Updated Exhibit One"))

    print(lm.view_all_exhibits())

    print(lm.view_people_related_to_exhibit("1"))

    print(lm.view_exhibits_related_to_person("Person B"))

    print(lm.view_exhibits_by_category("Book"))

    print(lm.delete_exhibit("1"))
