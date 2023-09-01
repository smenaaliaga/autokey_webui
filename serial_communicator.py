# serial_communicator.py

import serial

class SerialCommunicator:
    def __init__(self, port='COM3', baudrate=9600):
        self.ser = serial.Serial(port, baudrate)
        self.ser.timeout = 2
    
    def write(self, data):
        """Escribe datos en el puerto serial."""
        self.ser.write(data.encode())

    def read_line(self):
        """Lee una línea desde el puerto serial y la devuelve."""
        return self.ser.readline().decode().strip()

    def close(self):
        """Cierra la conexión serial."""
        self.ser.close()
