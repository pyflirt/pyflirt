import pytest
from itertools import islice
from pyflirt.pyflirt import loop, LANGUAGE_VALUES, TYPES_VALUES 

@pytest.mark.parametrize("language", LANGUAGE_VALUES)
@pytest.mark.parametrize("type_", TYPES_VALUES)
def test_loop_generator(language, type_):
    flirt_gen = loop(language=language, type=type_)

    # Take the first 5 items from the generator
    flirts = list(islice(flirt_gen, 5))

    assert len(flirts) == 5
    for flirt in flirts:
        assert isinstance(flirt, str)
        assert flirt.strip() != ""  # ensure it's not empty
        assert len(flirt) <= 200    # optional: check length constraint
