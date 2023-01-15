import turtle, random
from playsound import playsound
import threading

#this is a test

def loopSound():
    while True:
        playsound('Tetris.mp3', block=True)

# providing a name for the thread improves usefulness of error messages.
loopThread = threading.Thread(target=loopSound, name='backgroundMusicThread')
loopThread.daemon = True # shut down music thread when the rest of the program exits
loopThread.start()




SCALE = 32 #Controls how many pixels wide each grid square is

class Start_Screen:
    def __init__(self):
        # playsound('Tetris.mp3', False)
         
         
         #Setup window size based on SCALE value.
        
        
        turtle.setup(SCALE*12+20, SCALE*22+20)

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)
        
        turtle.onkeypress(self.start_game, 's')
        turtle.onkeypress(self.exit_game, 'e')
        
        #These three lines must always be at the BOTTOM of __init__
        turtle.update()
        turtle.listen()
        turtle.mainloop()
        
    def start_game(self):
        turtle.onkeypress(None, 's')
        turtle.onkeypress(None, 'e')
        print("starting Game")
        Game()
    
    def exit_game(self):
        turtle.bye()



    


class Game:
    def __init__(self):
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)

        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        turtle.onkeypress(self.rotate, 'space')
        turtle.onkeypress(self.drop, 'Down')

        self.new_block(random.randint(1, 7)) 
       
        
    

        self.occupied = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
        for list in self.occupied:
            for i in range(10):
                list.append(False)


        turtle.ontimer(self.gameloop, 300)
        #These three lines must always be at the BOTTOM of __init__
        turtle.update()
        turtle.listen()
        turtle.mainloop()


    def gameloop(self):

        if self.active.valid(0, -1, self.occupied):
            self.active.move(0,-1)
            turtle.update()
            turtle.ontimer(self.gameloop, 300) 
        
        elif self.active.ycors() < 20:
            self.new_block(random.randint(1, 7))
            turtle.ontimer(self.gameloop, 300) 

        else:
            print("Bye")
            turtle.onkeypress(None, 'Left')
            turtle.onkeypress(None, 'Right')
            turtle.onkeypress(None, 'space')
            turtle.onkeypress(None, 'Down')
            turtle.clearscreen()
            Game_Over()

    def move_left(self):
        if self.active.valid(-1, 0, self.occupied):
            self.active.move(-1, 0)
        turtle.update()

    def move_right(self):
        if self.active.valid(1, 0, self.occupied):
            self.active.move(1, 0)
        turtle.update()

    def drop(self):
        while self.active.valid(0, -1, self.occupied):
            self.active.move(0,-1)
        turtle.update()
    
    def rotate(self):
        self.active.rotate_block()

    def new_block(self, num):
        if num == 1:
            self.active = T()
        elif num == 2:
            self.active = I()
        elif num == 3:
            self.active = SQ()
        elif num == 4:
            self.active = J()
        elif num == 5:
            self.active = L()
        elif num == 6:
            self.active = Z()
        else:
            self.active = S()

class Game_Over:
    def __init__(self):
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)

        #These three lines must always be at the BOTTOM of __init__
        turtle.update()
        turtle.listen()
        turtle.mainloop()

class Square(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(color)
        self.pencolor("gray")
        self.penup()
        self.goto(x, y)

class Block:
    def __init__(self):
        self.squares = []    
        self.rot = 0

    def move(self, dx, dy):
        for square in self.squares:
            x = square.xcor() + dx
            y = square.ycor() + dy
            square.goto(x, y)
    
    def valid(self, dx, dy, occupied):
        for square in self.squares:
            x = square.xcor() + dx
            y = square.ycor() + dy
            print(y)
            if y == -1:
                for sq in self.squares:
                    occupied[19 - sq.ycor()][sq.xcor()] = True
                print(occupied)
                return False
            if y > 19:
                return True
            # if occupied[19 - y][x]:
            #     for sq in self.squares:
            #         occupied[19 - sq.ycor()][sq.xcor()] = True
            #     print(occupied)
            #     return False
            if x < 0 or x > 9 or (occupied[19 - y][x] and dy == 0 ):
                return False
            if y < 0 or occupied[19 - y][x]:
                
                for sq in self.squares:
                    occupied[19 - sq.ycor()][sq.xcor()] = True
                print(occupied)
                return False
        return True

    def ycors(self):
        min = self.squares[0].ycor()
        for square in self.squares:
            if square.ycor() < min:
                min = square.ycor()
        return min


class T(Block):
    def __init__(self):
        Block.__init__(self)
        self.squares.append(Square(3, 21, 'violet'))
        self.squares.append(Square(4, 21, 'violet'))
        self.squares.append(Square(5, 21, 'violet'))
        self.squares.append(Square(4, 22, 'violet'))
    
    def rotate_block(self):
        if self.rot == 0:
            left = 0
            for i in range(4):
                if self.squares[i].xcor() < self.squares[left].xcor():
                    left = i
            self.squares[left].goto(self.squares[left].xcor() + 1, self.squares[left].ycor() - 1)
            self.rot += 1
        elif self.rot == 1:
            top = 0
            for i in range(4):
                if self.squares[i].ycor() > self.squares[top].ycor():
                    top = i
            self.squares[top].goto(self.squares[top].xcor() - 1, self.squares[top].ycor() - 1)
            self.rot += 1
        elif self.rot == 2: 
            right = 0
            for i in range(4):
                if self.squares[i].xcor() > self.squares[right].xcor():
                    right = i
            self.squares[right].goto(self.squares[right].xcor() - 1, self.squares[right].ycor() + 1)
            self.rot += 1
        else:
            bot = 0
            for i in range(4):
                if self.squares[i].ycor() < self.squares[bot].ycor():
                    bot = i
            self.squares[bot].goto(self.squares[bot].xcor() + 1, self.squares[bot].ycor() + 1)
            self.rot = 0


class I(Block):
    def __init__(self):
        Block.__init__(self)
        self.squares.append(Square(3, 21, 'cyan'))
        self.squares.append(Square(4, 21, 'cyan'))
        self.squares.append(Square(5, 21, 'cyan'))
        self.squares.append(Square(6, 21, 'cyan'))

    def rotate_block(self):
        if self.rot == 0:
            self.squares[0].goto(self.squares[0].xcor() + 2, self.squares[0].ycor() + 1)
            self.squares[1].goto(self.squares[1].xcor() + 1, self.squares[1].ycor())
            self.squares[2].goto(self.squares[2].xcor(), self.squares[2].ycor() - 1)
            self.squares[3].goto(self.squares[3].xcor() - 1, self.squares[3].ycor() - 2)
            self.rot += 1
        elif self.rot == 1:
            self.squares[0].goto(self.squares[0].xcor() + 1, self.squares[0].ycor() - 2)
            self.squares[1].goto(self.squares[1].xcor(), self.squares[1].ycor() - 1)
            self.squares[2].goto(self.squares[2].xcor() - 1, self.squares[2].ycor())
            self.squares[3].goto(self.squares[3].xcor() - 2, self.squares[3].ycor() + 1)
            self.rot += 1
        elif self.rot == 2: 
            self.squares[0].goto(self.squares[0].xcor() - 2, self.squares[0].ycor() - 1)
            self.squares[1].goto(self.squares[1].xcor() - 1, self.squares[1].ycor())
            self.squares[2].goto(self.squares[2].xcor(), self.squares[2].ycor() + 1)
            self.squares[3].goto(self.squares[3].xcor() + 1, self.squares[3].ycor() + 2)
            self.rot += 1
        else:
            self.squares[0].goto(self.squares[0].xcor() - 1, self.squares[0].ycor() + 2)
            self.squares[1].goto(self.squares[1].xcor(), self.squares[1].ycor() + 1)
            self.squares[2].goto(self.squares[2].xcor() + 1, self.squares[2].ycor())
            self.squares[3].goto(self.squares[3].xcor() + 2, self.squares[3].ycor() - 1)
            self.rot = 0


class SQ(Block):
    def __init__(self):
        Block.__init__(self)
        self.squares.append(Square(4, 21, 'yellow'))
        self.squares.append(Square(4, 22, 'yellow'))
        self.squares.append(Square(5, 21, 'yellow'))
        self.squares.append(Square(5, 22, 'yellow'))

    def rotate_block(self):
        pass


class J(Block):
    def __init__(self):
        Block.__init__(self)
        self.squares.append(Square(3, 22, 'blue'))
        self.squares.append(Square(3, 21, 'blue'))
        self.squares.append(Square(4, 21, 'blue'))
        self.squares.append(Square(5, 21, 'blue'))

    def rotate_block(self):
        if self.rot == 0:
            self.squares[0].goto(self.squares[0].xcor() + 2, self.squares[0].ycor())
            self.squares[1].goto(self.squares[1].xcor() + 1, self.squares[1].ycor() + 1)
            self.squares[3].goto(self.squares[3].xcor() - 1, self.squares[3].ycor() - 1)
            self.rot += 1
        elif self.rot == 1:
            self.squares[0].goto(self.squares[0].xcor(), self.squares[0].ycor() - 2)
            self.squares[1].goto(self.squares[1].xcor() + 1, self.squares[1].ycor() - 1)
            self.squares[3].goto(self.squares[3].xcor() - 1, self.squares[3].ycor() + 1)
            self.rot += 1
        elif self.rot == 2: 
            self.squares[0].goto(self.squares[0].xcor() - 2, self.squares[0].ycor())
            self.squares[1].goto(self.squares[1].xcor() - 1, self.squares[1].ycor() - 1)
            self.squares[3].goto(self.squares[3].xcor() + 1, self.squares[3].ycor() + 1)
            self.rot += 1
        else:
            self.squares[0].goto(self.squares[0].xcor(), self.squares[0].ycor() + 2)
            self.squares[1].goto(self.squares[1].xcor() - 1, self.squares[1].ycor() + 1)
            self.squares[3].goto(self.squares[3].xcor() + 1, self.squares[3].ycor() - 1)
            self.rot = 0

class L(Block):
    def __init__(self):
        Block.__init__(self)
        self.squares.append(Square(3, 21, 'orange'))
        self.squares.append(Square(4, 21, 'orange'))
        self.squares.append(Square(5, 21, 'orange'))
        self.squares.append(Square(5, 22, 'orange'))

    def rotate_block(self):
        if self.rot == 0:
            self.squares[0].goto(self.squares[0].xcor() + 1, self.squares[0].ycor() + 1)
            self.squares[2].goto(self.squares[2].xcor() - 1, self.squares[2].ycor() - 1)
            self.squares[3].goto(self.squares[3].xcor(), self.squares[3].ycor() - 2)
            self.rot += 1
        elif self.rot == 1:
            self.squares[0].goto(self.squares[0].xcor() + 1, self.squares[0].ycor() - 1)
            self.squares[2].goto(self.squares[2].xcor() - 1, self.squares[2].ycor() + 1)
            self.squares[3].goto(self.squares[3].xcor() - 2, self.squares[3].ycor())
            self.rot += 1
        elif self.rot == 2: 
            self.squares[0].goto(self.squares[0].xcor() - 1, self.squares[0].ycor() - 1)
            self.squares[2].goto(self.squares[2].xcor() + 1, self.squares[2].ycor() + 1)
            self.squares[3].goto(self.squares[3].xcor(), self.squares[3].ycor() + 2)
            self.rot += 1
        else:
            self.squares[0].goto(self.squares[0].xcor() - 1, self.squares[0].ycor() + 1)
            self.squares[2].goto(self.squares[2].xcor() + 1, self.squares[2].ycor() - 1)
            self.squares[3].goto(self.squares[3].xcor() + 2, self.squares[3].ycor())
            self.rot = 0

class Z(Block):
    def __init__(self):
        Block.__init__(self)
        self.squares.append(Square(3, 22, 'red'))
        self.squares.append(Square(4, 22, 'red'))
        self.squares.append(Square(4, 21, 'red'))
        self.squares.append(Square(5, 21, 'red'))

    def rotate_block(self):
        if self.rot == 0:
            self.squares[0].goto(self.squares[0].xcor() + 2, self.squares[0].ycor())
            self.squares[1].goto(self.squares[1].xcor() + 1, self.squares[1].ycor() - 1)
            self.squares[3].goto(self.squares[3].xcor() - 1, self.squares[3].ycor() - 1)
            self.rot += 1
        elif self.rot == 1:
            self.squares[0].goto(self.squares[0].xcor(), self.squares[0].ycor() - 2)
            self.squares[1].goto(self.squares[1].xcor() - 1, self.squares[1].ycor() - 1)
            self.squares[3].goto(self.squares[3].xcor() - 1, self.squares[3].ycor() + 1)
            self.rot += 1
        elif self.rot == 2: 
            self.squares[0].goto(self.squares[0].xcor() - 2, self.squares[0].ycor())
            self.squares[1].goto(self.squares[1].xcor() - 1, self.squares[1].ycor() + 1)
            self.squares[3].goto(self.squares[3].xcor() + 1, self.squares[3].ycor() + 1)
            self.rot += 1
        else:
            self.squares[0].goto(self.squares[0].xcor(), self.squares[0].ycor() + 2)
            self.squares[1].goto(self.squares[1].xcor() + 1, self.squares[1].ycor() + 1)
            self.squares[3].goto(self.squares[3].xcor() + 1, self.squares[3].ycor() - 1)
            self.rot = 0

class S(Block):
    def __init__(self):
        Block.__init__(self)
        self.squares.append(Square(3, 21, 'green'))
        self.squares.append(Square(4, 21, 'green'))
        self.squares.append(Square(4, 22, 'green'))
        self.squares.append(Square(5, 22, 'green'))  

    def rotate_block(self):
        if self.rot == 0:
            self.squares[0].goto(self.squares[0].xcor() + 1, self.squares[0].ycor() + 1)
            self.squares[2].goto(self.squares[2].xcor() + 1, self.squares[2].ycor() - 1)
            self.squares[3].goto(self.squares[3].xcor(), self.squares[3].ycor() - 2)
            self.rot += 1
        elif self.rot == 1:
            self.squares[0].goto(self.squares[0].xcor() + 1, self.squares[0].ycor() - 1)
            self.squares[2].goto(self.squares[2].xcor() - 1, self.squares[2].ycor() - 1)
            self.squares[3].goto(self.squares[3].xcor() - 2, self.squares[3].ycor())
            self.rot += 1
        elif self.rot == 2: 
            self.squares[0].goto(self.squares[0].xcor() - 1, self.squares[0].ycor() - 1)
            self.squares[2].goto(self.squares[2].xcor() - 1, self.squares[2].ycor() + 1)
            self.squares[3].goto(self.squares[3].xcor(), self.squares[3].ycor() + 2)
            self.rot += 1
        else:
            self.squares[0].goto(self.squares[0].xcor() - 1, self.squares[0].ycor() + 1)
            self.squares[2].goto(self.squares[2].xcor() + 1, self.squares[2].ycor() + 1)
            self.squares[3].goto(self.squares[3].xcor() + 2, self.squares[3].ycor())
            self.rot = 0

if __name__ == '__main__':
   Start_Screen()
