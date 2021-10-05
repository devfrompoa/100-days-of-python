import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

cursor = turtle.Turtle()
cursor.hideturtle()
cursor.penup()

data = pandas.read_csv("50_states.csv")
num_states = len(data)
correct_answers = 0
correct_guesses = []

while correct_answers < num_states:
    answer_state = screen.textinput(title=f"{correct_answers}/{num_states} States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_to_learn = [state for state in data.state if state not in correct_guesses]
        # for state in data.state:
        #     if state not in correct_guesses:
        #         states_to_learn.append(state)
        df = pandas.DataFrame(states_to_learn, columns=['state'])
        df.to_csv("states_to_learn.csv")
        break
    for state in data.state:
        if (answer_state == state) and (answer_state not in correct_guesses):
            x_pos = float(data.x[data.state == answer_state])
            y_pos = float(data.y[data.state == answer_state])
            cursor.setpos(x_pos, y_pos)
            cursor.write(answer_state, align="center")
            correct_guesses.append(answer_state)
            correct_answers += 1
