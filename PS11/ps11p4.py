def average(score1, score2, score3):
    total = score1 + score2 + score3
    avg = total / 3
    handicap_avg = (total + handicap) / 3 
    
    return avg, handicap_avg

last_name = input("Enter your last name: ")
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
handicap = float(input("What is your handicap: "))

avg, handicap_avg = average(score1, score2, score3)

print(last_name)
print(F"Score average: {avg}")
print(f"Handicap avg: {handicap_avg}")


