x = 0
while x <= 5:
    print(x)
    x = x + 1

count = 7
while count < 1:
    print("Hello World")

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
