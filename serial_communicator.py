# serial_communicator.py

import serial
import time

class SerialCommunicator:
    def __init__(self, port='COM3', baudrate=9600):
        self.ser = serial.Serial(port, baudrate)
        self.ser.timeout = 2
        self.chunk_size = 32
        self.pause_time = 0.2
    
    def write(self, data):
        """Escribe datos en el puerto serial."""
        for i in range(0, len(data), self.chunk_size):
            chunk = data[i:i+self.chunk_size]
            self.ser.write(chunk.encode())
            time.sleep(self.pause_time)

    def read_line(self):
        """Lee una línea desde el puerto serial y la devuelve."""
        return self.ser.readline().decode().strip()

    def close(self):
        """Cierra la conexión serial."""
        self.ser.close()
