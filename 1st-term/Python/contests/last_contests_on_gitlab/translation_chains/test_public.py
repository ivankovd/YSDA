import pytest

from translator import ANS_SIMPLE

def test_simple():
    assert ANS_SIMPLE == {"be": 1, "ceb": 1, "de": 1, "el": 1, "en": 1, "eo": 1, "es": 1, "et": 1, "eu": 1, "he": 1, "ne": 1, "te": 1}

