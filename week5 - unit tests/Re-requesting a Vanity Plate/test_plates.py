from plates import is_valid
# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def test_min_max():
    assert is_valid("q") == False
    assert is_valid("qw") == True
    assert is_valid("QWe") == True
    assert is_valid("QWer") == True
    assert is_valid("QWERT") == True
    assert is_valid("qwerty") == True
    assert is_valid("QwertyU") == False

def test_first_two():
    assert is_valid("qw") == True
    assert is_valid("q1") == False
    assert is_valid("1q") == False
    assert is_valid("12") == False

def test_middle_num():
    assert is_valid("qwe123") == True
    assert is_valid("qw1234") == True
    assert is_valid("qw123e") == False
    assert is_valid("qw1w2e") == False

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_symbols():
    assert is_valid("q.") == False
    assert is_valid("qw/123") == False
    assert is_valid("qwe rt") == False
