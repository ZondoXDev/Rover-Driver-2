const express = require('express');
const Gpio = require('pigpio').Gpio;
const { exec } = require('child_process');
const path = require('path');
const bodyParser = require('body-parser');
const mqtt = require('mqtt');
const cors = require('cors');

// Inicjalizacja GPIO
const servo1 = new Gpio(21, { mode: Gpio.OUTPUT });
const servo2 = new Gpio(20, { mode: Gpio.OUTPUT });

const led = new Gpio(17, { mode: Gpio.OUTPUT });
const buzzer = new Gpio(16, { mode: Gpio.OUTPUT });

// Konfiguracja aplikacji Express
const app = express();
const port = 3000;

app.use(cors()); 

app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const mqttBroker = 'mqtt://192.168.0.19'; // Zastąp IP_RPi_4 rzeczywistym adresem IP Raspberry Pi 4

// Dodaj nazwę użytkownika i hasło do połączenia MQTT (jeśli są wymagane)
const mqttOptions = {
  username: 'mqtt_user',
  password: 'C8FB26FF30A0',
};
const mqttClient = mqtt.connect(mqttBroker, mqttOptions);


mqttClient.on('connect', () => {
  console.log('Connected to MQTT broker');
});

mqttClient.on('error', (error) => {
  console.error('MQTT connection error:', error);
});


function angleToPulseWidth(angle) {
  // Przyjmujemy zakres kątów od 0 do 180
  const minAngle = 0;
  const maxAngle = 180;

  // Zakres szerokości impulsu dla serwomechanizmu
  const minPulseWidth = 500;
  const maxPulseWidth = 2500;

  // Konwersja kąta na pulseWidth
  // Zmiana w linii poniżej, dodanie "+ minPulseWidth" na końcu
  return Math.floor((angle - minAngle) / (maxAngle - minAngle) * (maxPulseWidth - minPulseWidth) + minPulseWidth);
}

// Obsługa przycisków
app.post('/sendDirection', (req, res) => {
  const direction = req.body.order;

  // Dodajemy log przed wysłaniem wiadomości
  console.log(`Sending direction to Raspberry Pi 1: ${direction}`);

  mqttClient.publish('direction', direction, (err) => {
    if (err) {
      console.error('Error publishing direction:', err);
      res.status(500).send('Error sending direction');
    } else {
      console.log('Direction sent successfully');
      res.send('Direction sent to Raspberry Pi 1: ' + direction);
    }
  });
});

app.post('/commandHandler', (req, res) => {
  const command = req.body.command;

  // Dodajemy log przed wysłaniem wiadomości
  console.log(`Sending command to Raspberry Pi 1: ${command}`);

  mqttClient.publish('t_command', command, (err) => {
    if (err) {
      console.error('Error publishing command:', err);
      res.status(500).send('Error sending command');
    } else {
      console.log('Command sent successfully');
      res.send('Command sent to Raspberry Pi 1: ' + command);
    }
  });
});

// Obsługa żądania przesunięcia serwomechanizmu
app.post('/moveServos', (req, res) => {
  const rec_position1 = parseInt(req.body.position1);
  const rec_position2 = parseInt(req.body.position2);

  console.log(`Received for Servo1: ${rec_position1}, Servo2: ${rec_position2}`);

  let position1 = 180-rec_position1;
  let position2 = rec_position2;

  if (
    !isNaN(position1) && position1 >= 0 && position1 <= 180 &&
    !isNaN(position2) && position2 >= 0 && position2 <= 180
  ) {
    servo1.servoWrite(angleToPulseWidth(position1));
    servo2.servoWrite(angleToPulseWidth(position2));
    res.json({ success: true });
  } else {
    res.status(400).json({ error: 'Invalid servo positions' });
  }
});

// Obsługa żądania robienia zdjęcia
app.get('/capturePhoto', (req, res) => {
  const timestamp = new Date().toISOString().replace(/[:]/g, '-').replace('T', '_').split('.')[0];
  const fileName = `photos/photo_${timestamp}.jpg`;
  const width = 1296;
  const height = 972;
  const command = `libcamera-still -t 5 -o ${fileName} --width ${width} --height ${height}`;
  console.log(fileName);

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error capturing photo: ${stderr}`);
      res.status(500).send('Błąd podczas przechwytywania zdjęcia.');
    } else {
      console.log(`Photo captured successfully: ${fileName}`);
      res.type('image/jpeg');
      res.sendFile(__dirname + `/${fileName}`);
    }
  });
});

// Dodana obsługa żądania włączania/wyłączania LED
app.post('/toggleLaser', (req, res) => {
  const ledState = req.body.ledState;

  if (ledState === 'on') {
    led.digitalWrite(1); // Włączanie LED
    res.send('Laser turned on');
  } else if (ledState === 'off') {
    led.digitalWrite(0); // Wyłączanie LED
    res.send('Laser turned off');
  } else {
    res.status(400).json({ error: 'Invalid LED state' });
  }
});

app.post('/buzzer', (req, res) => {
  const buzz_order = req.body.buzz_order;

  if(buzz_order == "pik") {
    buzzer.digitalWrite(1);
    setTimeout(() => {
      buzzer.digitalWrite(0);
    }, 250);
  }
  else if(buzz_order == "tune"){
    // play_melody;
    buzzer.digitalWrite(1);
    setTimeout(() => {
      buzzer.digitalWrite(0);
      setTimeout(() => {
        buzzer.digitalWrite(1);
        setTimeout(() => {
          buzzer.digitalWrite(0);
          setTimeout(() => {
            buzzer.digitalWrite(1);
            setTimeout(() => {
              buzzer.digitalWrite(0);
              setTimeout(() => {
                buzzer.digitalWrite(1);
                setTimeout(() => {
                  buzzer.digitalWrite(0);
                }, 50);
              }, 50);
            }, 50);
          }, 50);
        }, 50);
      }, 50);
    }, 50);
  }
  else {
    res.status(400).json({ error: 'Error' });
  }
});

app.post('/readAcc', async (req, res) => {
  try {
    const pythonProcess = exec('./acc.py');

    let pythonOutput = '';

    // Przechwyć output z procesu podrzędnego
    pythonProcess.stdout.on('data', (data) => {
      pythonOutput += data;
      console.log(`Output z Pythona: ${data}`);
    });

    // Obsłuż błędy, jeśli wystąpią
    pythonProcess.stderr.on('data', (data) => {
      console.error(`Błąd z Pythona: ${data}`);
    });

    // Złap zakończenie procesu
    pythonProcess.on('close', (code) => {
      console.log(`Proces Pythona zakończony z kodem: ${code}`);
      res.status(200).json({ output: pythonOutput });
    });
  } catch (error) {
    console.error('Wystąpił błąd:', error);
    res.status(500).send('Wystąpił błąd podczas przetwarzania zapytania');
  }
});

// Uruchomienie serwera na określonym porcie
app.listen(port, () => {
  console.log(`Aplikacja nasłuchuje na porcie ${port}`);
});
