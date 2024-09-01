class Solution:
    def maximumTime(self, time: str) -> str:
        # Convert the string into a list to make modifications easier
        time = list(time)

        # Determine the first digit of the hour
        if time[0] == '?':
            if time[1] == '?' or time[1] <= '3':
                time[0] = '2'
            else:
                time[0] = '1'

        # Determine the second digit of the hour
        if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'

        # Determine the first digit of the minute
        if time[3] == '?':
            time[3] = '5'

        # Determine the second digit of the minute
        if time[4] == '?':
            time[4] = '9'

        # Join the list back into a string and return the result
        return ''.join(time)
