"""
Broken Score
Program to determine score status
Now featuring functions and random-ness !!
"""
import random

THRESHOLD_HIGH = 100
THRESHOLD_LOW = 0
LOW_SCORE = 50
HIGH_SCORE = 90


def main():
    """Determine score status"""
    score = get_valid_score("Enter score: ", THRESHOLD_LOW, THRESHOLD_HIGH)
    score_status = determine_score_status(score, HIGH_SCORE, LOW_SCORE)
    print_score_status(score, score_status)
    random_score = generate_random_score()
    score_status = determine_score_status(random_score, HIGH_SCORE, LOW_SCORE)
    print_score_status(random_score, score_status)


def get_valid_score(prompt, low, high):
    """Get score from within valid range"""
    score = float(input(prompt))
    while score < low or score > high:
        print("Invalid score")
        score = float(input(prompt))
    return score


def determine_score_status(score, high, low):
    """Determine the status of the score given"""
    if score >= high:
        score_status = "Excellent :D"
    elif score >= low:
        score_status = "Passable :)"
    else:
        score_status = "Bad :("
    return score_status


def print_score_status(score, status):
    """Print the status of the score"""
    print("Your score of {} is {}".format(score, status))


def generate_random_score():
    """Generates a random score from within the valid range"""
    return random.randint(THRESHOLD_LOW, THRESHOLD_HIGH)


main()
