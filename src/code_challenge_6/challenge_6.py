def number_is_less_than_5(number):
    return number < 5 


def number_is_odd(number):
    return number % 2 == 1


def number_is_even(number):
    return number % 2 != 1


def my_filter(input_list, function):
    return list(item for item in input_list if function(item))
