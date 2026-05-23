# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        start = 1
        end = n

        while start <= end:
            guessed_num = (start + end) // 2
            is_guessed = guess(guessed_num)

            if is_guessed == 0:
                return guessed_num
            elif is_guessed == -1:
                end = guessed_num - 1
            else:
                start = guessed_num + 1
        
        return -1
        