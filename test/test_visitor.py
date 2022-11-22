import glob

import pytest

from visitor import *

data = zip(glob.glob("data/visitor/input*"), glob.glob("data/visitor/output*"))


@pytest.mark.parametrize("test_data,expected", data)
def test_safe_area_examples(test_data, expected):
    with open(test_data) as ifh, open(expected) as ofh:
        lines = ifh.read().splitlines()
        expected = ofh.read()
        result = visitor(lines)
        assert f"{result}" == expected
