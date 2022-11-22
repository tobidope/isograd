import glob

import pytest

from area import *


def test_safe_are():
    data = "5 3".split()
    assert safe_area(data) == 16


@pytest.mark.parametrize("test_data,expected", zip(glob.glob("data/area/input*"), glob.glob("data/area/output*")))
def test_safe_area_examples(test_data, expected):
    with open(test_data) as ifh, open(expected) as ofh:
        data = ifh.read().splitlines()
        expected = ofh.read()
        result = safe_area(data)
        assert f"{result}" == expected
