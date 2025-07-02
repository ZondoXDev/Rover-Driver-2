## Example python GPIO codes:

## blinker.py

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)

while 0<1:
        GPIO.output(23, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(23, GPIO.LOW)
        time.sleep(0.1)



## rover driver 1.0

import RPi.GPIO as GPIO
import time
from picamera import PiCamera
# from colorama import init, Fore, Style

servo_angle = 175

servo_pin = 18
in1 = 17
in2 = 27
in3 = 22
in4 = 23

lights = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

def servo(angle):
    print("servo")

def angle_to_pwm(angle):
    duty_cycle = (angle / 18) + 2.5  # Konwersja kąta na wypełnienie PWM
    return duty_cycle

def servo_to_angle(angle):

    print("Servo to angle: " + str(angle))

    if angle < 0:
        angle = 0
    elif angle > 180:
        angle = 180

    # Utworzenie obiektu PWM dla serwomechanizmu
    # Inicjalizacja GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms cykl)

    # Konwersja kąta na sygnał PWM
    duty_cycle = angle_to_pwm(angle)

    # Włączenie PWM i ustawienie kąta
    pwm.start(duty_cycle)

    servo_angle = angle

    # Odczekanie chwili
    time.sleep(1)

    # Zatrzymanie PWM
    pwm.stop()
    # GPIO.cleanup()

# Funkcja do wyświetlania logo programu
def display_logo():
    logo = """                                                                  
    //   ) )                                        //    ) )                   
   //___/ /   ___              ___      __         //    / /  __     ( )          ___      __
  / ___ (   //   ) ) ||  / / //___) ) //  ) )     //    / / //  ) ) / / ||  / / //___) ) //  ) )
 //   | |  //   / /  || / / //       //          //    / / //      / /  || / / //       //
//    | | ((___/ /   ||/ / ((____   //          //____/ / //      / /   ||/ / ((____   //
                                                                                                                                                                                                                                                                                                                                                                                                                
    """
    print(logo)

def print_in_colors(white_text, green_text):
    print(f"{Fore.WHITE}{white_text}", end='', flush=True)  # Wypisz pierwszy tekst w kolorze białym
    time.sleep(1)  # Opóźnienie na 1 sekundę
    print(f"{Fore.GREEN}{green_text}{Style.RESET_ALL}")  # Wypisz drugi tekst w kolorze zielonym i przywróć domyślny kolor


def print_subsystem_status(text):
    print(f"\n{Fore.WHITE}{text}", end='', flush=True)
    time.sleep(1)  # Opóźnienie na 1 sekundę

def print_operational_status():
    print(f"{Fore.GREEN}operational{Style.RESET_ALL}", end='')  # Wypisz "operational" w kolorze zielonym w tej samej linii
    time.sleep(1)

def print_inoperational_status():
    print(f"{Fore.RED}inoperational{Style.RESET_ALL}", end='')  # Wypisz "inoperational" w kolorze zielonym w tej samej linii
    time.sleep(1)

def print_launch_abort():
    print(f"\n{Fore.RED}Starting aborted{Style.RESET_ALL}", end='')

def Forward():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)


    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)

    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

    time.sleep(.5)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

def Backward():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)


    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)

    time.sleep(.5)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

def TurnLeft():
    # GPIO.setmode(GPIO.BCM)

    # GPIO.output(in1, GPIO.LOW)
    # GPIO.output(in2, GPIO.LOW)
    # GPIO.output(in3, GPIO.LOW)
    # GPIO.output(in4, GPIO.LOW)

    # # GPIO.output(in1, GPIO.LOW)
    # # GPIO.output(in2, GPIO.HIGH)

    # # GPIO.output(in3, GPIO.HIGH)
    # # GPIO.output(in4, GPIO.LOW)

    # time.sleep(0.1)

    # GPIO.output(in1, GPIO.LOW)
    # GPIO.output(in2, GPIO.HIGH)

    # GPIO.output(in3, GPIO.LOW)
    # GPIO.output(in4, GPIO.HIGH)

    # time.sleep(0.5)

    # GPIO.output(in1, GPIO.LOW)
    # GPIO.output(in2, GPIO.LOW)
    # GPIO.output(in3, GPIO.LOW)
    # GPIO.output(in4, GPIO.LOW)

    servo_to_angle(40)

def TurnRight():
    # GPIO.setmode(GPIO.BCM)

    # GPIO.output(in1, GPIO.LOW)
    # GPIO.output(in2, GPIO.LOW)
    # GPIO.output(in3, GPIO.LOW)
    # GPIO.output(in4, GPIO.LOW)

    # # GPIO.output(in1, GPIO.LOW)
    # # GPIO.output(in2, GPIO.HIGH)

    # # GPIO.output(in3, GPIO.HIGH)
    # # GPIO.output(in4, GPIO.LOW)

    # time.sleep(0.1)

    # GPIO.output(in1, GPIO.HIGH)
    # GPIO.output(in2, GPIO.LOW)

    # GPIO.output(in3, GPIO.HIGH)
    # GPIO.output(in4, GPIO.LOW)

    # time.sleep(0.5)

    # GPIO.output(in1, GPIO.LOW)
    # GPIO.output(in2, GPIO.LOW)
    # GPIO.output(in3, GPIO.LOW)
    # GPIO.output(in4, GPIO.LOW)

    servo_to_angle(130)

def YouSpinMeRound():
    GPIO.setmode(GPIO.BCM)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

    time.sleep(0.1)

    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)

    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)

    time.sleep(5)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

def MoveCameraUp():
    global servo_angle
    servo_angle = servo_angle + 15
    servo_to_angle(servo_angle)

def MoveCameraDown():
    global servo_angle
    servo_angle = servo_angle - 15
    servo_to_angle(servo_angle)

def Beep():
    GPIO.output(25, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(25, GPIO.LOW)
    time.sleep(.1)
    GPIO.output(25, GPIO.HIGH)
    time.sleep(.1)
    GPIO.output(25, GPIO.LOW)

def LightOn():
    GPIO.output(4, GPIO.HIGH)
    global lights
    lights = 1

def LightOff():
    GPIO.output(4, GPIO.LOW)
    global lights
    lights = 0

def ShotPhoto():
    filename = "1.jpg"
    filepath = "/var/www/html/images/01/" + filename
    # photo_command = "raspistill -o img/" + filename + " -st -t 500 -w 400 -h 300"
    # os.system(photo_command)
    camera = PiCamera()
    camera.start_preview()

    time.sleep(0.5)
    camera.capture(filepath, use_video_port=True)
    camera.stop_preview()
    camera.close()



# Funkcja do wykonywania komend
def handle_command(command):
    print(f"Received command: {command}")
    # Tutaj możesz dodać odpowiednie instrukcje do sterowania roverem na podstawie komend
    if command == "W":
        Forward()
    elif command == "S":
        Backward()
    elif command == "D":
        TurnRight()
    elif command == "A":
        TurnLeft()
    elif command == "P":
        ShotPhoto()
    elif command == "I":
        MoveCameraUp()
    elif command == "K":
        MoveCameraDown()
    elif command == "DD":
        YouSpinMeRound()
    elif command == "L":
        if (lights == 0):
            LightOn()
        elif (lights == 1):
            LightOff()
    elif command == "B":
        Beep()
    else:
        return

def check_subsystems():
    # time.sleep(0.5)
    print("Subsystems testing started")

    print_subsystem_status("Servo ... ")

    servo_to_angle(175)
    servo_to_angle(5)
    servo_to_angle(175)

    # time.sleep(2)

    print_operational_status()

    print_subsystem_status("Left wheel ... ")
    print_operational_status()

    print_subsystem_status("Right wheel ... ")
    print_operational_status()

    print_subsystem_status("Powerbank voltage ... ")
    print_operational_status()

    print_subsystem_status("Battery voltage... ")
    print_inoperational_status()
    print_launch_abort()


# Główna pętla programu
display_logo()
print("Podaj komendę: (W - do przodu, S - do tyłu, D - w prawo, A - w lewo, P - zdjęcie, I - kamera w górę, K - kamera w dół, Q - wyjście)")


while True:
    command = input().upper()
    if command == 'Q':
        GPIO.cleanup()
        break
    handle_command(command)

    # Zakończenie programu - czyszczenie GPIO
pwm.stop()
GPIO.cleanup()


## servo.py

import RPi.GPIO as GPIO
import time
import sys

servo_pin = 18

# Inicjalizacja GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Utworzenie obiektu PWM dla serwomechanizmu
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz (20 ms cykl)

# Funkcja do konwersji kąta na sygnał PWM
def angle_to_pwm(angle):
    duty_cycle = (angle / 18) + 2.5  # Konwersja kąta na wypełnienie PWM
    return duty_cycle

try:
    # Sprawdzenie, czy podano poprawny kąt jako parametr uruchomieniowy
    if len(sys.argv) < 2:
        print("Podaj kąt jako parametr uruchomieniowy!")
        sys.exit(1)

    # Pobranie kąta z parametru uruchomieniowego
    angle = float(sys.argv[1])

    # Ograniczenie kąta do zakresu 0-180 stopni
    angle = max(0, min(angle, 180))

    # Konwersja kąta na sygnał PWM
    duty_cycle = angle_to_pwm(angle)

    # Włączenie PWM i ustawienie kąta
    pwm.start(duty_cycle)

    # Odczekanie chwili
    time.sleep(1)

    # Zatrzymanie PWM i wyczyszczenie ustawień GPIO
    pwm.stop()
    GPIO.cleanup()

except KeyboardInterrupt:
    # Obsługa przerwania przez użytkownika (Ctrl+C)
    pwm.stop()
    GPIO.cleanup()


## Project Odyssey: camera2.py:

from time import sleep
from picamera import PiCamera
from datetime import datetime
import subprocess
import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


def analyze(photo_name):
    result1 = subprocess.run(["python", "img/colorDetection.py", photo_name], capture_output=True, text=True, timeout=60)
    return(result1.stdout)

def motor(steps):
    result2 = subprocess.run(["python", "motor.py", str(steps)], capture_output=True, text=True, timeout = 60)
    output = result2.stdout
    # result2.kill()
    return(output)

def comm(color_code):
    result3 = subprocess.run(["python", "comm.py", color_code], capture_output=False, text=True, timeout = 60)
    return(result3.stdout)

def photo(filepath):
    result4 = subprocess.run(["python", "photo.py", filepath], capture_output=False, text=True, timeout = 60)
    return(result4.stdout)


filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.jpg')
filepath = "img/" + filename

        # photo_command = "raspistill -o img/" + filename + " -st -t 500 -w 400 -h 300"
        # os.system(photo_command)

        # photo(filepath)

camera = PiCamera()
camera.resolution = (400, 300)
camera.start_preview()
sleep(0.5)
camera.capture(filepath, use_video_port=True)
camera.stop_preview()
camera.close()

sleep(0.1)

message = analyze(filename)
logging.info('Analyze completed, color: %s', message)
print(message)

if (message.strip().lower() == "yellow"):
                comm('X')
                logging.info('Comm(X)')
                motor(1800)
                comm('Y')

elif (message.strip().lower() == "blue"):
                comm('A')
                logging.info('Comm(A)')
                motor(3300)

elif (message.strip().lower() == "green"):
                comm('F')
                logging.info('Comm(F)')
                motor(1800)
                comm('G')

else:
            pass

        # motor(1800)


        # if (message.strip().lower() == "yellow"):
        #     comm('Y')
        #     pass
        # elif (message.strip().lower() == "blue"):

        #     motor(1500)
        #     pass
        # elif (message.strip().lower() == "green"):
        #     comm('G')
        #     pass
        # else:
        #     pass

sleep(1)
print("Next cube")
logging.info('Program finished')


## Project Odyssey: launcher.py:

from time import sleep
from picamera import PiCamera
from datetime import datetime
import subprocess

while True:

    filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.jpg')
    filepath = "img/" + filename
    photo_command = "raspistill -o img/" + filename + " -st -t 500 -w 400 -h 300"
    # os.system(photo_command)
    camera = PiCamera()
    # camera.resolution = (400, 300)
    camera.start_preview()
    # Czekaj aż kamera się ustabilizuje
    sleep(0.5)
    camera.capture(filepath, use_video_port=True)
    camera.stop_preview()
    camera.close()
    sleep(0.1)
    result2 = subprocess.run(["python", "camera2.py", filename], capture_output=True, text=True, timeout = 60)
    print(result2.stdout)

## Project Odyssey: motor.py:

import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
from time import sleep
import sys

# Set up GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

ile_krokow = sys.argv[1]

# Create a named instance of the BYJMotor class
mymotor = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

# Set the delay time between steps to control the motor speed
delay = 0.0008

# Run the motor for 15000 steps in the counter-clockwise direction with half-step sequence and delay time
mymotor.motor_run([17, 18, 21, 22], delay, int(ile_krokow), False, False, "half", 0.05)

# Clean up GPIO pins
GPIO.cleanup()


## Project Odyssey: shotFoto.py:

import logging
from time import sleep
from datetime import datetime
import subprocess
import os
from picamera import PiCamera

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

def analyze(photo_name):
    logging.info('Funkcja analyze wywołana z argumentem: %s', photo_name)
    result1 = subprocess.run(["python", "img/colorDetection.py", photo_name], capture_output=True, text=True, timeout=60)
    return(result1.stdout)

def motor(steps):
    logging.info('Funkcja motor wywołana z argumentem: %s', steps)
    result2 = subprocess.run(["python", "motor.py", str(steps)], capture_output=True, text=True, timeout = 60)
    return(result2.stdout)

def comm(color_code):
    logging.info('Funkcja comm wywołana z argumentem: %s', color_code)
    result3 = subprocess.run(["python", "comm.py", color_code], capture_output=True, text=True, timeout = 60)
    return(result3.stdout)

def photo(filepath):
    camera = PiCamera()
    camera.resolution = (400, 300)
    camera.start_preview()
    sleep(0.5)
    camera.capture(filepath)
    camera.stop_preview()
    camera.close()

def photo2(filename):
    photo_command = "raspistill -o img/" + filename + " -t 500 -w 400 -h 300"
    os.system(photo_command)

while True:
    # camera = PiCamera()
    try:
        filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.jpg')
        filepath = "img/" + filename

        # photo_command = "raspistill -o img/" + filename + " -t 500 -w 400 -h 300"
        # os.system(photo_command)

        # camera.resolution = (400, 300)
        # camera.start_preview()
        # sleep(0.5)
        # camera.capture(filepath)
        # camera.stop_preview()
        # camera.close()

        # photo(filepath)
        photo2(filename)

        logging.info('Zdjęcie zrobione: %s', filename)

        message = analyze(filename)
        logging.info('Analiza zdjęcia: %s', message)
        print(message)

        if (message.strip().lower() == "yellow"):
            # comm('X')
            logging.info('Komunikacja: kolor żółty - wywołanie funkcji comm("X")')
        elif (message.strip().lower() == "blue"):
            # comm('A')
            logging.info('Komunikacja: kolor niebieski - wywołanie funkcji comm("A")')
        elif (message.strip().lower() == "green"):
            # comm('F')
            logging.info('Komunikacja: kolor zielony - wywołanie funkcji comm("F")')
        else:
            pass

        # motor(1800)
        motor(10)

        if (message.strip().lower() == "yellow"):
            # comm('Y')
            pass
        elif (message.strip().lower() == "blue"):
            # comm('B')
            pass
        elif (message.strip().lower() == "green"):
            # comm('G')
            pass
        else:
            pass

        sleep(2)
        logging.info('Przejście programu zakończyło się')
        pass
    finally:
        # camera.close()
        pass

