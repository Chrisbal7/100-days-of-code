class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_num = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        answer = input(f"Q{self.question_num}. {current_question.text}"
                       f"(True/False): ").strip().capitalize()
        self.check_answer(answer, current_question)

    def check_answer(self, answer, question):
        if answer == question.answer:
            print("You got it!")
            self.score += 1
        else:
            print("Oops, you're wrong!")
        print(f"The correct answer was: {question.answer}")

    def display_score(self):
        print(f"Your current score is: {self.score}/{self.question_num}")
