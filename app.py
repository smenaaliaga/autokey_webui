import serial
from flask import Flask, render_template, request
from serial_communicator import SerialCommunicator
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ""
    if request.method == 'POST':
        data_to_send = request.form['textbox_name']
        serial_com.write(data_to_send)
        # Leer la respuesta
        response = serial_com.read_line()
        message = f"Respuesta del dispositivo: {response}"
    
    return render_template('index.html', message=message)
    
if __name__ == '__main__':
    # 'COM3' for Windows, '/dev/ttyUSB0' for Linux or '/dev/tty.usbserial' for macOS.
    serial_com = SerialCommunicator('COM3', 9600)
    #webbrowser.open("http://127.0.0.1:5000/")
    try:
        app.run(debug=True, use_reloader=False)
    finally:
        serial_com.close()  # Asegúrate de cerrar la conexión serial al terminar
