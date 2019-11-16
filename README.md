# code-challenges

## code-challenge-16
https://coding-challenges.jl-engineering.net/challenges/challenge-16/

Create a function that accepts two strings containing roman numerals and returns as string containing a roman numeral which is the sum of the two roman numerals.

Decided easiest option was to have a function to convert from a roman numeral to a number, do a simple addition and then a function to convert from a number to a roman numeral.

Examples at https://www.romannumerals.org/converter gave a good set of tests to TDD against.

I don't have any validation code, Romans didn't have a character for zero and there were specific lower denomination options, e.g. IV = 1 before 5 (4), XL = 10 before 50 (40), CM = 100 before 1000 (900), so only pass valid roman numbers to my function!


## code-challenge-6
https://coding-challenges.jl-engineering.net/challenges/challenge-6/

I have 3 functions to pass true/false test on a passed number
* number_is_less_than_5
* number_is_even
* number_is_odd

Long winded method and concerned about mutability with the .append
```
    result = []
    for item in input_list:
        if function(item):
            result.append(item)
```

Using a lambda = bad!
```
    result = list(filter(lambda item: function(item), input_list))
```

Final simple method
```
    result = list(item for item in input_list if function(item))
```

Passing a "dodgy" function was interesting as using a_dodgy_function that took a string and returned the string the my_filter function took this as true so resulted in the whole list being passed back as required.

Tried with another function that took no input and passed None back, that broke it... so just surrounded the process in a try/except block


## Setup your python environnment

Use `pipenv` !! https://pipenv.readthedocs.io/en/latest/

### Setup the project

`pipenv install --dev`

### Run the tests with coverage

Anything less than 100% will fail

`pytest --cov=src`

### Lint the project

`flake8`

### Run continual testing

`ptw`
