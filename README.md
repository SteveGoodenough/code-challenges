# code-challenges

## code-challenge-21
https://coding-challenges.jl-engineering.net/challenges/challenge-21/

A Sudoku solver.

My initial approach was to start with using solving methods a human would have to use to solve a puzzle, but then it occurred to me to see what a brute force attack solver would look like (trying combinations until a solution(s) were found).

For a good Sudoku there should only be one solution and this brute force method works really well. As soon as there are multiple solutions the recursion in this solution can take time to find all solutions. However, my initial approach here would not have helped as you would need to track the previous solutions to find the range of solutions possible.

The upshot of this approach is that it solves those incredibly difficult puzzles that a human would need all logic methods to solve really quickly.

So again, a code challenge used recursion in the solution. Here it works well in trying out all possible numbers in each empty square and backing up if a number in a square results in an unsolvable puzzle.

The result is that this method can find all possible solutions too.

Luckily(?) for me the test puzzle of an unsolvable grid actually worked and resulted in the empty list being returned.


## code-challenge-19
https://coding-challenges.jl-engineering.net/challenges/challenge-19/

Reference id is a string containing the x, y coordinates, the orientation and the trolley id, each separated with a colon.

For obscuring the generated reference id I used base64 encode/decode. Not complex but achieves what was specified.

I took the decision to ignore a move command if the square wasn't clear, therefore you get the same reference id back. 

As I had a function that allowed for moving East (right), I decided for other directions to use a novel solution a colleague used for a previous challenge (Sokoban) where he rotated the board allowing you to use the same "move right" function.

That means we can use the following rotations to allow for all four directions:

| Rotation | Moving | Orientation |
|---------:|--------|:-----------:|
|        0 | right  | E           |
|       90 | up     | N           |
|      180 | left   | W           |
|      270 | down   | S           |

Rotating the map took some doing but I found this one liner on the net that rotates an array using the `zip` function in combination with reversing a list using `[::-1]`. `zip` returns tuples but can then list comprehension to convert back to a list of lists: `[list(line) for line in zip(*map[::-1])]`. 

Refactoring this using the reversed function makes it more readable, i.e. `return [list(line) for line in zip(*reversed(map))]`

For rotating 180 and 270 degrees, I just repeat the turn 90 function. Maybe a future refactor can make this more efficient but I got bored of trying different approaches for now.

Rotating the map means the trolley location has to alter too from the passed x, y coordinates.

| Rotation | new x   | new y   |
|---------:|---------|---------|
|        0 | x       | y       |
|       90 | depth-y | x       |
|      180 | width-x | depth-y |
|      270 | y       | width-x |

### ToDo:
* [ ] Merge the constants into a single dictionary
* [ ] Passing map, coordinates and location a lot of the time, maybe move into a single structure?
* [ ] Rotating just uses a rotate 90 function and does it twice for 180 degrees, three times for 270 degrees - find a more efficient way of doing this.
* [ ] After all said and done is rotating still a good idea? I didn't use it for moving, just when generating the view.

## code-challenge-18
https://coding-challenges.jl-engineering.net/challenges/challenge-18/

* Create a function that takes the first node of a linked list of strings and returns a string
that can be printed out to show all of the members of the list.
Using the sample code above getDescription(firstNode) should return "hello world null".

* Create a function to add a value onto the end of a list.
So addToList(firstNode, "!") and then running getDescription(firstNode) should result in "hello world ! null".

* Create a function that takes a linked list of strings and returns a linked list of integers.
If the string cannot be converted to an integer, convert it to 0.

* Create a function that takes a linked list of strings and reverses it.
So a list with a description of "a b c d e f null" would be converted to a list with a description of "f e d c b a null".

I substituted `None` for `null` in the examples as this is python.

I ended up using recursion to solve these challenges which works ok.

For challenge three I really could have used the same class to hold the integer values as python is not strict about types but it's more readable having an Integer Node list.

The last challenge was tough as linked lists are really only for reading sequentially from start to end (unless you use a linked list with a pointer linking to the previuous item) but then I realised I had an append function which I could use while reading the list from front to end to append each item to the new list, again using recursion to work through the linked list.

I think I could have had all these functions as functions of the class (like `__str__`) but the challenge did ask for _external_ functions.


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
