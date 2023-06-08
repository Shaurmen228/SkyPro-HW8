class Question:
    is_asked = False
    user_response = None

    def __init__(self, question_text: str, complexity: int, correct_answer: str):
        """
        Конструктор
        """
        self.question_text = question_text
        self.complexity = complexity
        self.correct_answer = correct_answer

    def __repr__(self):
        return f"Текст вопроса: {self.question_text}, Сложность: {self.complexity}, Правильный ответ: {self.correct_answer} \n"

    def get_points(self) -> int:
        """
        Возврат очков за правильный ответ
        """
        match self.complexity:
            case 1:
                return 10
            case 2:
                return 20
            case 3:
                return 30
            case 4:
                return 40
            case 5:
                return 50
            case _:
                return 0

    def is_correct(self) -> bool:
        """
        Проверка правильности ответа
        """
        return self.correct_answer == self.user_response

    def build_question(self) -> None:
        """
        Вывод вопроса
        """
        print(f"Вопрос: {self.question_text}")
        print(f"Сложность: {self.complexity}/5")

    def build_feedback(self) -> None:
        """
        Вывод информации о правильности ответа
        """

        if self.is_correct():
            print(f"Ответ верный, получено {self.get_points()}")
        else:
            print(f"Ответ неверный, верный ответ {self.correct_answer}")
