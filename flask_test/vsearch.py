def serch4voewls(phrase: str) -> set:
    """指定されたフレーズ内の母音を返す"""
    return vowels.intersection(set(phrase))

def search4letters(phrase: str, letters: str='aiueo') -> set:
    """phrase内のlettersの集合を返す"""
    return set(letters).intersection(set(phrase))

