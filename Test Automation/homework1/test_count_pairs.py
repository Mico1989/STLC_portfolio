import pytest
from count_pairs import count_vowel_consonant_pairs

@pytest.mark.parametrize("test_input, expected_result", [
    ("hello", 1),
    ("banana", 2),
    ("AEIObc", 1),
    ("", 0),
    ("12345", 0),
    ("PyThOn", 1),
    ("a!e@i#o$u%", 0),
])
def test_basic_cases(test_input, expected_result):
    assert count_vowel_consonant_pairs(test_input) == expected_result

@pytest.mark.parametrize("test_input, expected_result", [
    ("", 0),
    ("a!e@i#o$u%", 0),
    ("12345", 0),
    ("a", 0),
    ("b", 0),
    ("a1e2i3o4u", 0),
])
def test_edge_cases(test_input, expected_result):
    assert count_vowel_consonant_pairs(test_input) == expected_result


@pytest.mark.parametrize("test_input", [
    None,
    12345,
    ["hello"],
    {"text": "hi"}
])
def test_invalid_inputs(test_input):
    with pytest.raises(TypeError):
        count_vowel_consonant_pairs(test_input)


@pytest.mark.parametrize("test_input, expected_result", [
    ("a" * 1000 + "b" * 1000, 1),
    ("ab" * 1000, 1000),
    ("a1e2i3o4u" * 10000, "int"),  # Ovdje ne testiraš konkretnu vrijednost već tip
])
def test_large_inputs(test_input, expected_result):
    result = count_vowel_consonant_pairs(test_input)
    if expected_result == "int":
        assert isinstance(result, int)
    else:
        assert result == expected_result

