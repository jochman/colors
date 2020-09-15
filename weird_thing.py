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


dct = {
    'Dean': 'Arbel',
    'Yana': 'Orhov',
    'Bar': 'Hochman',
    'Number??': 0
}
print(weird_thing(dct))
