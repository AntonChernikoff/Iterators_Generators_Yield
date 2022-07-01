from collections import Iterable

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


# for item in FlatIterator(nested_list):
# 	print(item)

class FlatIterator:
    def __init__(self, lst):
        self.lst = lst
        self.cursor = 0
        self.list_len = len(self.lst)

    def __iter__(self):
        self.cursor += 1
        self.nested_cursor = 0
        return self

    def __next__(self):
        if self.nested_cursor == len(self.lst[self.cursor - 1]):
            iter(self)
        if self.cursor - 1 == self.list_len:
            raise StopIteration
        self.nested_cursor += 1
        return self.lst[self.cursor-1][self.nested_cursor - 1]


def flat_generator(a: list) -> list:
    return [x for sublist in a for x in sublist]

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

if __name__ == '__main__':
    # flat_list = [item for item in FlatIterator(nested_list)]
    # print(flat_list)
    # задание 1
    for item in FlatIterator(nested_list):
        print(item)
    # Задание 2
    for item in flat_generator(nested_list):
        print(item)

