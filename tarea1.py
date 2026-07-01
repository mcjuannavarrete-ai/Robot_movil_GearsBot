# Tarea 1
#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

lef_motor = Motor(Port.A)
right_motor = Motor(Port.B)

print("La configuracion del robot se ha realizado correctamente")
print("\n")

print("inicio el moviminto de mi robot - Hacia adelente")

lef_motor.run_time(300, 2000, wait=False)
right_motor.run_time(300, 2000, wait=True)

print("giro a la derecha")
lef_motor.run_time(300, 800, wait=False)
right_motor.run_time(-300, 800, wait=True)

print("inicio el moviminto de mi robot - Hacia adelente girando a la derecha")

lef_motor.run_time(300, 2000, wait=False)
right_motor.run_time(300, 2000, wait=True)

print("giro a la izquierda")
lef_motor.run_time(- 300, 800, wait=False)
right_motor.run_time(300, 800, wait=True)

print("moviminto de mi robot- Hacia adelente girando a la izquierda")

lef_motor.run_time(300, 2000, wait=False)
right_motor.run_time(300, 2000, wait=True)


print("Robot apagado")
lef_motor.run_time(0,0, wait=False)
right_motor.run_time(0, 0, wait=True)


  
