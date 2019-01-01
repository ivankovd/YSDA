import sys
import random
import re


def prepare_to_british_scientists(text, letters_to_shuffle_nm):
    words_regexp = re.compile(r"\w{3,}")
    words = re.findall(words_regexp, text)
    for i, word in enumerate(words):
        for _ in range(int(letters_to_shuffle_nm // 2)):
            from_ = random.randint(a=1, b=len(word) - 2)
            to_ = random.randint(a=1, b=len(word) - 2)
            from_char, to_char = word[from_], word[to_]
            word = word[:from_] + to_char + word[from_ + 1:]
            word = word[:to_] + from_char + word[to_ + 1:]

        text = re.sub(words[i], word, text)
    return text
