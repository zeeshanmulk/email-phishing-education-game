class Question:
    def __init__(self, question_id, question, correct_answer, answers, correct_answer_response,
                 incorrect_answer_response):
        self.incorrect_answer_response = incorrect_answer_response
        self.correct_answer_response = correct_answer_response
        self.answers = answers
        self.correct_answer = correct_answer
        self.question_id = question_id
        self.question = question

    def get_correct_answer(self):
        return self.answers[self.correct_answer - 1]
