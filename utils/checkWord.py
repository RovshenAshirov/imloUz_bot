from utils.uzwords import words
from difflib import get_close_matches

def checkWord(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = word
    elif 'х' in word:
        word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words)) 
    elif 'ҳ' in word:
        word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words)) 

    return {'available': available, 'matches' : matches}
     