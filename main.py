import json
from art import art, tprint
from question import Question


class Game:
    def __init__(self, player):
        self.player = player
        self.welcome_message = self.read_file('resources/welcome.txt')
        self.questions = list()
        self.get_questions('resources/questions.json')
        self.score = 0

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
        print(f"{self.player}! Let's test your knowledge with a few questions!")
        game_over = False
        while not game_over:
            for question in self.questions:
                self.ask_a_question(question)
            game_over = True
        print()
        print("Bye!")

    def ask_a_question(self, question):
        print()
        print(question.question)
        print()
        index = 1
        for answer in question.answers:
            print(f"{index}. {answer}")
            index = index + 1

        user_input = input("What do you think is the correct answer?")
        if int(user_input) == question.correct_answer:
            print(art("happy27") + " " +question.correct_answer_response)
            return False
        else:
            print(f"{art('sad4')} {question.incorrect_answer_response}")
            print(f"The correct answer is: {question.get_correct_answer()}")
            return True


if __name__ == '__main__':
    player_name = input("What is your name? ")
    # player_name = "Blah Blah"
    game = Game(player_name)
    game.welcome()
    game.start()
