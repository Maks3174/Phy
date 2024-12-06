from more_itertools import chunked

def split_dictionary(big_dict, chunk_size):

    items = list(big_dict.items())
    chunks = chunked(items, chunk_size)
    return [dict(chunk) for chunk in chunks]

big_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
chunk_size = 3
smaller_dictionaries = split_dictionary(big_dictionary, chunk_size)
for idx, smaller_dict in enumerate(smaller_dictionaries):
    print(f"Підсловник {idx + 1}: {smaller_dict}")
