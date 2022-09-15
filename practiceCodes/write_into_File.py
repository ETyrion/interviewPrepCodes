with open('workout.txt','a') as workout_track:
    workout_track.write('\nMay 26: 9000')

with open('workout.txt', 'r') as workout_track_reader:
    for line in workout_track_reader:
        print(line)