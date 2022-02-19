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
        self.player = input("So, what should I call you? - ")
        tprint(f"Hello {self.player}!")
        self.main_menu()

    def main_menu(self):
        game_over = False
        while not game_over:
            print()
            print("Select from the following options:")
            print("1. Learn about Email phishing.")
            print("2. Test your knowledge with a trivia game.")
            print("3. Quit")
            print()

            try:
                player_input = int(input("So, what will it be? "))
            except ValueError:
                print("Try a number instead please.")
                continue

            if int(player_input) == 1:
                continue
            elif int(player_input) == 2:
                self.ask_questions()
            elif int(player_input) == 3:
                game_over = True
            else:
                print("Nah, select something that I can actually do now. More features TBA. Try again!")

        print(f"{self.player}, thank you for playing. Hope to see you soon!")
        sys.exit(0)

    def ask_questions(self):
        print()
        print(f"Alright {self.player}, let's test your email phishing knowledge with a few questions!")
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


if __name__ == '__main__':
    game = Game()
    game.start()
