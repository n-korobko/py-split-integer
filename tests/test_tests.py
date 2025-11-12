from app.split_integer import split_integer

def test_one_part():
    assert split_integer(10, 1) == [10]

def test_even_split():
    assert split_integer(8, 2) == [4, 4]

def test_split_with_remainder():
    assert split_integer(10, 3) == [3, 3, 4]

def test_large_split():
    result = split_integer(100, 9)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert len(result) == 9
    assert sum(result) == 100

def test_almost_equal_parts():
    result = split_integer(32, 6)
    assert result == sorted(result)
    assert max(result) - min(result) <= 1
    assert len(result) == 6
    assert sum(result) == 32
