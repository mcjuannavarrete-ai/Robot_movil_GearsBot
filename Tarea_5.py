#!/usr/bin/env pybricks-micropython

from pybricks.ev3devices import Motor, GyroSensor
from pybricks.parameters import Port
from pybricks.tools import wait

left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
gyro_sensor = GyroSensor(Port.S3)

BASE_SPEED = 120
TARGET_ANGLE = 0
GYRO_GAIN = 3
MAX_SPEED = 250
MIN_SPEED = -250
DRIVE_TIME_MS = 90000
SAMPLE_TIME_MS = 90

def clamp(value, min_value, max_value):
    if value < min_value:
        return min_value

    if value > max_value:
        return max_value
    return int(value)

def set_drive_power(left_speed, right_speed):
    left_motor.run(left_speed)
    right_motor.run(right_speed)

def stop_robot():
    left_motor.stop()
    right_motor.stop()
    wait(300)

def drive_straight_with_gyro():
    print("Reiniciando giroscopio")
    gyro_sensor.reset_angle(0)
    wait(1000)
    print("Inicio de movimiento en linea recta")
    elapsed_time = 0
    while elapsed_time < DRIVE_TIME_MS:
        current_angle = gyro_sensor.angle()
        error = TARGET_ANGLE - current_angle
        correction = GYRO_GAIN * error
        # Corrección invertida para GearsBot
        left_speed = clamp(
            BASE_SPEED + correction,
            MIN_SPEED,
            MAX_SPEED
        )
        right_speed = clamp(
            BASE_SPEED - correction,
            MIN_SPEED,
            MAX_SPEED
        )
        print("Angulo:", current_angle)
        print("Error:", error)
        print("Correccion:", correction)
        print("Velocidad izquierda:", left_speed)
        print("Velocidad derecha:", right_speed)
        print("---")
        set_drive_power(left_speed, right_speed)
        wait(SAMPLE_TIME_MS)
        elapsed_time = elapsed_time + SAMPLE_TIME_MS
    stop_robot()
    print("Movimiento recto finalizado")
drive_straight_with_gyro()
