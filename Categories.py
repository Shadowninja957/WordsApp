from abc import ABC, abstractmethod

'''Beginning of Category Classes'''


class Category(ABC):

    @abstractmethod
    def getInterface(self) -> object:
        pass

    @abstractmethod
    def getCategory(self) -> str:
        pass

    @abstractmethod
    def getCategoryDescription(self) -> str:
        pass


class Anatomy(Category):

    def __init__(self):
        self.category = "Anatomy"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class People(Category):

    def __init__(self):
        self.category = "People"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Animal(Category):

    def __init__(self):
        self.category = "Animal"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Place(Category):

    def __init__(self):
        self.category = "Place"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Thing(Category):

    def __init__(self):
        self.category = "Thing"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Entertainment(Category):

    def __init__(self):
        self.category = "Entertainment"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Movie(Entertainment):

    def __init__(self):
        super().__init__()
        self.category = self.category + " - Movie"
        self.description = "Place description here"


class TvShow(Entertainment):

    def __init__(self):
        super().__init__()
        self.category = self.category + " - Tv Show"
        self.description = "Place description here"


class Anime(Entertainment):

    def __init__(self):
        super().__init__()
        self.category = self.category + " - Anime"
        self.description = "Place description here"


class Cartoon(Entertainment):

    def __init__(self):
        super().__init__()
        self.category = self.category + " - Cartoon"
        self.description = "Place description here"


class Music(Entertainment):

    def __init__(self):
        super().__init__()
        self.category = self.category + " - Music"
        self.description = "Place description here"


class Art(Entertainment):

    def __init__(self):
        super().__init__()
        self.category = self.category + " - Art"
        self.description = "Place description here"


class Verb(Category):

    def __init__(self):
        self.category = "Verb"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Adjective(Category):

    def __init__(self):
        self.category = "Adjective"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Food(Category):

    def __init__(self):
        self.category = "Food"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Drink(Category):

    def __init__(self):
        self.category = "Drink"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class CustomWord(Category):

    def __init__(self):
        self.category = "CustomWord"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Game(Category):

    def __init__(self):
        self.category = "Game"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class LeagueOfLegends(Game):

    def __init__(self):
        super().__init__()
        self.category = self.category + " - League of Legends"
        self.description = "Place description here"


class Apex(Game):

    def __init__(self):
        super().__init__()
        self.category = self.category + " - Apex"
        self.description = "Place description here"


class Overwatch(Game):

    def __init__(self):
        super().__init__()
        self.category = self.category + " - Overwatch"
        self.description = "Place description here"


class Color(Category):

    def __init__(self):
        self.category = "Color"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


class Astrology(Category):

    def __init__(self):
        self.category = "Astrology"
        self.description = "Place description here"

    def getInterface(self):
        return type(self)

    def getCategory(self):
        return self.category

    def getCategoryDescription(self):
        return self.description


'''End of Category classes'''