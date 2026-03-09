# Hercules Rover Control System 🚗

![Hercules Rover](Hercules_rover.jpg)

Control software for the **Hercules exploration rover**.

This repository contains the main control software used to operate the rover remotely.  
The system combines a **Node.js control server with a web interface** and a **Python hardware driver** responsible for low-level control of motors, servos and the camera.

The rover was designed as a small experimental robotics platform capable of remote exploration inside an apartment environment.

---

## System Architecture 🛠️

The rover software is divided into two main components.

### Control Server (Node.js)

Runs on a Raspberry Pi 4 and provides:

- web-based control interface
- REST API for rover commands
- MQTT communication with the rover driver
- servo and auxiliary hardware control

The interface allows remote operation directly from a browser.

### Rover Driver (Python)

Runs on a Raspberry Pi 1 mounted inside the rover.

Responsible for:

- DC motor control
- steering servo control
- camera capture
- executing commands received through MQTT

---

## Communication 📡

Both parts of the system communicate using **MQTT**.

Command flow:

Web Interface  
↓  
Node.js Control Server  
↓  
MQTT Broker  
↓  
Python Rover Driver  
↓  
Hardware (motors, servos, camera)

This architecture separates the **user interface layer** from the **hardware control layer**.

---

## Hardware 🔨

Main hardware components used in the rover:

- Raspberry Pi 4 (control server)
- Raspberry Pi 1 (rover driver)
- DC motors with motor driver
- steering servo
- Raspberry Pi NoIR infrared camera
- Raspberry Pi standard camera
- two 2W IR reflectors for night vision
- COB LED front lighting
- relay-controlled electromagnet
- Li-ion battery power system

Additional lighting is installed:

- on the camera mast
- inside the cargo section
- on the front of the rover

---

## Features ✨

The system allows remote control of the rover including:

- forward and backward movement
- steering control
- servo manipulation
- camera image capture
- lighting control
- electromagnet activation
- sensor reading

The rover completed around **20 remote exploration runs** between rooms in a ~20 meter indoor environment.


---

## Technologies ✈️

- Python  
- Node.js  
- Express  
- MQTT  
- Raspberry Pi GPIO  
- JavaScript  
- HTML / CSS

---

## Demo 🎥

Video demonstration of the rover: [CLICK](https://youtu.be/zd5MRYK65yc)

---

## Purpose of the Project 🤔

The project was created as an experimental platform for learning:

- robotics systems
- hardware/software integration
- MQTT communication
- Raspberry Pi hardware control
- remote robotics interfaces
