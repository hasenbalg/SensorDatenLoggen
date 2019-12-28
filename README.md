# SensorDatenLoggen
Loggt die Sensordaten von Phoscon

Die Sensornamen muessen oben eingepfegt werden. 

Der Cronjob sieht dann so aus:
```
* * * * * /usr/bin/python3 /home/$USER/sensoren/main.py
```
