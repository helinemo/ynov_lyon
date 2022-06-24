from main import count_char, check_if_maj, check_if_special_char, check_invalid_special_char, check_if_password_valid

def test_count_char():
    input = ["blabla", "45794278", "Bonjour!!!"]
    expected = [6, 8, 10]
    result = [count_char(password) for password in input]
    assert expected == result

def test_check_invalid_special_char():
    """
        banned char: '@', '=', '+', ' '
    """
    input = ["Bonjour", "789blabla-", "Bonjour@", "blabla oui", 'blabla=', 'bon+jour']
    expected = [True, True, False, False, False, False]
    result = [check_invalid_special_char(password) for password in input]
    assert expected == result

def test_check_if_maj():
    input = ["Bonjour", "bonjour", "bonJour", "bonjouR", "BonJouRR", "789456"]
    expected = [True, False, True, True, True, False]
    result = [check_if_maj(password) for password in input]
    assert expected == result

def test_check_if_special_char():
    """
        required char: "!", "#", ";"
    """
    input = ["Bonjour!", "bon#jour", ";bonjour", "#bonjour;", "@bonjour", "bonjour", "78945"]
    expected = [True, True, True, True, False, False, False]
    result = [check_if_special_char(password) for password in input]
    assert expected == result

def test_check_if_password_valid():
    input = ["Bonjourrrrr@", "bonjourrrr", "Bonjourrrr!", "bonjourrr!", "Bonjo urrrr!", "rrrRrrrrrrr!"]
    expected = [False, False, True, False, False, True]
    result = [check_if_password_valid(password) for password in input]
    assert expected == result