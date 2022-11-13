import requests
import json


class Pokemon:
    def __init__(self, name):
        self.__response = requests.get("https://pokeapi.co/api/v2/pokemon/" + name.lower())
        self.__data = json.loads(self.__response.text)
        self.__name = self.__data["name"]
        self.__weight = self.__data["weight"] / 10
        self.__height = self.__data["height"] * 10
        self.__ID = self.__data["id"]
        self.__HP = self.__data['stats'][0]['base_stat']
        self.__attack = self.__data['stats'][1]['base_stat']
        self.__defence = self.__data['stats'][2]['base_stat']
        self.__special_attack = self.__data['stats'][3]['base_stat']
        self.__special_defence = self.__data['stats'][4]['base_stat']
        self.__speed = self.__data['stats'][5]['base_stat']
        self.__moves = []
        for i in range(len(self.__data['moves']) // 2):
            self.__moves.append(self.__data['moves'][i]['move']['name'])
        self.__types = []
        for i in self.__data["types"]:
            self.__types.append(i["type"]["name"])

        self.__photo_response = requests.get(
            "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + str(self.__ID) + ".png")

        self.__photo = self.__photo_response.url

    def get_name(self):
        return self.__name

    def get_weight(self):
        return self.__weight

    def get_height(self):
        return self.__height

    def get_ID(self):
        return self.__ID

    def get_HP(self):
        return self.__HP

    def get_special_attack(self):
        return self.__special_attack

    def get_attack(self):
        return self.__attack

    def get_defence(self):
        return self.__defence

    def get_moves(self):
        return self.__moves

    def get_special_defence(self):
        return self.__special_defence

    def get_types(self):
        return self.__types

    def get_speed(self):
        return self.__speed

    def get_photo(self):
        return self.__photo
