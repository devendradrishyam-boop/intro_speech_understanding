def arithmetic(x, y):
    if isinstance(x, str) and isinstance(y, str):
        return x + y

    elif isinstance(x, (int, float)) and isinstance(y, str):
        return str(x) + y

    elif isinstance(x, str) and isinstance(y, (int, float)):
        return x * int(y)

    elif isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return x * y

    else:
        raise TypeError("Unsupported argument types for arithmetic function")