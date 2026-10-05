#!/usr/bin/env python3
print("Ik hou van brawl stars")

class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def display_info(self):
        print(f"Player Name: {self.name}, Level: {self.level}")

player1 = Player("Alice", 10)
player1.display_info()