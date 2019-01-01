import re
from collections import Counter

from compute_graph import ComputeGraph
from compute_graph.operation import Map, Reduce, Sort


def tokenizer_mapper(r):
    """
    splits rows with 'text' field into set of rows with 'token' field
    (one for every occurence of every word in text)
    """
    text = re.sub('[^A-Za-z]+', ' ', r['text'])
    tokens = text.split()
    for token in tokens:
        yield {
            'doc_id': r['doc_id'],
            'word': token.lower(),
        }


def term_frequency_reducer(records):
    """
    calculates term frequency for every word in doc_id
    """
    word_count = Counter()
    for r in records:
        word_count[r['word']] += 1
    for w, count in word_count.items():
        yield {
            'word': w,
            'count': count
        }


if __name__ == '__main__':
    graph = ComputeGraph(inputs='../data/text_corpus.txt',
                         outputs='../data/output/word_count.txt')
    graph.add(Map(mapper=tokenizer_mapper))
    graph.add(Sort(by='word'))
    graph.add(Reduce(reducer=term_frequency_reducer, key='word'))
    graph.compile()
    graph.summary()

    graph.run()
