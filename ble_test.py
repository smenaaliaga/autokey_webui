import asyncio
from bleak import BleakScanner, BleakClient

device_address = None

# Función que se llama cuando se detecta un dispositivo.
def detection_callback(device, advertisement_data):
    global device_address
    if device.name == "BT05":
        device_address = device.address

# Función para escanear dispositivos.
async def scan():
    scanner = BleakScanner()
    scanner.register_detection_callback(detection_callback)
    await scanner.start()
    await asyncio.sleep(10)  # Escanea durante 10 segundos.
    await scanner.stop()

# Función para conectarse y comunicarse con el dispositivo.
async def connect_and_communicate(address):
    async with BleakClient(address) as client:
        # Aquí puedes realizar operaciones con el dispositivo.
        # Por ejemplo, leer o escribir características.
        services = await client.get_services()
        for service in services:
            print(service)

# Ejecuta el código.
async def run():
    await scan()
    if device_address:
        print(f"Conectándose a BT05 con dirección {device_address}")
        await connect_and_communicate(device_address)
    else:
        print("No se encontró el dispositivo BT05.")

asyncio.run(run())
