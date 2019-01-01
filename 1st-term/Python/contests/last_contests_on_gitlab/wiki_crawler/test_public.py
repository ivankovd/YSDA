import pytest

from crawler import WIKI_PAGE_DEPTHS


class TestCrawler:
    def test_simple(self):
        page_depths = {
            "Sherutni_patrin": 0,
            "Romano_lekhipen": 1,
            "Sinti": 1,
        }
        for p, d in page_depths.items():
            assert WIKI_PAGE_DEPTHS[p] == d
