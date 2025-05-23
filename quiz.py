import pgzrun

TITLE = "Quiz Master"
WIDTH = 900
HEIGHT = 700

marquee_box = Rect(0,0,900,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0,150,150)
answer_box1 = Rect(0,0,300,150)
answer_box2 = Rect(0,0,300,150)
answer_box3 = Rect(0,0,300,150)
answer_box4 = Rect(0,0,300,150)
skip_box = Rect(0,0,150,330)

marquee_message = ""
score = 0
timer = 10
game_over = False
questions = []
question_count,question_index = 0,0

marquee_box.move_ip(0,0)
question_box.move_ip(20,100)
timer_box.move_ip(700,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)

answers = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    global marquee_message
    screen.clear()
    screen.fill("blue")
    screen.draw.filled_rect(marquee_box,"white")
    screen.draw.filled_rect(question_box,"green")
    screen.draw.filled_rect(timer_box,"yellow")
    screen.draw.filled_rect(skip_box,"black")
    screen.draw.filled_rect(marquee_box,"white")
    for i in answers:
        screen.draw.filled_rect(i,"red")
    marquee_message = "welcome to quizmaster"
    screen.draw.textbox(marquee_message, marquee_box, color = "black")
    screen.draw.textbox(question[0], question_box, color = "white")
    screen.draw.textbox(str(timer), timer_box, color = "white", shadow = (0.5,0.5), scolor = "gray")
    screen.draw.textbox("skip", skip_box, color = "white", angle = 90)
# for i,v in enumerate(answers):
#    screen.draw.textbox(question[i+1],v,color = "white")
    for i in range(len(answers)):
      screen.draw.textbox(question[i+1],answers[i],color = "white")    
      
def update():
    
    marquee_box.x -= 2
    if marquee_box.right < 0:
        marquee_box.left = WIDTH

def skip():
   global question, timer
   if questions and not game_over:
      question = read_next_question()
      timer = 10
   else:
      game_over = True

def read_file():
   global question_index, question_count, questions
   file = open("quiz.txt", "r")
   for i in file:
     questions.append(i)
     question_count += 1
   file.close()
   print(questions)

def read_next_question():
    global question_index
    question_index +=1
    return(questions.pop(0).split(","))

def update_timer():
   global timer, game_over
   if timer:
      timer -= 1
   else:
      game_over = True
def on_mouse_down(pos):
   global question, timer,score
   index = 1
   for i in answers:
      if i.collidepoint(pos):
         if index is int(question[5]):
            score += 1
            if questions:
               question = read_next_question()
               timer = 10
            else:
               gameOver()
         else:
            gameOver()
      index += 1
   if skip_box.collidepoint(pos):
      if questions and not game_over:
         question = read_next_question()
         timer = 10
      else:
         gameOver()

def gameOver():
   global timer,question, game_over
   message = f"game over\n you scored {score} out of {question_count}"
   question = [message,"-","-","-","-", 0]
   timer = 0
   game_over = True

   
read_file()
question = read_next_question()
print(question)
clock.schedule_interval(update_timer,1)





pgzrun.go()