import ast
import random

# Список встроенных функций и переменных
BUILTINS = set(dir(__builtins__))
BUILTIN_VARIABLES = {
    "__name__",
    "__file__",
    "__builtins__",
    "__doc__",
    "__package__",
    "__spec__",
    "__annotations__",
    "__loader__",
    "__cached__",
}


def shit(filename, power):
    def convert_to_expression(number):
        while True:
            mul_shift = random.randint(
                -(2 ** (int(power**0.5))), (2 ** (int(power**0.5)))
            )
            if mul_shift != 0:
                break

        shift = random.randint(-(2**power), 2**power)
        shift_negative = shift < 0

        return f"(({number * mul_shift + shift} {'+' if shift_negative else '-'} {abs(shift)}) // {mul_shift})"

    class NumberTransformer(ast.NodeTransformer):
        def visit_Constant(self, node):
            if isinstance(node.value, int):
                expression = convert_to_expression(node.value)
                return ast.parse(expression, mode="eval").body
            return node

    def transform_numbers_in_file(filename):
        with open(filename, "r") as file:
            source = file.read()

        tree = ast.parse(source, filename)

        # Применяем трансформацию к дереву
        transformer = NumberTransformer()
        new_tree = transformer.visit(tree)

        # Генерируем измененный код
        new_code = ast.unparse(new_tree)

        # Сохраняем измененный код в файл
        with open(filename, "w") as file:
            file.write(new_code)

    # Пример использования
    transform_numbers_in_file(filename)
