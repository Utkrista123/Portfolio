'''In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
times, was not out 162 times, and scored 48426 runs. Write a program to calculate
and display Boycott's batting average.'''

run_score = 484226
not_out_count = 162
batted_time = 1014

average = int(run_score / (batted_time - not_out_count))
print("Boycott's batting average is: ",average)