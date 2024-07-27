let servo_angle_js = 90;
        let photo_url_vis = "";
        let photo_url_infrared = "";

        function centralizeCamera() {
            switch(servo_angle_js){
                case 45:
                moveServosToAngle(64, 54); break;
                case 60:
                moveServosToAngle(79, 54);break;
                case 75:
                moveServosToAngle(92, 55);break;
                case 90:
                moveServosToAngle(110, 57);break;
                case 105: 
                moveServosToAngle(123, 58);break;
                case 120:
                moveServosToAngle(140, 59);break;
                case 135:
                moveServosToAngle(153, 59); break;
            }
        }
        function turnLeft(){
            servo_angle_js -= 15;
            if (servo_angle_js < 45) servo_angle_js = 45;
            console.log("Servo: " + servo_angle_js);
            setTimeout(() => {
                updateTurnPreview();
            }, 500);
        }
        function turnLeftFull(){
            servo_angle_js = 45;
            setTimeout(() => {
                updateTurnPreview();
            }, 500);
        }
        function turnRight(){
            servo_angle_js += 15;
            if (servo_angle_js > 135) servo_angle_js = 135;
            console.log("Servo: " + servo_angle_js);
            setTimeout(() => {
                updateTurnPreview();
            }, 500);
        }
        function turnRightFull(){
            servo_angle_js = 135;
            
            setTimeout(() => {
                updateTurnPreview();
            }, 500);
        }
        function updateTurnPreview() {
            var rotationPreview = document.getElementById('rover-front');
            var newRotationValue = servo_angle_js - 90;
            rotationPreview.style.transform = 'rotate(' + newRotationValue + 'deg)';
        }

        function sendCommand(command){
            fetch("/commandHandler", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ command }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log("Command send successfully");
                } else {
                    console.log("Error");
                }
            })
            .catch(error => {
                console.error("Wystąpił błąd:", error);
            });
        }

        function giveOrder(order){
            fetch("/sendDirection", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ order }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log("Order successful");
                } else {
                    console.log("Error");
                }
            })
            .catch(error => {
                console.error("Wystąpił błąd:", error);
            });
        }

        function startTimer() {
          const progressBar = document.getElementById('progress');
          progressBar.style.transition = 'width 3s linear';
          progressBar.style.width = '100%';
          setTimeout(() => {
            progressBar.style.transition = 'width 0.1s linear';
            progressBar.style.width = '0';
            // progressBar.style.width = '0';
            // document.getElementById('progress-bar').style.opacity = 0;
            //     setTimeout(() => {
            //     document.getElementById('progress-bar').style.display = "none";
            // }, 500);
          }, 3000);
        }

        function moveServos() {
            let result_p = document.getElementById("result-p");

            const position1 = parseInt(document.getElementById("servoPosition").value);
            const position2 = parseInt(document.getElementById("servoPosition2").value);

            console.log(position1 + ";" + position2);

            fetch("/moveServos", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ position1, position2 }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    result_p.innerHTML = "Kąty ustawione pomyślnie!";
                    setTimeout(() => {
                        result_p.innerHTML = "";
                    }, 500);
                } else {
                    result_p.innerHTML = "Błąd ustawiania kątów";
                }
            })
            .catch(error => {
                console.error("Wystąpił błąd:", error);
            });
        }

        function moveServosToAngle(position1, position2) {
            let result_p = document.getElementById("result-p");

            document.getElementById("servoPosition").value = position1;
            document.getElementById("servoPosition2").value = position2;

            console.log(position1 + ";" + position2);

            fetch("/moveServos", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ position1, position2 }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    result_p.innerHTML = "Kąty ustawione pomyślnie!";
                    setTimeout(() => {
                        result_p.innerHTML = "";
                    }, 500);
                } else {
                    result_p.innerHTML = "Błąd ustawiania kątów";
                }
            })
            .catch(error => {
                console.error("Wystąpił błąd:", error);
            });
        }

        function superCargo(operation) {
            let result_p = document.getElementById("result-p");

            console.log(operation);
            
            if (operation == "open"){
                console.log("Opening SuperCargo!");
              }
              else if (operation == "close"){
                  console.log("Closing SuperCargo!");
              }

            fetch("/superCargo", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ operation }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    result_p.innerHTML = "Operacja wykonana";
                    setTimeout(() => {
                        result_p.innerHTML = "";
                    }, 500);
                } else {
                    result_p.innerHTML = "Coś się nie udało";
                }
            })
            .catch(error => {
                console.error("Wystąpił błąd:", error);
            });
        }
        // crane
        function crane(operation) {
            let result_p = document.getElementById("result-p");

            console.log(operation);

            fetch("/crane", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ operation }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    result_p.innerHTML = "Operacja wykonana";
                    setTimeout(() => {
                        result_p.innerHTML = "";
                    }, 500);
                } else {
                    result_p.innerHTML = "Coś się nie udało";
                }
            })
            .catch(error => {
                console.error("Wystąpił błąd:", error);
            });
        }


        function capturePhoto() {
            fetch('/capturePhoto')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Błąd podczas przechwytywania zdjęcia.');
                    }
                    return response.blob();
                })
                .then(photoBlob => {
                    const url = URL.createObjectURL(photoBlob);
                    photo_url_vis = url;
                    document.getElementById('capturedPhoto').src = url;
                    // document.getElementById('capturedPhoto').style.width = "600px";
                })
                .catch(error => {
                    console.error(error);
                    alert('Wystąpił błąd podczas przechwytywania zdjęcia.');
                });
        }
        let lastInfUrl = "";
        function captureInfrared() {
            const timestamp = new Date().toISOString().replace(/[:]/g, '-').replace('T', '_').split('.')[0];
            const fileName = `photo_${timestamp}.jpg`;
            console.log(fileName);
            let command = "infrared:" + fileName;
            giveOrder(command);
            let url = "http://192.168.0.17/images/hercules/" + fileName;
            lastInfUrl = url;
            document.getElementById('capturedInfrared').src = url;
        }
        function refreshInf() {
            document.getElementById('capturedInfrared').src = lastInfUrl;
        }

        function openPhotoVis() {
            window.open(photo_url_vis);
        }
        function readServoFromTxt() {
            // Pobierz referencję do iframe
            const iframe = document.getElementById('mojIframe');

            // Odśwież iframe
            iframe.contentWindow.location.reload();

        }
        function toggleLed(ledState) {
            fetch("/toggleLaser", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ ledState }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log("LED toggled successfully");
                } else {
                    console.log("Error toggling LED");
                }
            })
            .catch(error => {
                console.error("Wystąpił błąd:", error);
            });
        }

        function buzzer(buzz_order) {
            fetch("/buzzer", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ buzz_order }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log("Success");
                } else {
                    console.log("Error ");
                }
            })
            .catch(error => {
                console.error("Wystąpił błąd:", error);
            });
        }

        // Dodano obsługę checkboxa w HTML
        const checkbox = document.getElementById('ledCheckbox');

        checkbox.addEventListener('change', () => {
            const ledState = checkbox.checked ? 'on' : 'off';
            toggleLed(ledState);
        });

        // async function fetchDataAndDisplay() {
        //     try {
        //     const response = await fetch('/readAcc', { method: 'POST' });
        //     const data = await response.json();
            
        //     // Wywołaj funkcję do przetwarzania danych
        //     const { X, Y, Z } = extractAccelerationValues(data.output);

        //     // Wyświetl dane w odpowiednim formacie
        //     const accelerationValues = document.getElementById('acceleration-values');
        //     accelerationValues.innerText = `X=${X.toFixed(3)}, Y=${Y.toFixed(3)}, Z=${Z.toFixed(3)}`;
        //     } catch (error) {
        //     console.error('Wystąpił błąd:', error);
        //     }
        // }

        // document.getElementById('readAccButton').addEventListener('click', fetchDataAndDisplay);

        // // Automatyczne odświeżanie co 1 sekundę
        // setInterval(fetchDataAndDisplay, 1000);

        // // Funkcja do przetwarzania danych
        // function extractAccelerationValues(dataString) {
        //     const valuesArray = dataString.split(',').map(item => parseFloat(item.split('=')[1]));
        //     return { X: valuesArray[0], Y: valuesArray[1], Z: valuesArray[2] };
        // }

