
def get_ver_num(ver_str: str) -> int:
    return int(ver_str[0])


def first_eq_last(ver_str: str) -> bool:
    check_str = ''
    # TODO: что тут происходит, вообще непонятно
    for index, symb in enumerate(ver_str):
        if not symb.isdigit():
            check_str = ver_str[index:]
    if check_str[0] is check_str[-1]:
        return True
    return False


def has_correct_length(ver_str: str) -> bool:
    # TODO: так тожде писать не нужно
    # return len(ver_str) == 10 в все -)
    if len(ver_str) == 10:
        return True
    return False


# TODO: это глоьбальной переменной - плохая идея. Лучше локальной в validate_ver()
ver_protocol = {
    1: [
        first_eq_last,
        has_correct_length
    ]
}


# TODO: Такое себе название, ты валидируешь строку, а не ее версию
def validate_ver(task_str: str) -> bool:
    # TODO: тут нужна обработка исключения, если первый символ не цифра
    ver_num = get_ver_num(task_str)
    for func in ver_protocol[ver_num]:
        if not func(task_str):
            return False
    return True
