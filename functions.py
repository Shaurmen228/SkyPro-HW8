import json
from question_class import Question


# def __init__(self, question_text: str, complexity: int, correct_answer: str):
def load_questions_from_json(path: str) -> list:
    """
    Парсинг json файла и выгрузка данных в лист
    """
    questions_list = []
    with open(path, "r", encoding="utf-8") as file:
        content_list = json.loads(file.read())

    for item in content_list:
        questions_list.append(Question(item["q"], int(item["d"]), item["a"]))

    return questions_list


def get_statistic(answers: list) -> None:
    """
    Вывод статистики
    """

    total_score = 0
    counter_correct_answers = 0

    for item in answers:
        if item.is_correct():
            counter_correct_answers += 1
            total_score += item.get_points()

    print("Вот и все!")
    print(f"Отвечено {counter_correct_answers} верно из {len(answers)}")
    print(f"Набрано {total_score} баллов")
