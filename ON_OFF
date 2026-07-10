#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
color_sensor = ColorSensor(Port.S1)

# Valores iniciales; para ajustar segun la pista

threshold = 45
base_speed = 90
turn_speed = 100

samples = 600
sample_time = 5

def set_motor_speeds(left_speed, right_speed):
    left_motor.run(left_speed)
    right_motor.run(right_speed)


def stop_robot():
    left_motor.stop()
    right_motor.stop()


def on_off_control(reflection_value):
    if reflection_value < threshold:
        print("Línea detectada: corrigiendo a la izquierda")
        set_motor_speeds(base_speed - turn_speed, base_speed + turn_speed)
    else:
        print("Fondo detectado: corrigiendo a la derecha")
        set_motor_speeds(base_speed + turn_speed, base_speed - turn_speed)


print("Iniciando control ON/OFF")

for sample in range(samples):
    reflection_value = color_sensor.reflection()

    print("Muestra:", sample + 1, "Reflexión:", reflection_value)

    on_off_control(reflection_value)
    wait(sample_time)

stop_robot()
print("Control ON/OFF finalizado")
