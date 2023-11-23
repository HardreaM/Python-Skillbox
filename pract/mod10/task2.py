import re
import doctest

def validate(color:str) -> bool:
    """
    >>> validate('rgb(255, 255, 255)')
    True
    >>> validate('rgb(10%, 20%, 0%)')
    True
    >>> validate('#21f48D')
    True
    >>> validate('#888')
    True
    >>> validate('hsl(200,100%,50%)')
    True
    >>> validate('hsl(0, 0%, 0%)')
    True
    >>> validate('rgb(257, 50, 10)')
    False
    >>> validate('#2345')
    False
    >>> validate('ffffff')
    False
    >>> validate('hsl(34%, 20%, 50%)')
    False
    >>> validate('hsl(20, 10, 0.5)')
    False
    """
    patterns = [r'^rgb\((\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), (\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?), (\d{1,2}%?|1?\d{1,2}%?|2[0-4]\d%?|25[0-5]%?)\)$',
                r'^#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})$',
                r'^hsl\((\d{1,3}|[1-9]\d{0,2}),\s*(100%|[1-9]?\d%|0%),\s*(100%|[1-9]?\d%|0%)\)$']

    for pattern in patterns:
        if re.match(pattern, color):
            return True
    return False

doctest.testmod()