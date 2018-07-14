"""Core functionality for the CAS-based Korean stenography system."""

from typing import Tuple, List
import operator

from plover_korean.system.cas.util import (
    get_stroke_groups,
    compare_numeric_text
)


LONGEST_KEY = 1
OPERATOR_ATTACH = '{^}'
REVERSE_KEY = '*'


def lookup(strokes: Tuple[str]) -> str:
    """Get the text that the provided strokes would output.

    Args:
        strokes: A tuple of strokes to look up text for.

    Returns:
        The text text output for the stroke.

    Raises:
        KeyError: The lookup failed to find any matching text.
    """

    if len(strokes) != LONGEST_KEY:
        raise KeyError()
    initial, medial, final, numbers = get_stroke_groups(strokes[0])

    # An asterisk is used to reverse the numeric output and is the only
    # acceptable medial for this dictionary
    reverse_output = (REVERSE_KEY in medial and len(medial) == 1)

    if not numbers:
        raise KeyError()
    elif initial or final:
        raise KeyError()
    elif medial and not reverse_output:
        raise KeyError()

    output = numbers[::-1] if reverse_output else numbers

    return f'{output}{OPERATOR_ATTACH}'


def reverse_lookup(text: str) -> List[Tuple[str]]:
    """Gets the possible strokes that would result in the provided text.

    Args:
        text: The text to look up strokes for.

    Returns:
        A list of stroke tuples. An empty list will be returned if no possible
        strokes were found.
    """

    # TODO: Disable for now as this is broken.
    #       See unit tests.
    return []

    original_text = text

    # Need to swap where 0 is if it exists for numeric comparisons
    if text.startswith('0'):
        text = text[1:] + '0'
    elif text.endswith('0'):
        text = '0' + text[:-1]

    # We can only generate, and therefore look up, increasing or decreasing
    # numbers like 12...90 or 09...21, so limit the search to that
    is_decreasing = compare_numeric_text(text, operator.lt)
    if not is_decreasing and not compare_numeric_text(text, operator.gt):
        return []

    # Just shove the reverse key at the end to be lazy
    output = original_text
    if is_decreasing and len(output) > 1:
        output += REVERSE_KEY

    return [(output,)]
