class WorkoutData:
    push = [ "push",
             ["dumbbell press", "3x8", 25, ""],
             ["dumbbell incline press", "3x8", 20, ""],
             ["dumbbell single triceps push up", "3x10", 10, ""],
             ["machine single triceps push down", "3x15", 25, ""],
             ["machine flies", "3x10", 70, ""] ] 

    pull = [ "pull",
             ["pull up", "3x5", "N/A", "use all the bands or you will die"],
             ["dumbbell row", "3x8", 20, "do it for both hands"],
             ["machine row", "3x10", 135, ""],
             ["hammer curls", "3x10", 15, ""] ]

    leg = [ "leg",
            ["machine squad", "2x8", 15, "the weight is pounds for each side\nmake sure don't get too right"],
            ["legs front squad", "1x10", 0, "no plates"],
            ["romanian deadlifts", "3x10", 20, ""],
            ["leg extension", "3x10", 50, ""],
            ["leg curl", "3x10", 65, ""] ]

    shoulder = [ "shoulder",
                 ["overhead press", "3x10", 20, ""],
                 ["reverse machine flies", "5x10", 50, "do it with laterals"],
                 ["laterals/stand up flies", "5x10", 10, "do it with RMF"],
                 ["shrugs", "3x10", 15, ""] ]

class BotFunction:
    def get_workout(workout):
        workout_type = None

        if workout == "push":
            workout_type = WorkoutData.push
        elif workout == "pull":
            workout_type = WorkoutData.pull
        elif workout == "leg":
            workout_type = WorkoutData.leg
        elif workout == "shoulder":
            workout_type = WorkoutData.shoulder
        else:
            print("ERROR: WORKOUT TYPE NOT FOUND!!")
            return

        return workout_type
    
    def index_workout(workout, index):
        length = len(workout)
        
        if index > length:
            print("ERROR: INDEX IS OUT OF RANGE!!")
            return 

        return workout[index]
    
    def get_summary(workout):
        plan = ""
        print(workout)

        for i in range(1, len(workout)):
            plan = plan + f"- {workout[i][0]}\n"

        return f"Nice! So it's {workout[0]} day!\nHere's your workout plan for today:\n" + plan + "Good luck!"

    def get_current_workout(workout, index):
        string = f"{index}/{len(workout)-1} **{workout[index][0]}**\nSets and reps: {workout[index][1]}\nWeight: {workout[index][2]} pounds\nNotes:\n{workout[index][3]}"
        return string








