from quiz_brain import QuizBrain
from question_model import Question
from data import question_data
from random import shuffle


def main():
    question_bank = []
    for question in question_data:
        question_instance = Question(question['text'],
                                     question['answer'])
        question_bank.append(question_instance)
    shuffle(question_bank)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
        quiz.display_score()


if __name__ == "__main__":
    main()
