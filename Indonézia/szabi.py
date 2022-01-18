import turtle as t

def indonesia():
    t.showturtle()
    t.bgcolor('black')

    t.pu()
    t.setpos(t.xcor()-t.window_width()/3, t.ycor()-t.window_height()+700)
    t.pd()

    def teglalap_also(hosszu, rovid):
        for _ in range(2):
            t.fillcolor('#ffffff')
            t.begin_fill()
            t.fd(hosszu)
            t.rt(90)
            t.fd(rovid)
            t.rt(90)
            t.end_fill()

    def teglalap_felso(hosszu, rovid):
        for _ in range(2):
            t.fillcolor('#ff0000')
            t.begin_fill()
            t.fd(hosszu)
            t.lt(90)
            t.fd(rovid)
            t.lt(90)
            t.end_fill()

    def kiir (oldal):
        t.pu()
        t.rt(90)
        t.fd(oldal)
        t.lt(90)
        t.fd(oldal)
        t.pd()
        t.pencolor('white')
        t.write("Indonézia", font=('Arial', 20, 'bold'))

    t.hideturtle()
