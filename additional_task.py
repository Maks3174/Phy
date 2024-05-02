import pickle

def update_friends_dict(friends_dict, person1, person2):
    if person1 in friends_dict:
        friends_dict[person1].append(person2)
    else:
        friends_dict[person1] = [person2]

def save_friends_to_file(friends_dict, filename):
    with open(filename, 'wb') as f:
        pickle.dump(friends_dict, f)

def load_friends_from_file(filename):
    with open(filename, 'rb') as f:
        friends_dict = pickle.load(f)
    return friends_dict

def main():
    fixed_friends_dict = {
        'Alice': ['Bob', 'Charlie'],
        'Bob': ['Alice', 'Charlie'],
        'Charlie': ['Alice', 'Bob']
    }

    save_friends_to_file(fixed_friends_dict, "friends.pkl")
    print("Дані про фіксованих друзів збережено у файлі 'friends.pkl'.")

    loaded_friends_dict = load_friends_from_file("friends.pkl")
    print("\nЗавантажені дані про друзів:")
    for person, friends in loaded_friends_dict.items():
        print(f"{person}: {', '.join(friends)}")

if __name__ == "__main__":
    main()
