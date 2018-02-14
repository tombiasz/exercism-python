def anagram_filter(string):
    string = string.lower()
    string_chars = sorted(list(string))

    def filter(element):
        element = element.lower()
        return element != string and sorted(list(element)) == string_chars

    return filter


def detect_anagrams(string, array):
    return list(filter(anagram_filter(string), array))
