# code-challenges

## code-challenge-6
https://coding-challenges.jl-engineering.net/challenges/challenge-6/

I have 3 functions to pass true/false test on a passed number
* number_is_less_than_5
* number_is_even
* number_is_odd

Long winded method
```
    res = []
    for item in input_list:
        if function(item):
            res.append(item)
```

Using a lambda = bad!
```
    result = list(filter(lambda item: function(item), input_list))
```

Final simple method
```
    res = list(item for item in input_list if function(item))
```


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
