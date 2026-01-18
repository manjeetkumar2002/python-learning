class Solution:
    def solve(self, index, subset, result, char_map, digits):
        if index >= len(digits):
            result.append("".join(subset.copy()))
            return

        string = char_map[digits[index]]
        for letter in string:
            subset.append(letter)
            self.solve(index + 1, subset, result, char_map, digits)
            subset.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        self.solve(0, [], result, char_map, digits)
        return result