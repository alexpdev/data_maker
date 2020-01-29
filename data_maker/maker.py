import random
from data_maker import samples


class Maker():
    def __init__(self):




class UserMaker():
    def __init__(self):
        self.name = None
        self.first_name = None
        self.last_name = None
        self.occupation = None
        self.country = None
        self.state = None
        self.description = None
        self.username = None
        self.age = None
        self.info = get_info(self)

    def get_info(self):
        info = {"name": self.name, "first_name": self.first_name, "last_name": self.last_name, "occupation": self.occupation, "country": self.country, "state": self.state, "username": self.username, "age": self.age, "description": self.description}
        return info


    def set_info(self):
        self.get_name()
        self.get_occupation()
        self.get_state()
        self.get_description()
        self.get_username()
        self.get_age()
        return self.info


    def get_name(self):
        if self.first_name == None:
            self.first_name = self.get_first_name()
        if self.last_name == None:
            self.last_name = self.get_last_name()
        self.name = self.first_name + ' ' + self.last_name
        return self.name


    def get_age(self):
        self.age = random.randint(18, 75)
        return self.age


    def get_username(self):
        if self.name == None:
            name = self.get_name()
        else:
            name = self.name
        username = name.split(' ')
        self.username = ('.'.join(username)).lower()
        return self.username


    def get_description(self):
        description = ""
        num_words = random.randint(12,25)
        for i in range(num_words):
            word = random.choice(samples.lorem)
            if i == num_words - 1:
                description += word + "."
                break
            else:
                description += word + " "
        self.description = description
        return self.description


    def get_first_name(self):
        self.first_name = random.choice(samples.first_name)
        return self.first_name

    def get_last_name(self):
        self.last_name = random.choice(samples.first_name)
        return self.last_name


    def get_occupation(self):
        self.occupation = random.choice(samples.occupations)
        return self.occupation


    def get_state(self):
        self.state = random.choice(samples.states)
        if self.state in samples.states[-6:]:
            self.country = "Canada"
        else:
            self.country = "United States"
        return self.state


    def get_country(self):
        if self.state == None:
            self.country = random.choice(samples.countries)
        elif self.state in states[-6:]:
            self.country = "Canada"
        else:
            self.country = "United States"
        return self.country

if __name__ == "__main__":
    pass
