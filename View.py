import turtle
from assets import assets_list

class PokeBattleGame:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.bgcolor("#a7a7a7")

        for assets in assets_list:
            self.screen.addshape(assets)

        self.fight_button = self.create_button("assets\\teste.gif",[1,1],[-225,-250],"#3b3b3b",self.show_attacks,text="Fight")

        self.back_button = self.create_button("assets\\back_button.gif",[1,1],[200,-180],"#000000",self.go_back)
        self.back_button.hideturtle()

        

    def create_button(self,shape: str,size: list[float,float],place: list[int,int],color: str,function: function,text: str = "") -> turtle.Turtle:
        button = turtle.Turtle(shape)
        button.shapesize(stretch_wid=size[0],stretch_len=size[1])
        button.teleport(place[0],place[1])
        button.color(color)
        button.onclick(function)
        return button

    def show_attacks(self,x,y):
        self.fight_button.hideturtle()
        self.back_window = self.subwindow()
        self.backwindowstamp = self.back_window.stamp()
        self.back_window.hideturtle()
        self.back_button.showturtle()

    def go_back(self,x,y):
        self.back_button.hideturtle()
        self.back_window.clearstamp(self.backwindowstamp)
        self.fight_button.showturtle()

    def subwindow(self):
        subwindow = turtle.Turtle("square")
        subwindow.shapesize(stretch_wid=10,stretch_len=250)
        subwindow.color("#646464")
        subwindow.teleport(0,-250)
        return subwindow
        

    def start(self):
        running = True
        while running:
            self.screen.update()

if __name__ == "__main__":
    game = PokeBattleGame()
    game.start()