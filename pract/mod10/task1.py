import re
import doctest

def check_password(password: str) -> bool:
    """
    >>> check_password("rtG3FG!Tr^e")
    True
    >>> check_password("aA1!*!1Aa")
    True
    >>> check_password("oF^a1D@y5e6")
    True
    >>> check_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> check_password("пароль")
    False
    >>> check_password("password")
    False
    >>> check_password("qwerty")
    False
    >>> check_password("lOngPa$$$W0Rd")
    False
    """
    return re.match(r'(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.{2,}[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}', password) != None and re.search(r'[0-9a-zA-Z!@#$%^&*](.)\1{2,}', password) == None

doctest.testmod()