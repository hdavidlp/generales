from cgitb import reset
from pprint import pprint
from unittest import result




def _is_perfect_lenght(sequence):
    """  True if equencie has lenght 2n -1 """
    n = len(sequence)
    return ((n+1) & n == 0) and (n!=0)



class LevelOrderIterator:

    def __init__(self, sequence):
        if not _is_perfect_lenght(sequence):
            raise ValueError(
                f"Sequence of lenght {len(sequence)} does not represent "
                " a perfect binary tree lenght "
            )
        self._sequence = sequence
        self._index = 0
        
    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration
        result = self._sequence[self._index]
        self._index +=1
        return result
    
    def __iter__(self):
        return self

def _left_child(index):
    return 2 * index + 1

def _right_child(index):
    return 2 * index + 2  


class PreOrderIterator:
    def __init__(self, sequence):
        if not _is_perfect_lenght(sequence):
            raise ValueError(
                f"Sequence of lenght {len(sequence)} does not represent "
                " a perfect binary tree lenght "
            )
        self._sequence = sequence
        self._stack = [0] 
    
    def __next__(self):
        if len(self._stack)==0:
            raise StopIteration
        index = self._stack.pop()
        result = self._sequence[index]

        # Pre order: Push right child first so left child is
        # popped and processed first. Last-in, first-out
        right_child_index = _right_child(index)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)

        left_child_index =_left_child(index)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result 
    
    def __iter__(self):
        return self

class InOrderIterator:
    def __init__(self, sequence):
        if not _is_perfect_lenght(sequence):
            raise ValueError(
                f"Sequence of lenght {len(sequence)} does not represent "
                " a perfect binary tree lenght "
            )
        self._sequence = sequence
        self._stack = [0] 
        self._index = 0
    
    def __next__(self):
        if (len(self._stack)==0) and (self._index >= len(self._sequence)):
            raise StopIteration

        # Push left children onto the stack while possible
        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = _left_child(self._index)

        # Pop from stack an process, before moving to the right child
        index = self._stack.pop()
        result = self._sequence[index]
        self._index = _right_child(index)
        return result
    
    def __iter__(self):
        return self


class SkipMissingIterator():

    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __next__(self):
        while True:
            item = next(self._iterator)
            if item is not missing:
                return item

    def __iter__(self):
        return self


class TranslationIterable:

    def __init__(self, table, iterable):
        self._table = table
        self._iterator = iter(iterable)
    
    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)

    def __iter__(self):
        return self


# for i in range (len(expr_tree)):
#     print (next(iterator))

# for item in iterator:
#     print (item)


# expr_tree = ["*", "+", "-", "a", "b", "c", "d"]
# iterator = iter(expr_tree)
# iterator2 = LevelOrderIterator(expr_tree)

# for i in iterator2:
#     print (i)

# print (" ".join(iterator2))

# pprint ({i: _is_perfect_lenght(["x"]*i) for i in range (0,32)} )


expr_tree = "* + - a b c d".split()
iterator = PreOrderIterator(expr_tree)
iterator2 = InOrderIterator(expr_tree)

#print (" ".join(iterator))
print (" ".join(iterator2))

# missing = object()

# expr_tree = ["+", "r", "*", missing, missing, "p", "q"]
# iterator = SkipMissingIterator(expr_tree)

# print (" ".join(iterator))


# iterator2 = SkipMissingIterator(InOrderIterator(expr_tree))
# print (" ".join(iterator2))

# typesetting_table = {
#     "-" : "\u2212", # Minus sign
#     "*" : "\u00D7", # Multiplication sign
#     "/" : "\u00F7",# Division sign
# }


# m = missing
# expr_tree = [
#                  "-",
#              "*",      "/",
#           "p", "q", "r", "+",
#          m, m, m, m, m,m, "s", "t"
# ]

# iterator = TranslationIterable(typesetting_table, SkipMissingIterator(InOrderIterator(expr_tree)))
# print (" ".join(iterator))

