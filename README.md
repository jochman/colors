```python
import requests
from mypy import api

def run_mypy(file_path):
    print(api.run([file_path])[0])
```

<center> <h1>The magic of Typed Python</h1>
<img src="https://media.giphy.com/media/E6jscXfv3AkWQ/giphy.gif"><img src="https://media.giphy.com/media/ws0sZhwes8l1K/giphy.gif"></center>

## What is type annotation?


```python
from helper import swap
def weird_thing(arg):
    build = {}
    for key, value in arg.items():
        build = {}
        build[key.upper()] = value.lower()
    return swap(build)

```

# What??

```2: def weird_thing(arg)``` -> <h3> What is **arg**?</h3>

```6: return swap(build)``` -> <h3> What returned?</h3>

## Is docstring is enough?


```python
from helper import swap
def weird_thing(arg):
    """Get a dict and tranform its keys to upper and value lower. Then swapping key with values them.

    Arguments:
        arg: A dictionary to transform.
    
    Returns:
        swapped dict with former keys to upper and values to lower.
    """
    build = {}
    for key, value in arg.items():
        build[key.upper()] = value.lower()
    return swap(build)
```

# IS THAT ENOUGH?!?!?!
![](https://media.giphy.com/media/YQk8nXloVftzW/giphy.gif)

## So what should we do?

# REMOVE THE DOCTEST





![](https://media.giphy.com/media/PkoZpdQllFpXwJX6Tp/giphy.gif)


```python
from typing import Dict
from helper import swap
def weird_thing(arg: Dict[str, str]) -> Dict:
    """Get a dict and tranform its keys to upper and value lower. Then swapping key with values them.

    Arguments:
        arg: A dictionary to transform.
    
    Returns:
        swapped dict with former keys to upper and values to lower.
    """
    build = {}
    for key, value in arg.items():
        build[key.upper()] = value.lower()
    return swap(build)
```

## Cool! what does python do with that information?
### Well, lets see!


```python
dct = {
    'Dean': 'Arbel',
    'Yana': 'Orhov',
    'Bar': 'Hochman',
    'Number??': '1'
}
print(weird_thing(dct))
```

    {'arbel': 'DEAN', 'orhov': 'YANA', 'hochman': 'BAR', '1': 'NUMBER??'}


The dict is valid. what happens if it's not valid?


```python
dct = {
    'Dean': 'Arbel',
    'Yana': 'Orhov',
    'Bar': 'Hochman',
    'Number??': 0
}
print(weird_thing(dct))
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-6-d5ce6d60b376> in <module>
          5     'Number??': 0
          6 }
    ----> 7 print(weird_thing(dct))
    

    <ipython-input-2-88071b540756> in weird_thing(arg)
         12     build = {}
         13     for key, value in arg.items():
    ---> 14         build[key.upper()] = value.lower()
         15     return swap(build)


    AttributeError: 'int' object has no attribute 'lower'


So what python does with that problem?

![](https://media.giphy.com/media/baPIkfAo0Iv5K/giphy.gif)

## If no one validates it, who cares?

# MYPY CARES
![](https://camo.githubusercontent.com/68c7827eeb796f3a664f48f5657c04e65e04ae6e/687474703a2f2f6d7970792d6c616e672e6f72672f7374617469632f6d7970795f6c696768742e737667)


```python
'''dct = {
    'Dean': 'Arbel',
    'Yana': 'Orhov',
    'Bar': 'Hochman',
    'Number??': 0
}
print(weird_thing(dct))'''
run_mypy("./weird_thing.py")
```

    weird_thing.py:26: error: Argument 1 to "weird_thing" has incompatible type "Dict[str, object]"; expected "Dict[str, str]"
    Found 1 error in 1 file (checked 1 source file)
    



```python
from typing import List
dct: List = 'I am actually a string!'
```


```python
from typing import List
dct: List = 'I am actually a string!'

run_mypy('./wrong_typing.py')
```

    wrong_typing.py:2: error: Incompatible types in assignment (expression has type "str", variable has type "List[Any]")
    Found 1 error in 1 file (checked 1 source file)
    


## Python 3 variable type annotation


```python
from typing import Dict
loved_colors: Dict = {
    'Red': 0,
    'Blue': 4,
    'Purple': 90001
    }
print(loved_colors)
```

    {'Red': 0, 'Blue': 4, 'Purple': 90001}


## The **RIGHT** type annotation is to not annotate at all


```python
loved_colors = {
    'Red': 0,
    'Blue': 4,
    'Purple': 90001
    }
print(loved_colors)
```

    {'Red': 0, 'Blue': 4, 'Purple': 90001}


# Where problems start



```python
from typing import Dict, Optional
class GetColors:
    @classmethod
    def loved_colors(cls) -> Optional[Dict]:
        color_love_url = "http://my-json-server.typicode.com/jochman/colors/love"
        if res := requests.get(color_love_url, verify=False).json():
            return res
        return None

    @classmethod
    def hated_colors(cls)-> Optional[Dict]:
        color_love_url = "http://my-json-server.typicode.com/jochman/colors/hate"
        if res := requests.get(color_love_url, verify=False).json():
            return res
        return None

```


```python
loved_colors = GetColors.loved_colors()

print(loved_colors.keys())

run_mypy('./no_annotation.py')
```

    dict_keys(['Red', 'Blue', 'Purple'])
    no_annotation.py:3: error: Item "None" of "Optional[Dict[Any, Any]]" has no attribute "keys"
    Found 1 error in 1 file (checked 1 source file)
    


How does he knew what to do?

MYPY sees: `def loved_colors() -> Optional[Dict]`

So he knows that there're two options of return types: `[None, dict]`

Then, he sees `loved_colors.keys()`. MYPY knows that `dict` type has the `keys` function, But `None` got nothing in it.

#### Boom! an error!


## Common case: The easy way


```python
loved_colors = GetColors.loved_colors()  # type: ignore

print(loved_colors.items())
run_mypy('./typeignore.py')
```

    dict_items([('Red', 0), ('Blue', 4), ('Purple', 90001)])
    Success: no issues found in 1 source file
    


# `TYPE: IGNORE`? PANIC!
![](https://media.giphy.com/media/KmTnUKop0AfFm/giphy.gif)


```python
assert loved_colors is not None, 'Bad response from API'
print(loved_colors.keys())

```

    dict_keys(['Red', 'Blue', 'Purple'])



```python
if loved_colors is None:
    print('No colors, no love')
else:
    print(loved_colors.keys())
```

    dict_keys(['Red', 'Blue', 'Purple'])


## More types and how to annotate them:


```python
# Dicts and Lists: you can map the keys\values types
from typing import List, Dict
french_wars: List[str]
french_wars_starting_year: Dict[str, int]

# What if something can be None? Use Optional!
from typing import Optional
phrase_of_the_day: Optional[str]

# Some return types? we got you with Union
from typing import Union
am_i_a_dict_or_list_or_none: Union[Dict, List]

# You can combine those
kabya_sharkan_or_hazir_yaml: Optional[Union[Dict, List]]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-20-26135c298303> in <module>
         10 # Some return types? we got you with Union
         11 from typing import Union
    ---> 12 am_i_a_dict_or_list_or_none: Optional[Dict, List]
    

    ~/.pyenv/versions/3.8.0/lib/python3.8/typing.py in inner(*args, **kwds)
        259         except TypeError:
        260             pass  # All real errors (not unhashable args) are raised below.
    --> 261         return func(*args, **kwds)
        262     return inner
        263 


    ~/.pyenv/versions/3.8.0/lib/python3.8/typing.py in __getitem__(self, parameters)
        362             return _GenericAlias(self, parameters)
        363         if self._name == 'Optional':
    --> 364             arg = _type_check(parameters, "Optional[t] requires a single type.")
        365             return Union[arg, type(None)]
        366         if self._name == 'Literal':


    ~/.pyenv/versions/3.8.0/lib/python3.8/typing.py in _type_check(arg, msg, is_argument)
        147         return arg
        148     if not callable(arg):
    --> 149         raise TypeError(f"{msg} Got {arg!r:.100}.")
        150     return arg
        151 


    TypeError: Optional[t] requires a single type. Got (typing.Dict, typing.List).


![](https://media.giphy.com/media/3oD3YveOJWdwIAfZ5e/giphy.gif)
