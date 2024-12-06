from fastrbtree import FastRBTree

class TaxPenaltyDatabase:
    def __init__(self):
        self.database = FastRBTree()

    def print_database(self):
        print("Tax Penalty Database:")
        for person_code, penalties in self.database.items():
            print(f"Person Code: {person_code}, Penalties: {penalties}")

    def print_by_person_code(self, person_code):
        if person_code in self.database:
            print(f"Penalties for Person with Code {person_code}: {self.database[person_code]}")
        else:
            print(f"No penalties found for Person with Code {person_code}")

    def print_by_penalty_type(self, penalty_type):
        print(f"Penalties with Type '{penalty_type}':")
        for person_code, penalties in self.database.items():
            for penalty in penalties:
                if penalty['type'] == penalty_type:
                    print(f"Person Code: {person_code}, Penalty: {penalty}")

    def print_by_city(self, city):
        print(f"Penalties for People in {city}:")
        for person_code, penalties in self.database.items():
            for penalty in penalties:
                if penalty['city'] == city:
                    print(f"Person Code: {person_code}, Penalty: {penalty}")

    def add_person(self, person_code, penalties):
        self.database[person_code] = penalties

    def add_penalty(self, person_code, penalty):
        if person_code in self.database:
            self.database[person_code].append(penalty)
        else:
            self.database[person_code] = [penalty]

    def remove_penalty(self, person_code, penalty):
        if person_code in self.database:
            if penalty in self.database[person_code]:
                self.database[person_code].remove(penalty)
                print("Penalty removed successfully.")
            else:
                print("Penalty not found for this person.")
        else:
            print("Person not found in the database.")

    def update_person_info(self, person_code, penalties):
        if person_code in self.database:
            self.database[person_code] = penalties
            print("Person information updated successfully.")
        else:
            print("Person not found in the database.")

def main():
    database = TaxPenaltyDatabase()

    database.add_person("1234567890", [{"type": "Speeding", "amount": 100, "city": "Kyiv"}])
    database.add_person("0987654321", [{"type": "Parking Violation", "amount": 50, "city": "Lviv"}])
    database.add_person("1111111111", [{"type": "Speeding", "amount": 150, "city": "Odessa"}])

    database.print_database()

    database.print_by_person_code("1234567890")
    database.print_by_penalty_type("Speeding")
    database.print_by_city("Lviv")

if __name__ == "__main__":
    main()
