"""
Broken Score
Program to determine score status
"""
THRESHOLD_HIGH = 100
THRESHOLD_LOW = 0
LOW_SCORE = 50
HIGH_SCORE = 90


score = float(input("Enter score: "))
while score < THRESHOLD_LOW or score > THRESHOLD_HIGH:
    print("Invalid score")
    score = float(input("Enter score: "))
if score >= HIGH_SCORE:
    score_status = "Excellent :D"
elif score >= LOW_SCORE:
    score_status = "Passable :)"
else:
    score_status = "Bad :("
print(f"Your score is {score_status}")
