import serial
import sys
import time

class SerialManager:
    def __init__(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)
        self.ser.timeout = 2  # Define un tiempo de espera de 2 segundos para la lectura

    def procesar_texto(self, entrada):
        
        if entrada.startswith("key -e ") :
            cmd = entrada.split(" ")
            self.ser.write((cmd[0] + " " + cmd[1]).encode())
            time.sleep(2)
            # D:/Proyectos/autokey/cont.txt
            with open(cmd[2], "r") as file:
                contenido = file.read() 
                for caracter in contenido:
                    self.ser.write(caracter.encode()) 
                    time.sleep(0.01)
            self.ser.write(bytearray([0x01])) 
        else: 
            self.ser.write(entrada.encode())
        # Esperar un breve momento antes de intentar leer una respuesta
        time.sleep(0.1)
        respuesta = self.leer_respuesta()
        print(respuesta) 

    def leer_respuesta(self):
        # Lee hasta 1024 bytes desde el puerto serial
        respuesta = self.ser.read(1024).decode('utf-8')
        return respuesta.strip()  # Elimina espacios en blanco o caracteres de nueva línea

    def escuchar_entrada(self):
        try:  
            print("Escribe un texto y presiona Enter (Ctrl+C para terminar):")
            while True:
                texto = input()
                self.procesar_texto(texto)
        except KeyboardInterrupt:
            print("\n¡Hasta luego!")
            self.ser.close()
            sys.exit(0)

def main():
    # 'COM3' for Windows, '/dev/ttyUSB0' for Linux or '/dev/tty.usbserial' for macOS.
    manager = SerialManager('COM3', 9600)
    manager.escuchar_entrada()

if __name__ == "__main__":
    main()
