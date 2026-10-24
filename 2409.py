# 2409. Count Days Spent Together
# Alice and Bob are traveling to Rome for separate business meetings.
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
# Return the total number of days that Alice and Bob are in Rome together.
# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

class Solution:
    def get_date_float(self, date_str: str) -> float:
        arrive_month, arrive_day = [int(x) for x in date_str.split("-")]
        return arrive_month + arrive_day / 100

    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        count = 0
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        arrive_a = self.get_date_float(arriveAlice)
        leave_a = self.get_date_float(leaveAlice)
        arrive_b = self.get_date_float(arriveBob)
        leave_b = self.get_date_float(leaveBob)
        for idx, days in enumerate(month_days):
            month = idx + 1
            for day in range(1, days + 1):
                stamp = month + day / 100
                if arrive_a <= stamp <= leave_a and arrive_b <= stamp <= leave_b:
                    count += 1
        return count