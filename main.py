# ----------------------------------------------------------------------
# Code made for Helix Hacks - by Oliver, Aidan, Chris, and Ty :D
# https://devpost.com/software/maze-quest-2
# This was the final product at the end of the hackathon!
# ----------------------------------------------------------------------

import turtle
import time
import random

wn = turtle.Screen()
wn.setup(650, 650)

# Creating Pen Class
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('black')
        self.penup()
        self.speed(0)
        self.walls = []
        self.keys = []

# Creating Player Class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('midnightblue')
        self.penup()
        self.speed(0)
        self.lvl = 1
        self.ice = False
        self.key = False
        self.initx = -288 + 24
        self.inity = 288 - 24

    def check_pos(self, new_x, new_y):
        if (new_x, new_y) not in pen.walls:
            self.goto(new_x, new_y)

            if (new_x, new_y) == goal.pos:
                goal.hideturtle()

                clear_maze(levels[self.lvl])
                self.lvl += 1
                setup_maze(levels[self.lvl])

            if (new_x, new_y) == key.pos:
                key.hideturtle()
                player.key = True

            if (new_x, new_y) == qey.pos:
                qey.hideturtle()
                player.key = True

            if (new_x, new_y) == door.pos:
                if player.key == True:
                    door.hideturtle()
                    player.key = False
                    door.pos = []
                else:
                    self.reset()

            if (new_x, new_y) == dorr.pos:
                if player.key == True:
                    dorr.hideturtle()
                    player.key = False
                    dorr.pos = []
                else:
                    self.reset()

            for enemy in enemies:
                if enemy.x == new_x and enemy.y == new_y:
                    self.reset()
                else:
                    enemy.move()

        else:
            self.color('midnightblue')
            self.reset()

    def check_pos_ice(self, new_x, new_y):
        if (new_x, new_y) == key.pos:
            print('ICE KEYYYYY')
            key.hideturtle()
            player.key = True

        if (new_x, new_y) == door.pos:
            if player.key == True:
                print('USED ICE KEY BVRUHEUHRIUEHRN')
                door.hideturtle()
                player.key = False
            else:
                self.reset()

        if (new_x, new_y) == hole.pos:
            clear_maze(levels[self.lvl])
            self.lvl -= 1
            self.ice = False
            setup_maze(levels[self.lvl])
            return 'HOLE'

        if (new_x, new_y) == goal.pos:
            goal.hideturtle()

            clear_maze(levels[self.lvl])
            self.lvl += 1
            self.ice = False
            setup_maze(levels[self.lvl])
            return 'GOAL'

    def go_up(self):
        # Calc new pos
        new_x = player.xcor()
        new_y = player.ycor() + 24

        if self.ice == True:
            while (new_x, new_y) not in ice.iceWall:
                self.goto(new_x, new_y)
                if self.check_pos_ice(new_x, new_y) == 'HOLE':
                    break
                elif self.check_pos_ice(new_x, new_y) == 'GOAL':
                    break
                time.sleep(0.05)
                new_y += 24
        else:
            self.check_pos(new_x, new_y)


    def go_down(self):
        new_x = player.xcor()
        new_y = player.ycor() - 24

        if self.ice == True:
            while (new_x, new_y) not in ice.iceWall:
                self.goto(new_x, new_y)
                if self.check_pos_ice(new_x, new_y) == 'HOLE':
                    break
                elif self.check_pos_ice(new_x, new_y) == 'GOAL':
                    break
                time.sleep(0.05)
                new_y -= 24
        else:
            self.check_pos(new_x, new_y)


    def go_right(self):
        new_x = player.xcor() + 24
        new_y = player.ycor()

        if self.ice == True:
            while (new_x, new_y) not in ice.iceWall:
                self.goto(new_x, new_y)
                if self.check_pos_ice(new_x, new_y) == 'HOLE':
                    break
                elif self.check_pos_ice(new_x, new_y) == 'GOAL':
                    break
                time.sleep(0.05)
                new_x += 24
        else:
            self.check_pos(new_x, new_y)

    def go_left(self):
        new_x = player.xcor() - 24
        new_y = player.ycor()

        if self.ice == True:
            while (new_x, new_y) not in ice.iceWall:
                self.goto(new_x, new_y)
                if self.check_pos_ice(new_x, new_y) == 'HOLE':
                    break
                elif self.check_pos_ice(new_x, new_y) == 'GOAL':
                    break
                time.sleep(0.05)
                new_x -= 24
        else:
            self.check_pos(new_x, new_y)

    def reset(self):
        if self.lvl != 1:
            self.goto(self.initx, self.inity)
            key.goto(key.initx, key.inity)
            key.showturtle()

            door.goto(door.initx, door.inity)
            door.pos = ((door.initx, door.inity))
            door.showturtle()

            if self.lvl == 3:
                qey.goto(qey.initx, qey.inity)
                qey.showturtle()

                self.key = False
                dorr.goto(dorr.initx, dorr.inity)
                dorr.pos = ((dorr.initx, dorr.inity))
                dorr.showturtle()
        else:
            self.goto(self.initx, self.inity)

class Enemy(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape('square')
            self.color('gray')
            self.penup()
            self.speed(0)
            self.x = x
            self.y = y
            self.goto(x, y)
            self.dir = random.choice(['right', 'left', 'up', 'down'])

        def move(self):
            dx, dy = 0, 0
            if self.dir == 'right':
                dx = 24
            elif self.dir == 'left':
                dx = -24
            elif self.dir == 'up':
                dy = 24
            elif self.dir == 'down':
                dy = -24

            new_x = self.xcor() + dx
            new_y = self.ycor() + dy

            if (new_x, new_y) == (player.xcor(), player.ycor()):
                player.color('midnightblue')
            elif (new_x, new_y) not in pen.walls and (new_x, new_y) != goal.pos and (new_x, new_y) != door.pos and (new_x, new_y) != dorr.pos:
                self.x = new_x
                self.y = new_y

                self.goto(new_x, new_y)
            else:
                self.dir = random.choice(['right', 'left', 'up', 'down'])
                self.move()

        def destroy(self):
            self.goto(5000, 5000)
            self.hideturtle()

class Key(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('yellow')
        self.penup()
        self.speed(0)
        self.pos = []
        self.hideturtle()
        self.initx = x
        self.inity = y

class Qey(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('yellow')
        self.penup()
        self.speed(0)
        self.pos = []
        self.hideturtle()
        self.initx = x
        self.inity = y

class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('brown')
        self.penup()
        self.speed(0)
        self.pos = []
        self.hideturtle()
        self.initx = x
        self.inity = y

class Dorr(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('brown')
        self.penup()
        self.speed(0)
        self.pos = []
        self.hideturtle()
        self.initx = x
        self.inity = y

class Hole(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('black')
        self.penup()
        self.speed(0)
        self.pos = []
        self.hideturtle()

class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('orange')
        self.penup()
        self.speed(0)
        self.pos = []
        self.hideturtle()

class Ice(turtle.Turtle):
     def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('lightblue')
        self.penup()
        self.speed(0)
        self.hideturtle()
        self.pos = []
        self.iceWall = []


# Creating Levels List
# Levels are 25 x 25 grids
levels = ['']

level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP                      X",
"X             E         X",
"X     E                 X",
"XXXXXXXXXXXXXX          X",
"X      E                X",
"X                       X",
"X                       X",
"X        XXXXXXXXXXXXXXXX",
"X                       X",
"X   E                   X",
"X                       X",
"XXXXXXXXXXXXXX          X",
"X                       X",
"X                       X",
"X           E           X",
"X        XXXXXXXXXXXXXXXX",
"X                 E     X",
"X    E                  X",
"X                       X",
"XXXXXXXXXXXXXX          X",
"X          E            X",
"X                       X",
"XG                      X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"

]

level_2 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXP       E            XX",
"XX                     XX",
"XXXX  XXXXXXXXXXXXXXX  XX",
"XXXX  XXXXX        XX  XX",
"XXXX      X XXXXXX XX  XX",
"XXXX      X X E        XX",
"XXXXXXXX  XKX          XX",
"XXXXXXXX  XXX  XX  XXXXXX",
"XX        XXX  XX  XXXXXX",
"XX  XXXXXXXXX  XX  XXXXXX",
"XX  XXXXXXXXX  XX  XXXXXX",
"XX    EXXX     XX  XXXXXX",
"XX     XXX     XX  XXXXXX",
"XX  XXXXXX  XXXXX   E  XX",
"XX  XXXXXX  XXXXX      XX",
"XX          XXXXXXXXX  XX",
"XX      E   XX   GXXX  XX",
"XX  XXXXXXXXXX    XXX  XX",
"XX  XXXXXXXXXXDXXXXXX  XX",
"XX              XXX    XX",
"XX         E    XXX    XX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",

]

level_3 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP        XXXXXXXQ     XX",
"X  XXXXX  XXXXXXXE     XX",
"X  XXXXX     E   XXXX  XX",
"XXXXXXXX         XXXX  XX",
"XXXXXXXX  XXXXX  XXXX  XX",
"XX        XXXXX  XXXX  XX",
"XX  XXX XXXXXXX  XXXX  XX",
"XX  XXX XXX  XX  XXXX  XX",
"XX  XXX      XX  XXXX  XX",
"XX  XXXXXXXXXXX  XXXX  XX",
"XX  XXXXX        XXXX  XX",
"XX  XXXXX  E     XXXX  XX",
"XX  XXXXX      XXXXXX  XX",
"XXE XXXXX      XXXXXX  XX",
"XXDXXXXXXK     XXXXXX  XX",
"XX   XXXXXXXXXXXXXXXX  XX",
"XX         E           XX",
"XX                     XX",
"XX    XXXXXXXXXX  XXXXXXX",
"XXOXXXXXXXXXX     XXXXXXX",
"XX     XXXXXX     XXXXXXX",
"XX     XXXXXXXX      XXXX",
"XG     XXXXXXXX E    XXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",

]

level_4 = [

"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXX K XXXXXXXXXXX",
"XXXXXXXXXXX   XXXXXXXXXXX",
"XXXX                  EEX",
"XXXX XXXXXXXXXXXXXXXXXXXX",
"XXXX XXXXXXXXXXXXXXXXXXXX",
"XXXX X               XXXX",
"XXXX X XXXX   XXXXXX XXXX",
"XXXX X XXXXXXXXXXXXX XXXX",
"XXXX X XXXX   XXXXXX XXXX",
"XX   X      P      X   XX",
"XXXX XXXXXX   XXXX X XXXX",
"XXXX XXXXXXXXXXXXX X XXXX",
"XXXX XXXXXX   XXXX X XXXX",
"XXXX               X XXXX",
"XXXXXXXXXXXXXXXXXXXX XXXX",
"XXXXXXXXXXXXXXXXXXXX XXXX",
"XEE                  XXXX",
"XXXXXXXXXXXXDXXXXXXXXXXXX",
"XXXXXXXXXXX G XXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

level_5 = [
"IIIIIIIIIIIIIIIIIIIIIIIII",
"IP             I       KI",
"II                      I",
"I    I                  I",
"I                     III",
"I      I               II",
"I                       I",
"I          I           II",
"I                      II",
"I             I         I",
"I     I                 I",
"I                    I  I",
"I                       I",
"IH                     II",
"I           I           I",
"I                I      I",
"I       I               I",
"I   I                   I",
"I                       I",
"I                  I    I",
"I                       I",
"IIIIIIIIIIIII IIIIIIIIIII",
"I  I                    I",
"IG D                    I",
"IIIIIIIIIIIIIIIIIIIIIIIII"

]

levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_4)
levels.append(level_5)

def setup_maze(level):
    player.ice = False
    wn.bgcolor('moccasin')
    pen.color('black')
    for y in range(len(level)):
        for x in range(len(level[y])):

            # Get char at each x,y coord
            character = level[y][x]

            # Calc screen coords
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Checking if wall
            if character == 'X':
                pen.goto(screen_x, screen_y)
                pen.stamp()
                pen.walls.append((screen_x, screen_y))

            # player
            elif character == 'P':
                player.goto(screen_x, screen_y)
                player.initx = screen_x
                player.inity = screen_y

            # goal
            elif character == 'G':
                goal.goto(screen_x, screen_y)
                goal.showturtle()
                goal.pos = ((screen_x, screen_y))

            elif character == 'E':
                enemies.append(Enemy(screen_x, screen_y))

            elif character == 'K':
                key.pos = ((screen_x, screen_y))

                key.goto(screen_x, screen_y)
                key.initx = screen_x
                key.inity = screen_y
                key.showturtle()

            elif character == 'Q':
                qey.pos = ((screen_x, screen_y))

                qey.goto(screen_x, screen_y)
                qey.initx = screen_x
                qey.inity = screen_y
                qey.showturtle()

            elif character == 'D':
                door.pos = ((screen_x, screen_y))

                door.goto(screen_x, screen_y)
                door.initx = screen_x
                door.inity = screen_y
                door.showturtle()

            elif character == 'O':
                dorr.pos = ((screen_x, screen_y))

                dorr.goto(screen_x, screen_y)
                dorr.initx = screen_x
                dorr.inity = screen_y
                dorr.showturtle()

            elif character == 'L':
                pen.goto(screen_x, screen_y)
                pen.color("darkorange")
                pen.stamp()
                pen.color("black")
                pen.walls.append((screen_x, screen_y))

            elif character == 'H':
                hole.goto(screen_x, screen_y)
                hole.showturtle()
                hole.pos = (screen_x, screen_y)

            elif character == 'I':
                player.ice = True
                ice.goto(screen_x, screen_y)
                ice.stamp()
                ice.iceWall.append((screen_x, screen_y))


def clear_maze(level):
    pen.color('moccasin')
    for coords in ice.iceWall:
        pen.goto(coords[0], coords[1])
        pen.stamp()
    ice.iceWall = []
    for coords in pen.walls:
        pen.goto(coords[0], coords[1])
        pen.stamp()
    pen.walls = []
    pen.keys = []
    goal.hideturtle()
    goal.pos = []
    key.hideturtle()
    qey.hideturtle()
    door.hideturtle()
    door.pos = []
    dorr.hideturtle()
    dorr.pos = []
    hole.hideturtle()
    for enemy in enemies:
        enemy.destroy()

# Create class instances
pen = Pen()
player = Player()
key = Key(0,0)
qey = Qey(0,0)
door = Door(0,0)
dorr = Dorr(0,0)
goal = Goal()
hole = Hole()
ice = Ice()

enemies = []

# Setting up maze level(s)
setup_maze(levels[player.lvl])

# Keyboard binding
turtle.listen()
turtle.onkey(player.go_left,'Left')
turtle.onkey(player.go_right,'Right')
turtle.onkey(player.go_down,'Down')
turtle.onkey(player.go_up,'Up')

# Making window close
wn.exitonclick()
