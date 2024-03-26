#!/usr/bin/env python
import board
import busio
import adafruit_adxl34x
import time  # Dodana biblioteka time

# Utwórz obiekt magistrali I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Utwórz obiekt czujnika ADXL345
accelerometer = adafruit_adxl34x.ADXL345(i2c)

        # Odczytaj wartości przyspieszenia
x, y, z = accelerometer.acceleration

        # Wyświetl odczytane dane
print("X={0:0.3f}, Y={1:0.3f}, Z={2:0.3f}".format(x, y, z))