class Game:
    def __init__(self, player_name):
        self.player = player_name

    def welcome(self):



if __name__ == '__main__':
    player_name = input("What is your name?: ")
    game = Game(player_name)

