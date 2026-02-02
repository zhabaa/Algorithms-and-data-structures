class ExpressionEvaluator:
    def __init__(self, expr: str):
        self.expr = expr.strip()

    def validate_equal(self):
        if not self.expr.endswith("="):
            raise Exception("Expression must end with '='")

        self.expr = expr.strip()[:-1]

    def validate_parentheses(self):
        stack = []

        for char in expr:
            if char == "(":
                stack.append(char)

            elif char == ")":
                if not stack:
                    raise Exception("Close parentheses excess")

                stack.pop()

        if stack:
            raise Exception("Close parentheses missing")

    def validate_zero_division(self):
        if "/0" in expr.replace(" ", ""):
            raise Exception("Zero division")

    def check_expression(self):
        self.validate_equal()
        self.validate_parentheses()
        self.validate_zero_division()

    def to_postfix(self):  # potsfix polish notation
        precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

        output = []
        stack = []

        number = ""
        expr = self.expr

        for char in expr:
            if char.isdigit() or char == ".":
                number += char

            else:
                if number:
                    output.append(number)
                    number = ""

                if char in precedence:
                    while (
                        stack
                        and stack[-1] != "("
                        and precedence.get(stack[-1], 0) >= precedence[char]
                    ):
                        output.append(stack.pop())

                    stack.append(char)

                elif char == "(":
                    stack.append(char)

                elif char == ")":
                    while stack and stack[-1] != "(":
                        output.append(stack.pop())

                    stack.pop()

                elif char.strip() == "":
                    continue

                else:
                    raise Exception(f"Unsopported symbol: {char}")

        if number:
            output.append(number)

        while stack:
            output.append(stack.pop())

        return output

    def eval_postfix(self, postfix):  # stack evaluation
        stack = []

        for token in postfix:
            if token.replace(".", "", 1).isdigit():
                stack.append(float(token))

            else:
                b = stack.pop()
                a = stack.pop()

                try: # if -> match case -> dictionary; check KeyError 
                    res = {
                        "+": a + b,
                        "-": a - b,
                        "*": a * b,
                        "/": a / b if b != 0 else Exception("Zero division"),
                    }

                    stack.append(res[token])

                except KeyError:
                    raise Exception(f"Unsopported symbol: {token}")

        return stack[0]

    def evaluate(self):
        self.check_expression()
        postfix = self.to_postfix()
        return self.eval_postfix(postfix)


if __name__ == "__main__":
    expr = input("Enter expression: ")

    try:
        eval = ExpressionEvaluator(expr)
        result = eval.evaluate()
        print("Result:", result)

    except Exception as e:
        print("Error:", e)
