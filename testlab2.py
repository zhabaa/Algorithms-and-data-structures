class ExpressionError(Exception):
    """Кастомное исключение для ошибок в выражении"""
    pass


class ExpressionEvaluator:
    def __init__(self, expr: str):
        self.expr = expr.strip()

    def check_expression(self):
        """Проверка корректности выражения"""
        if not self.expr.endswith("="):
            raise ExpressionError("Выражение должно заканчиваться '='")

        expr = self.expr[:-1]  # убираем '='

        # Проверка баланса скобок
        stack = []
        for char in expr:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if not stack:
                    raise ExpressionError("Лишняя закрывающая скобка")
                stack.pop()
        if stack:
            raise ExpressionError("Не хватает закрывающих скобок")

        # Проверка на деление на 0
        if "/0" in expr.replace(" ", ""):
            raise ExpressionError("Деление на 0 запрещено")

        return expr

    def to_postfix(self, expr: str):
        """Перевод в обратную польскую запись (ОПЗ)"""
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
        output = []
        stack = []

        number = ""
        for char in expr:
            if char.isdigit() or char == ".":  # число (включая вещественные)
                number += char
            else:
                if number:
                    output.append(number)
                    number = ""

                if char in precedence:
                    while (stack and stack[-1] != "("
                           and precedence.get(stack[-1], 0) >= precedence[char]):
                        output.append(stack.pop())
                    stack.append(char)
                elif char == "(":
                    stack.append(char)
                elif char == ")":
                    while stack and stack[-1] != "(":
                        output.append(stack.pop())
                    stack.pop()  # убираем "("
                elif char.strip() == "":
                    continue
                else:
                    raise ExpressionError(f"Недопустимый символ: {char}")

        if number:
            output.append(number)

        while stack:
            output.append(stack.pop())

        return output

    def eval_postfix(self, postfix):
        """Вычисление выражения в ОПЗ"""
        stack = []
        for token in postfix:
            if token.replace(".", "", 1).isdigit():  # число
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    if b == 0:
                        raise ExpressionError("Деление на 0")
                    stack.append(a / b)
        return stack[0]

    def evaluate(self):
        expr = self.check_expression()
        postfix = self.to_postfix(expr)
        return self.eval_postfix(postfix)


# Пример использования
if __name__ == "__main__":
    expr = input("Введите выражение: ")
    try:
        evaluator = ExpressionEvaluator(expr)
        result = evaluator.evaluate()
        print("Результат:", result)
    except ExpressionError as e:
        print("Ошибка:", e)
