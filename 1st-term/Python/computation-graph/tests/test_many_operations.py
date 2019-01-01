from collections import Counter

from compute_graph import ComputeGraph
from compute_graph.operation import Map, Fold, Reduce, Sort


def get_simple_data():
    return [
        {"1": 1, "2": 2},
        {"1": 3, "2": 4},
        {"1": 5, "2": 6},
        {"1": 7, "2": 8}
    ]


def mapper_1(r):
    yield {
        "2": r["1"]
    }


def sum_columns_folder(state, record):
    for column in state:
        state[column] += record[column]
    return state


def test_simple_fold():
    g = ComputeGraph(inputs=get_simple_data(), outputs=[],
                     save_to_variable=True)
    g.add(Map(mapper=mapper_1))
    g.add(Fold(folder=sum_columns_folder, state={"2": 0}))
    g.compile()
    g.run()
    resp = [
        {"2": 16}
    ]
    assert g.output_node.output == resp


def tokenizer_mapper(r):
    """
    splits rows with 'text' field into set of rows with 'token' field
    (one for every occurence of every word in text)
    """
    tokens = r['text'].split()
    for token in tokens:
        yield {
            'doc_id': r['doc_id'],
            'word': token,
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


easy_word_count = [
    {'doc_id': 0, 'text': 'Artem a b c d Nastya a b c d Roma'},
    {'doc_id': 1, 'text': 'Artem e f g  Nastya e f g h Roma'},
]


def test_word_count():
    graph = ComputeGraph(inputs=easy_word_count, outputs=[],
                         save_to_variable=True)

    graph.add(Map(mapper=tokenizer_mapper))
    graph.add(Sort(by='word'))
    graph.add(Reduce(reducer=term_frequency_reducer, key='word'))
    graph.compile()
    graph.summary()

    graph.run()

    assert graph.output_node.output == [{'word': 'Artem', 'count': 2},
                                        {'word': 'Nastya', 'count': 2},
                                        {'word': 'Roma', 'count': 2},
                                        {'word': 'a', 'count': 2},
                                        {'word': 'b', 'count': 2},
                                        {'word': 'c', 'count': 2},
                                        {'word': 'd', 'count': 2},
                                        {'word': 'e', 'count': 2},
                                        {'word': 'f', 'count': 2},
                                        {'word': 'g', 'count': 2},
                                        {'word': 'h', 'count': 1}]
