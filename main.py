import json
from art import art, tprint
from question import Question
from random import shuffle


class Game:
    def __init__(self, player):
        self.player = player
        self.welcome_message = self.read_file('resources/welcome.txt')
        self.questions = list()
        self.get_questions('resources/questions.json')
        self.score = 0
        self.points_per_question = round((100 / len(self.questions)), 2)

    @staticmethod
    def read_file(file_name):
        with open(file_name, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
        return lines

    def welcome(self):
        print()
        tprint(f"Hello {self.player}!")
        for line in self.welcome_message:
            print(line)
        self.pause()

    def get_questions(self, file_name):
        with open(file_name, 'r') as f:
            questions = json.loads(f.read())
        for question in questions['questions']:
            question_obj = Question(question['question_id'], question['question'], question['correct_answer'],
                                    question['answers'], question['correct_answer_response'],
                                    question['incorrect_answer_response'])
            self.questions.append(question_obj)

    def start(self):
        print()
        print(f"{self.player}, Let's test your phishing knowledge with a few questions!")
        game_over = False
        while not game_over:
            shuffle(self.questions)
            for question in self.questions:
                if self.ask_a_question(question):
                    self.score += self.points_per_question
                    self.score = 100 if self.score > 99.50 else self.score
                    print()
                    print(f"Your current score is: {self.score}")
                    self.pause()
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

        user_input = input("What do you think is the correct answer?")
        if int(user_input) == question.correct_answer:
            print(art("happy27") + " " + question.correct_answer_response)
            return True
        else:
            print(f"{art('sad4')} {question.incorrect_answer_response}")
            print(f"The correct answer is: {question.get_correct_answer()}")
            return False

    @staticmethod
    def pause():
        print()
        input("Press Enter/Return to continue...")


if __name__ == '__main__':
    player_name = input("What is your name? ")
    game = Game(player_name)
    game.welcome()
    game.start()
