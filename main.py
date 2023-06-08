import os.path
import functions
import random


def main():
    question_list = functions.load_questions_from_json(os.path.join("Data", "questions.json"))
    random.shuffle(question_list)

    print("Программа начинается!")
    for item in question_list:
        item.is_asked = True
        item.build_question()

        user_input = input("Ввод: ")
        item.user_response = user_input

        item.build_feedback()
    functions.get_statistic(question_list)


main()
