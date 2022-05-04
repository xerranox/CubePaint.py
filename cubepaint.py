#Librerías
import time
import turtle
import random
from tkinter import messagebox

#Pantalla
pantalla = turtle.Screen()
pantalla.title("CubePaint By: xerranox")
pantalla.bgcolor("Black")
pantalla.setup(width=1080, height=720)

#Limite abajo
barrera3 = turtle.Turtle()
barrera3.goto(-600, 300)
barrera3.pensize(2)
barrera3.pencolor("White")
barrera3.speed(2)
barrera3.goto(600, 300)
barrera3.hideturtle()

#Titulo
texto = turtle.Turtle()
texto.color("White")
texto.hideturtle()
texto.penup()
texto.goto(0, 315)
texto.write("CUBEPAINT", align="center", font=("Courier", 20, "normal"))

#Limite abajo
barrera3 = turtle.Turtle()
barrera3.goto(-600, -300)
barrera3.pensize(2)
barrera3.pencolor("White")
barrera3.speed(2)
barrera3.goto(600, -300)
barrera3.hideturtle()

#Controles
Controls = turtle.Turtle()
Controls.color("White")
Controls.hideturtle()
Controls.penup()
Controls.goto(-270, -340)
Controls.write("AWSD = Movimiento | R = Reinicio", align="center", font=("Courier", 20, "normal"))

#Copy
Copyright = turtle.Turtle()
Copyright.color("White")
Copyright.hideturtle()
Copyright.penup()
Copyright.goto(260, -340)
Copyright.write("    By: xerranox", align="left", font=("Courier", 20, "normal"))

#Jugador
jugador = turtle.Turtle()
jugador.color("White")
jugador.shape("square")
jugador.goto(0, 0)
jugador.direccion = "quieto"

#Funciones
def arriba():
    jugador.direccion = "arriba"
def abajo():
    jugador.direccion = "abajo"
def derecha():
    jugador.direccion = "derecha"
def izquierda():
    jugador.direccion = "izquierda"

#Reiniciar
def gameover():
    jugador.goto(0, 0)
    jugador.direccion = "quieta"

#Teclado
pantalla.listen()
pantalla.onkeypress(arriba, "w")
pantalla.onkeypress(abajo, "s")
pantalla.onkeypress(derecha, "d")
pantalla.onkeypress(izquierda, "a")
pantalla.onkeypress(gameover, "r")

#Movimiento
def movimiento():
    if jugador.direccion == 'arriba':
        y = jugador.ycor()
        jugador.sety(y+20)
    if jugador.direccion == 'abajo':
        y = jugador.ycor()
        jugador.sety(y-20)
    if jugador.direccion == 'derecha':
        x = jugador.xcor()
        jugador.setx(x+20)
    if jugador.direccion == 'izquierda':
        x = jugador.xcor()
        jugador.setx(x-20)

#Juego
while True:
    pantalla.update()

    #Movimiento
    movimiento()

    #Choque pared
    if jugador.xcor() > 520 or jugador.xcor() < -520 or jugador.ycor() > 280 or jugador.ycor() < -280:
        gameover()
