import pytest
from pyflirt.pyflirt import search_flirts, get_flirts

def test_search_flirts_finds_matches():
    all_flirts = get_flirts(language="en", type="all")
    if not all_flirts:
        pytest.skip("No flirts available to test with.")
    
    keyword = all_flirts[0].split()[0]  # Use a word from an existing flirt
    results = search_flirts(keyword=keyword, language="en", type="all")

    assert isinstance(results, list)
    assert any(keyword.lower() in line.lower() for line in results)

def test_search_flirts_no_match():
    keyword = "nonexistentkeyword987654"
    results = search_flirts(keyword=keyword, language="en", type="all")
    assert isinstance(results, list)
    assert len(results) == 0

def test_search_flirts_case_insensitive():
    # Find a keyword in lowercase and use it in uppercase
    flirts = get_flirts(language="en", type="simple")
    if not flirts:
        pytest.skip("No simple English flirts to test with.")
    
    keyword = flirts[0].split()[0]  # Take a word from a flirt line
    results_lower = search_flirts(keyword=keyword.lower(), language="en", type="simple")
    results_upper = search_flirts(keyword=keyword.upper(), language="en", type="simple")

    assert results_lower == results_upper
