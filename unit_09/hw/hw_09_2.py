"""
Закодируйте любую строку по алгоритму Хаффмана
"""


def node(name, parent=None, left=None, right=None, freq=0, leaf=False):
    return {'name': name,
            'parent': parent,
            'left': left,
            'right': right,
            'freq': freq,
            'leaf': leaf}


def make_nodes(string):
    return [node(name=c, freq=string.count(c), leaf=True) for c in set(string)]


def sort_nodes(ns):
    return sorted(ns, key=lambda x: x['freq'], reverse=True)


def tree(string):
    nodes = make_nodes(string)
    nodes = sort_nodes(nodes)
    nodes_len = len(nodes)
    nodes_done = []
    n = None

    if nodes_len == 1:
        return nodes

    while nodes_len > 1:
        left = nodes.pop()
        right = nodes.pop()
        n = node(name=left['name'] + right['name'],
                 left=left['name'],
                 right=right['name'],
                 freq=left['freq'] + right['freq'])
        nodes.append(n)
        nodes = sort_nodes(nodes)
        nodes_len = len(nodes)
        left['parent'] = n['name']
        right['parent'] = n['name']
        nodes_done.append(left)
        nodes_done.append(right)

    nodes_done.append(n)

    return nodes_done


def huffman_dict_new(string):
    chars = sorted(list(set(string)))
    nodes = tree(string)
    nodes_dict = {n['name']: n for n in nodes}

    if len(chars) == 1:
        return {chars[0]: '0'}

    ch_dict = {c: '' for c in chars}

    for c in chars:
        child_name = c
        child = nodes_dict[child_name]
        parent_name = child['parent']

        while parent_name:
            parent = nodes_dict[parent_name]
            if child_name == parent['left']:
                ch_dict[c] = '1' + ch_dict[c]
            elif child_name == parent['right']:
                ch_dict[c] = '0' + ch_dict[c]

            child_name = parent_name
            child = nodes_dict[child_name]
            parent_name = child['parent']

    return ch_dict


def huffman_encode(string, ch_dict):
    """

    :param string:
    :param ch_dict:
    :return:
    """
    return ''.join(ch_dict[c] for c in string)


if __name__ == '__main__':
    st = input('Введите непустую строку: ')
    assert len(st), 'Введена пустая строка!'

    h_dict = huffman_dict_new(st)
    st_encoded = huffman_encode(st, h_dict)

    print('Словарь кодирования:')
    for k, v in h_dict.items():
        print(k, v, sep=': ')

    print(f'\nЗакодированная строка:\n{st_encoded}')
