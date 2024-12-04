score = int(input("enter number (0-100): "))

is_pass = score >= 50
is_high_pass = score > 75 and score < 90
is_perfect = score == 100
is_failing = score < 50

print(is_pass,is_high_pass,is_perfect,is_failing)