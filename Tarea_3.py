#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# configuracion de Motores y sensores
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
distance_sensor = UltrasonicSensor(Port.S2)

# Aconfugración del algoritmo
samples = 200             # Maximo numero de iteraciones
sample_time = 50          # Tiempo entre muestras, en milisegundos
minimum_distance = 150    # 150 mm = 15 cm
speed = 250

def move(left_speed, right_speed):  # Funcion para mover el motor
    left_motor.run(left_speed)
    right_motor.run(right_speed)

def stop():                        # Función alto
    left_motor.stop()
    right_motor.stop()

def move_forward():               # Función para avanzar
    print("Robot avanzando")
    move(speed, speed)

def move_backward(speed_value, time):  # Función para retroceder
    print("Robot retrocediendo")
    move(-speed_value, -speed_value)
    wait(time)
    stop()

def turn_right(speed_value, time):     # Funcion para dar vuelta a la derecha
    print("Robot girando a la derecha")
    move(speed_value, -speed_value)
    wait(time)
    stop()

def avoid_obstacle():    # Función para evadir obstaculos
    print("Obstaculo detectado")
    stop()
    wait(300)
    move_backward(speed, 700)
    turn_right(speed, 1100)
    move_forward()
    wait(1000)
    stop()
    print("Obstaculo evadido")

# Programa principal
print("Iniciando la lectura del sensor ultrasonico")

for sample in range(samples):
    distance_mm = round(distance_sensor.distance(), 2)
    print("Muestra:", sample + 1,
          "Distancia medida:", distance_mm / 10, "cm")

    if distance_mm <= minimum_distance:
        avoid_obstacle()
    else:
        move_forward()

    wait(sample_time)

stop()     # Al completar las muestras, el robot se detiene
print("Lectura finalizada")
print("Robot apagado")
