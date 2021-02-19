from random import randint


def generation() -> str:
    """Generates 50 characters length hash_code to be used for a ticket."""
    hash_code = ''
    for i in range(50):
        hash_code += chr(randint(48, 122))

    return hash_code
