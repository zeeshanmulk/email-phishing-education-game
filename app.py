import json
import sys

from art import art, tprint
from question import Question
from random import shuffle

_data_file = 'resources/data.json'


class Game:
    def __init__(self):
        self.player = None
        self.questions = list()
        self.information_json = self.read_json_file()
        self.welcome_message = self.information_json['welcome']
        self.get_questions()
        self.knowledge = self.information_json['knowledge']
        self.references = self.information_json['references']
        self.attack_vectors = self.information_json['attack_vectors']
        self.score = 0
        self.points_per_question = round((100 / len(self.questions)), 2)

    def get_questions(self):
        for question in self.information_json['questions']:
            question_obj = Question(question['question_id'], question['question'], question['correct_answer'],
                                    question['answers'], question['correct_answer_response'],
                                    question['incorrect_answer_response'])
            self.questions.append(question_obj)

    @staticmethod
    def read_json_file():
        try:
            with open(_data_file, 'r') as f:
                return json.loads(f.read())
        except IOError:
            print("Could not read data file. Make sure there is a resources folder with data.json file in it. "
                  "Exiting...")
            sys.exit(1)

    def start(self):
        print(self.welcome_message)
        print()
        self.player = input("So, what should I call you? ")
        tprint(f"Hello {self.player}!")
        self.main_menu()

    def main_menu(self):
        game_over = False
        while not game_over:
            print(art("boombox1"))
            print()
            print("Here is the glorious main menu for your selection pleasure.")
            print("1. Learn about Email compromise and malware.")
            print("2. Learn about how you can be compromised to install a malware.")
            print("3. Test your knowledge with a trivia game.")
            print("4. Further readings.")
            print("5. Quit.")
            print(art("bee"))
            print()

            try:
                player_input = int(input(f"So, what will it be {self.player}? "))
            except ValueError:
                print("Try a number instead please.")
                continue

            if player_input == 1:
                self.training()
            elif player_input == 2:
                self.display_attack_vectors()
            elif player_input == 3:
                self.ask_questions()
            elif player_input == 4:
                self.display_references()
            elif player_input == 5:
                game_over = True
            else:
                print("Nah, select something that I can actually do now. Try again!")

        print(f"{self.player}, thank you for playing. Hope to see you soon!")
        sys.exit(0)

    def training(self):
        print(f"Alright {self.player}, its time for some lessons. I shall dispense what I know in a random order.")
        print()
        print("First up is:")
        shuffle(self.knowledge)
        training_over = False
        while not training_over:
            for knowledge in self.knowledge:
                print(knowledge)
                print()
                if self.yes_user_response_validator():
                    continue
                else:
                    break
            training_over = True
        print()
        print("Looks like we are done for now. Returning to main menu.")
        self.main_menu()

    def display_references(self):
        print("Ok, here is what I got for further readings. These resources were also used to prepare")
        print("this training module.")
        for reference in self.references:
            print(reference)
        print()
        self.pause()
        self.main_menu()

    def ask_questions(self):
        print()
        print(f"Alright {self.player}, let's test your knowledge with a few questions!")
        game_over = False
        shuffle(self.questions)
        while not game_over:
            for question in self.questions:
                # Correct answer
                if self.ask_a_question(question):
                    self.score += self.points_per_question
                    self.score = 100 if self.score > 99.50 else self.score
                    print()
                    print(f"Your current score is: {self.score}")
                    self.pause()
                # Incorrect answer
                else:
                    print()
                    print(f"Your current score is: {self.score}")
            game_over = True
        print()
        print(f"{self.player}, your total score is {self.score}. Thank you for playing!")

    def ask_a_question(self, question):
        print()
        print(art("singing"))
        print(question.question)
        print()
        index = 1
        for answer in question.answers:
            print(f"{index}. {answer}")
            index = index + 1
        print(f"{index}. Back to main menu.")

        user_input = input("What do you think is the correct answer?")
        if int(user_input) == question.correct_answer:
            print(art("happy27") + " " + question.correct_answer_response)
            return True
        elif int(user_input) == index:
            print("Alright. Back to main menu it is.")
            print(f"Your current score is: {self.score}")
            self.main_menu()
        else:
            print(f"{art('sad4')} {question.incorrect_answer_response}")
            print(f"The correct answer is: {question.get_correct_answer()}")
            return False

    @staticmethod
    def pause():
        print()
        input("Press Enter/Return to continue...")

    def display_attack_vectors(self):
        print("So you want to know how YOU can be used as an attack vector? Dispensing knowledge...")
        shuffle(self.attack_vectors)
        training_over = False
        while not training_over:
            for vector in self.attack_vectors:
                print()
                print(vector)
                if self.yes_user_response_validator():
                    continue
                else:
                    break
            training_over = True
        print()
        print("Looks like we are done! Returning to main menu.")
        self.main_menu()

    @staticmethod
    def yes_user_response_validator():
        while True:
            print()
            user_response = input("Should I continue? (y/n): ")
            if user_response[0].lower() == 'y':
                return True
            elif user_response[0].lower() == 'n':
                return False
            else:
                print("Lets stick a simple yes or a no.")
                continue


if __name__ == '__main__':
    game = Game()
    game.start()
