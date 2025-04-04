import pytest
from pyflirt.pyflirt import (
    get_flirt,
    get_flirts,
    LANGUAGE_VALUES,
    TYPES_VALUES,
    LanguageNotFoundError,
    TypeNotFoundError,
)

invalid_values = ["", "123", "xyz"]

def test_get_flirt_default_returns_string():
    assert isinstance(get_flirt(), str)

def test_get_flirt_valid_languages():
    for lang in LANGUAGE_VALUES:
        flirt = get_flirt(language=lang)
        assert isinstance(flirt, str)

def test_get_flirt_valid_types():
    for t in TYPES_VALUES:
        flirt = get_flirt(type=t)
        assert isinstance(flirt, str)

def test_get_flirt_invalid_language_raises():
    for invalid_lang in invalid_values:
        with pytest.raises(LanguageNotFoundError):
            get_flirt(language=invalid_lang)

def test_get_flirt_invalid_type_raises():
    for invalid_type in invalid_values:
        with pytest.raises(TypeNotFoundError):
            get_flirt(type=invalid_type)

def test_get_flirt_valid_language_invalid_type_raises():
    for invalid_type in invalid_values:
        with pytest.raises(TypeNotFoundError):
            get_flirt(language="en", type=invalid_type)

def test_all_flirts_are_nonempty_strings():
    for lang in LANGUAGE_VALUES:
        flirts = get_flirts(language=lang, type="all")
        for flirt in flirts:
            assert isinstance(flirt, str)
            assert flirt.strip(), f"Empty flirt line found in language: {lang}"
