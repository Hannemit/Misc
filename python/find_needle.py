import numpy as np

def find_needle_in_haystack(haystack, needle):
    """
    Find some subsequence in a longer sequence and return the first index at which the subsequence was completely
    contained in the haystack, in the order defined in the subsequence (returns None if not found).
    Examples:
    needle = 'hlo', haystack = 'hello hello', returns 4
    needle = [2, 3], haystack = [3, 2, 4, 1, 3], returns 4
    needle = [4, 2], haystack = [3, 2, 4, 1, 3], returns None

    :param haystack: string, list or numpy array
    :param needle: same type as haystack,
    :return: int or None, if the needle is contained in the haystack, return the first index in haystack at which
                        the needle is fully contained within it. Return None if needle not found
    """
    idx_haystack = idx_needle = 0
    while idx_haystack < len(haystack) and idx_needle < len(needle):
        if haystack[idx_haystack] == needle[idx_needle]:
            idx_needle += 1
            if idx_needle == len(needle):
                return idx_haystack
        idx_haystack += 1
    return None


def find_unordered_needle_in_haystack(haystack, needle):
    """
    Find some subsequence in a longer sequence and return the first index at which the subsequence was completely
    contained in the haystack (returns None if not found).
    Examples:
    needle = [2, 3], haystack = [3, 2, 4, 1, 3], returns 1
    needle = [4, 2], haystack = [3, 2, 4, 1, 3], returns 2

    :param haystack: list or numpy array
    :param needle: same type as haystack,
    :return: int or None, if the needle is contained in the haystack, return the first index in haystack at which
                        the needle is fully contained within it. Return None if needle not found
    """

    haystack = np.array(haystack)

    needle_element_to_last_index_in_hay = {}
    for element in needle:
        last_index_in_input = needle_element_to_last_index_in_hay.get(element, -1) + 1  # returns 0 if not in dict
        index_list = np.where(haystack[last_index_in_input:] == element)[0]

        if len(index_list) != 0:
            needle_element_to_last_index_in_hay[element] = index_list[0] + last_index_in_input
        else:
            return None
    return max(needle_element_to_last_index_in_hay.values())