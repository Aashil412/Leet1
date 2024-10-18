class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ball_count = {}
        for i in range(lowLimit, highLimit + 1):
            sum_of_digit = 0
            while i:
                sum_of_digit += i % 10
                i //= 10
            if sum_of_digit in ball_count:
                ball_count[sum_of_digit] += 1
            else:
                ball_count[sum_of_digit] = 1
        return max(ball_count.values())