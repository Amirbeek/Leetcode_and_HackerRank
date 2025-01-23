class Solution:
    def convertTime(self, current, correct):
        # Extract hours and minutes from the current and correct times
        cur_hour, cur_minute = map(int, current.split(':'))
        corr_hour, corr_minute = map(int, correct.split(':'))

        cur_total_minutes = cur_hour * 60 + cur_minute
        corr_total_minutes = corr_hour * 60 + corr_minute

        # Determine the minutes difference
        minutes_needed = corr_total_minutes - cur_total_minutes

        # Initialize the result counter for steps
        result = 0

        # Calculate the number of 60-minute increments needed
        result += minutes_needed // 60
        minutes_needed %= 60

        # Calculate the number of 15-minute increments needed
        result += minutes_needed // 15
        minutes_needed %= 15

        # Calculate the number of 5-minute increments needed
        result += minutes_needed // 5
        minutes_needed %= 5

        # The remaining minutes will be the number of 1-minute increments
        result += minutes_needed

        return result


# Example usage:
solution = Solution()
print(solution.convertTime("02:30", "04:35"))  # Expected output: 3
print(solution.convertTime("11:00", "11:01"))  # Expected output: 1
