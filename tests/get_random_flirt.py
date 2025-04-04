import pytest
from pyflirt.pyflirt import get_random_flirt, LANGUAGE_VALUES, TYPES_VALUES

def test_get_random_flirt_runs_without_error():
    flirt = get_random_flirt()
    assert isinstance(flirt, str)
    assert flirt.strip() != ""

def test_get_random_flirt_validity():
    # Run multiple times to check language/type randomness still produces valid results
    for _ in range(20):
        flirt = get_random_flirt()
        assert isinstance(flirt, str)
        assert flirt.strip()  # Ensure it's not empty
