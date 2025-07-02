import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
# from colorama import init, Fore, Style

# Dane dostępowe
username = "mqtt_user"
password = "passwd"

servo_angle = 90

servo_pin = 18
in1 = 17
in2 = 27
in3 = 22
in4 = 23

lights = 0

movement_multiplier_value = 0.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

# Adres IP serwera MQTT
server_address = "192.168.0.103"

# Callback do obsługi odbieranych wiadomości
def on_message(client, userdata, message):
    global movement_multiplier_value

    message_payload = message.payload.decode()
    print(f"Odebrano wiadomość na temacie {message.topic}: {message_payload}")

    # Reakcja na treść wiadomości
    if message_payload.lower() == "forward":
        move_forward()
    elif message_payload.lower() == "backward":
        move_backward()
    elif message_payload.lower() == "left":
        turn_left()
    elif message_payload.lower() == "right":
        turn_right()
    elif message_payload.lower() == "left-full":
        servo_to_angle(45)
    elif message_payload.lower() == "right-full":
        servo_to_angle(135)
    elif message_payload.startswith("setMultiplier:"):
        try:
            movement_multiplier_value = float(message_payload.split(":")[1])
            print(f"Aktualna wartość movement_multiplier_value: {movement_multiplier_value}")
            # set_multiplier(multiplier_value)
        except ValueError:
            print("Nieprawidłowy format wartości mnożnika.")

    elif message_payload.startswith("infrared:"):
        try:
            infrared_photo_name = message_payload.split(":")[1]
            ShotPhoto(infrared_photo_name)
        except ValueError:
            print("Nieprawidłowa nazwa zdjęcia podczerwonego")

    elif message_payload.lower() == "readServo":
        set_info_file()
        print("Servo sprawdzone i zapisane do pliku")
    elif message_payload.lower() == "straighten":
        servo_to_angle(90)


    # Dodaj inne warunki zgodnie z Pańskimi potrzebami

def set_info_file():
    try:
        global servo_angle
        angle = servo_angle
        # Otwarcie pliku w trybie nadpisywania
        with open('/var/www/html/info.txt', 'w') as file:
            # Konwersja wartości na ciąg znaków i zapisanie do pliku
            file.write(str(angle))
        print("Zawartość pliku została nadpisana wartością: ", angle)
    except Exception as e:
        print("Wystąpił błąd podczas nadpisywania pliku:", str(e))


def angle_to_pwm(angle):
    duty_cycle = (angle / 18) + 2.5  # Konwersja kąta na wypełnienie PWM
    return duty_cycle

def servo_to_angle(angle):
    global servo_angle
    servo_angle = angle

    print("Servo to angle: " + str(angle))

    if angle < 45:
        angle = 45
        servo_angle = 45
    elif angle > 135:
        angle = 135
        servo_angle = 135

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

# Funkcje do wykonania w zależności od treści wiadomości
def move_forward():
    print("Wywołano funkcję moveForward()")
    global movement_multiplier_value
    print("Wartość mlt: " + str(movement_multiplier_value))

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

    time.sleep(movement_multiplier_value)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

def move_backward():
    print("Wywołano funkcję moveBackward()")
    global movement_multiplier_value

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

    time.sleep(movement_multiplier_value)

    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)

def turn_left():
    global servo_angle
    servo_angle -= 15
    servo_to_angle(servo_angle)
    # min 45

def turn_right():
    global servo_angle
    servo_angle += 15
    servo_to_angle(servo_angle)
    # max 135

def ShotPhoto(filename):
    # filename = "1.jpg"
    filepath = "/var/www/html/images/hercules/" + filename
    # photo_command = "raspistill -o img/" + filename + " -st -t 500 -w 400 -h 300"
    # os.system(photo_command)
    camera = PiCamera()
    camera.start_preview()

    time.sleep(0.5)
    camera.rotation = 180
    camera.capture(filepath, use_video_port=True)
    camera.stop_preview()
    camera.close()

# Tworzenie klienta MQTT
client = mqtt.Client()
# client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, 1)

# Ustawienie nazwy użytkownika i hasła
client.username_pw_set(username, password)

# Przypisanie funkcji do obsługi odbieranych wiadomości
client.on_message = on_message

# Połączenie z serwerem MQTT
client.connect(server_address, 1883, 60)

# Subskrypcja na temat (możesz zmienić na swój temat)
client.subscribe("#", qos=1)

# Pętla główna do oczekiwania na wiadomości
client.loop_forever()
