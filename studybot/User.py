"""
This is the User Class

Each user will have a class like this
Input will be fed in by the DumbleDore algorithm

breaks -> an tuple with 2 ingetegers that describes how long of a break in an hour in minutes in a study session and how many of those breaks eg: (5min, 2)
"""


class User:
    def __init__(self, name:str, subjects:list, strengths:list, weaknesses:list, breaks:int, grade:tuple, holidays:list, skill:int):
        
        self.name = name
        self.grade = grade
        self.subjects = subjects

        self.strengths = strengths
        self.weaknesses = weaknesses
        self.skill_level = skill

        self.breaks = breaks
        self.holidays = holidays

    def get_hour_distr(self, hours:int):
        session_length = (60/self.breaks[1]) - self.breaks[0]
        plan = []

        for _ in range(self.breaks[1]*hours):
            plan.append(session_length)
            plan.append(self.breaks[0])

        return plan

        
        
user = User("Rayan", ["Physics", "Hindi"], ["Physics"], ["Hindi"], (5, 3), 10, [6], 0.65)
print(user.get_hour_distr(2))

