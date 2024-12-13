import asyncio
import logging
from ble_serial.bluetooth.ble_interface import BLE_interface
import socket

# Global variable to store received data as a tuple
rx_buffer = (0, 0, 0)
rx_available = asyncio.Event()  # Event for signaling when data is received

csv_processor = exop.csv_file_processor()


host = host='127.0.0.1'
port=65432





        
# Callback function to handle received data
def receive_callback(value: bytes):

    # Decode incoming bytes and parse them as a tuple of integers
    decoded_value = value.decode('utf-8')
    x, y, z = map(int, decoded_value[1:-2].split(','))
    rx_buffer = (x, y, z)
    print(f"Received: {rx_buffer}")  # Print the received tuple (x, y, z)
    csv_processor.append_data(rx_buffer)
    client_socket.sendall(str(rx_buffer).encode('utf-8'))  # Send data to the server

    rx_available.set()  # Signal that new data has been received

# Main async function to connect and listen for data
async def main():
    # Bluetooth device details
    DEVICE = "30:45:11:F6:3D:3D"  # BLE device address
    ADAPTER = "hci0"  
    SERVICE_UUID = None  
    WRITE_UUID = None  
    READ_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"  # Same UUID for receiving notifications from the HM-10

    # Initialize the BLE interface
    ble = BLE_interface(ADAPTER, SERVICE_UUID)
    ble.set_receiver(receive_callback)  # Set callback for incoming data
    # Connect to the BLE device
    await ble.connect(DEVICE, "public", 10.0)  # Timeout of 10 seconds
    await ble.setup_chars(WRITE_UUID, READ_UUID, "rw")  # Setup characteristics for reading/writing
    # Keep the connection open to listen for incoming data
    csv_processor.generate_new_file()
    try:
        print("Listening for notifications...")
        while True:
            await rx_available.wait()  # Wait until data is received
            rx_available.clear()  # Clear event flag for next data reception
    except KeyboardInterrupt:
        print("Disconnecting...")

    # Disconnect once done
    await ble.disconnect()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print('start')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))  # Connect to the server        
        asyncio.run(main())
