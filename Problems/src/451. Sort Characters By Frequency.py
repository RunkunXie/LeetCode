class Solution:
    """my sol"""
    def frequencySort(self, s: str) -> str:
        return ''.join([char * freq for char, freq in Counter(s).most_common()])

