import re
from collections import Counter

from compute_graph import ComputeGraph
from compute_graph.operation import Map, Reduce, Sort


def doc_count(records):
    cnt = len(records)
    for r in records:
        r['cnt_docs'] = cnt
        yield r


def tokenizer_mapper(r):
    """
    splits rows with 'text' field into set of rows with 'token' field
    (one for every occurence of every word in text)
    """
    text = re.sub('[^A-Za-z]+', ' ', r['text'])
    tokens = text.split()
    for token in tokens:
        if len(token) > 4:
            yield {
                'cnt_docs': r['cnt_docs'],
                'doc_id': r['doc_id'],
                'word': token.lower(),
            }


def one_doc_word_count_reducer(records):
    """
    calculates counts for every word in one doc_id
    """
    word_count = Counter()
    for r in records:
        word_count[r['word']] += 1
    for w, count in word_count.items():
        if count >= 2:
            yield {
                'cnt_docs': records[0]['cnt_docs'],
                'doc_id': records[0]['doc_id'],
                'word': w,
                'count_in_one_doc': count
            }


if __name__ == '__main__':
    graph = ComputeGraph(inputs='../data/text_corpus.txt',
                         outputs='../data/output/pmi.txt')
    graph.add(Reduce(reducer=doc_count))
    graph.add(Map(mapper=tokenizer_mapper))
    graph.add(Sort(by='word'))
    graph.add(Reduce(reducer=one_doc_word_count_reducer, key='word'))
    graph.compile()
    graph.summary()

    graph.run()
