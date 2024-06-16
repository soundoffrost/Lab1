import pytest
import re
from main import Node
from main import queryBridgeWords

nodes = {}
with open('test.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    # 进行匹配的正则表达式
    words = re.findall(r'\b[A-Za-z]+\b', content)
    nodelast = Node()
    nodenow = Node()
    for word in words:
        # print("本轮开始last=",nodelast.label,",now=",nodenow.label)
        if word not in nodes:
            nodes[word] = Node(word)
            nodenow = nodes[word]
            if nodelast is not None:
                # print("last=", nodelast.label, ",now=", nodenow.label)
                if nodenow not in nodelast.outgoing_edges:
                    nodelast.add_edge_to(nodenow)
                else:
                    nodelast.update_edge_weight(nodenow)
        else:
            nodenow = nodes[word]
            if nodelast is not None:
                # print("last=", nodelast.label, ",now=", nodenow.label)
                if nodenow not in nodelast.outgoing_edges:
                    nodelast.add_edge_to(nodenow)
                else:
                    nodelast.update_edge_weight(nodenow)
        nodelast = nodenow

@pytest.mark.parametrize("word1, word2, expected_output",[
    ('error', 'To', None),
    ('To', 'error', None),
    ('To', 'strange', [nodes['explore']]),
    ('To', 'new', None),
])

def test_query_bridge_words(word1, word2, expected_output):
    result = queryBridgeWords(word1, word2,nodes)
    assert result == expected_output