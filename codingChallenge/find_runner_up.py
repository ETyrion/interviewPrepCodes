score_list = [10, 20, 10, 30, 50, 50, 25,100, 75, 100]

unique_score = list(set(score_list))
print(unique_score)
unique_score.sort()
print(unique_score)

runner_up = unique_score[-2]
print(runner_up)