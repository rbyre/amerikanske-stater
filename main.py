import turtle
import pandas as pd

screen = turtle.Screen()

screen.title('Amerikanske stater')
screen.bgpic('./blank_states_img.gif')

bob = turtle.Turtle()
bob.hideturtle()
bob.speed('fastest')


data = pd.read_csv("50_states.csv")

# def get_mouse_click_coor(x, y):
#   print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
antall_rette = []
all_states = data.state.tolist()
gameloop = True
while gameloop and len(antall_rette) < 50:
  answer_state = screen.textinput(title="Gjett Staten", prompt=f"Nevn en annen stat. Du har {len(antall_rette)}/50" ).title()
  states = data['state']
  states_x = data['x']
  states_y = data['y']
  for state in states:
    if answer_state == state and answer_state not in antall_rette:
      chosen_x = states_x[data['state'] == answer_state]
      chosen_y = states_y[data['state'] == answer_state]
      # print(chosen_x.describe(), chosen_y.describe())
      bob.up()
      bob.goto(int(chosen_x), int(chosen_y))
      bob.down()
      bob.write(answer_state)
      antall_rette.append(answer_state)
      all_states.remove(answer_state)
  if answer_state == 'Exit':
    df = pd.DataFrame(all_states, columns=['states_left'])
    df.to_csv('states_to_practice.csv')
    gameloop = False
    

screen.exitonclick()