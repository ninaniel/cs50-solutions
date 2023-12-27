from um import count

def test_umstarts():
    assert count("um") == 1
    assert count("um, hello!") == 1
    assert count("Um... how are you?") == 1

def test_mixed_ums():
    assert count("maybe it's, um, little bit difficult") == 1
    assert count("he's name is, um... David") == 1
    assert count("Um, I guess, um.. I'm writing very um.. stupid things!") == 3

def test_um_in_words():
    assert count("Um, I'll have, um, numerous mistakes") == 2
    assert count("love this album!") == 0
    assert count("To sum up, that was a nice task!") == 0
