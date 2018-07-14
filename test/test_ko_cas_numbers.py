"""Unit tests for the number dictionary."""

import pytest

from plover_korean.system.cas.dictionaries.ko_cas_numbers import (
    lookup,
    reverse_lookup,
    OPERATOR_ATTACH
)


class TestLookup(object):
    """Tests the cases of lookup."""

    def test_length_zero(self):
        strokes = ()
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_length_one(self):
        strokes = ('12',)
        text = lookup(strokes)
        assert text == f'12{OPERATOR_ATTACH}'

    def test_length_two(self):
        strokes = ('1', '0')
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_contains_initial(self):
        strokes = ('1ㅎ',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_contains_final(self):
        strokes = ('1-ㅎ',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_contains_non_star_medial(self):
        strokes = ('1ㅏ',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_separated_numbers(self):
        strokes = ('1-9',)
        text = lookup(strokes)
        assert text == f'19{OPERATOR_ATTACH}'

    def test_edge_numbers_right(self):
        strokes = ('2-6',)
        text = lookup(strokes)
        assert text == f'26{OPERATOR_ATTACH}'

    def test_edge_numbers_left(self):
        strokes = ('5-7',)
        text = lookup(strokes)
        assert text == f'57{OPERATOR_ATTACH}'

    def test_edge_numbers_both(self):
        strokes = ('5-6',)
        text = lookup(strokes)
        assert text == f'56{OPERATOR_ATTACH}'

    def test_reverse_key(self):
        strokes = ('3*8',)
        text = lookup(strokes)
        assert text == f'83{OPERATOR_ATTACH}'

    def test_long_number(self):
        strokes = ('125-70',)
        text = lookup(strokes)
        assert text == f'12570{OPERATOR_ATTACH}'

    def test_long_number_reverse(self):
        strokes = ('125*70',)
        text = lookup(strokes)
        assert text == f'07521{OPERATOR_ATTACH}'

    def test_max_number(self):
        strokes = ('12345-67890',)
        text = lookup(strokes)
        assert text == f'1234567890{OPERATOR_ATTACH}'

    def test_max_number_reverse(self):
        strokes = ('12345*67890',)
        text = lookup(strokes)
        assert text == f'0987654321{OPERATOR_ATTACH}'

    def test_non_sequential_number(self):
        strokes = ('18302',)
        with pytest.raises(KeyError):
            lookup(strokes)


@pytest.mark.xfail(reason='Fails to construct * and split cases correctly.')
class TestReverseLookup(object):
    """Tests the cases of reverse_lookup."""

    def test_empty_string(self):
        text = ''
        strokes = reverse_lookup(text)
        assert strokes == []

    def test_non_sequential_number(self):
        text = '18302'
        strokes = reverse_lookup(text)
        assert strokes == []

    def test_increasing_number(self):
        text = '13'
        strokes = reverse_lookup(text)
        assert strokes == [('13',)]

    def test_decreasing_number(self):
        text = '872'
        strokes = reverse_lookup(text)
        assert strokes == [('2*78',)]

    def test_starts_with_zero(self):
        text = '0631'
        strokes = reverse_lookup(text)
        assert strokes == [('13*60',)]

    def test_ends_with_zero(self):
        text = '2590'
        strokes = reverse_lookup(text)
        assert strokes == [('25-90',)]

    def test_max_number(self):
        text = '123456780'
        strokes = reverse_lookup(text)
        assert strokes == [('12345-67890',)]

    def test_max_number_reverse(self):
        text = '0987654321'
        strokes = reverse_lookup(text)
        assert strokes == [('12345*67890',)]

    def test_separated_numbers(self):
        text = '12347'
        strokes = reverse_lookup(text)
        assert strokes == [('1234-7',)]
