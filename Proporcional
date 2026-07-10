#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
color_sensor = ColorSensor(Port.S1)

threshold = 45
base_speed = 120
kp = 4

samples = 500
sample_time = 5


def set_motor_speeds(left_speed, right_speed):
    left_motor.run(left_speed)
    right_motor.run(right_speed)


def stop_robot():
    left_motor.stop()
    right_motor.stop()


def proportional_control(reflection_value):
    error = threshold - reflection_value
    turn = kp * error

    left_speed = base_speed + turn
    right_speed = base_speed - turn

    print("Reflexión:", reflection_value,
          "Error:", error,
          "Corrección:", turn)

    set_motor_speeds(left_speed, right_speed)


print("Iniciando control proporcional")

for sample in range(samples):
    reflection_value = color_sensor.reflection()

    print("Muestra:", sample + 1)

    proportional_control(reflection_value)

    wait(sample_time)

stop_robot()
print("Control proporcional finalizado")
