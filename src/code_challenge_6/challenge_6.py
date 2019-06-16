def number_is_less_than_5(number):
    return number < 5


def number_is_odd(number):
    return number % 2 == 1


def number_is_even(number):
    return number % 2 != 1


def a_dodgy_function(input: str):
    return input


def an_even_more_dodgy_function():
    return None


def my_filter(input_list, function):
    try:
        return list(item for item in input_list if function(item))
    except:
        return input_list
