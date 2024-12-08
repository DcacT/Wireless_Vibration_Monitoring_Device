import socket
import threading
from collections import deque
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Deque to store the latest 50 tuples
buffered_data = deque([(0, 0, 0)] * 50, maxlen=50)

# Set up the real-time plot
fig, ax = plt.subplots(figsize=(10, 6))
line_a, = ax.plot([], [], label='a', color='blue')
line_b, = ax.plot([], [], label='b', color='green')
line_c, = ax.plot([], [], label='c', color='red')

# Configure plot aesthetics
ax.set_xlabel('Index (Time Step)')
ax.set_ylabel('Value')
ax.set_title('Real-Time Data Plot')
ax.legend()
ax.grid(True)
ax.set_xlim(0, 49)
ax.set_ylim(0, 100)

# Update function for FuncAnimation
def update_plot(frame):
    a_data, b_data, c_data = zip(*buffered_data)

    # Update the line data
    line_a.set_data(range(len(a_data)), a_data)
    line_b.set_data(range(len(b_data)), b_data)
    line_c.set_data(range(len(c_data)), c_data)

    # Dynamically adjust y-axis limits
    all_data = a_data + b_data + c_data
    min_y = min(all_data)
    max_y = max(all_data)
    margin = 30  # Add some margin for better visualization
    ax.set_ylim(min_y - margin, max_y + margin)

    return line_a, line_b, line_c

# Initialize the plot with empty data
def init_plot():
    line_a.set_data([], [])
    line_b.set_data([], [])
    line_c.set_data([], [])
    return line_a, line_b, line_c

# Set up FuncAnimation to call `update_plot` repeatedly
ani = FuncAnimation(fig, update_plot, init_func=init_plot, interval=200)

# TCP server function
def start_tcp_server(host='127.0.0.1', port=65432):
    """Set up a TCP server that listens for data."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))  # Bind the socket to localhost and the port
        server_socket.listen(5)  # Listen for incoming connections (up to 5 clients)

        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()  # Accept new connection
            print(f"Connected by {addr}")
            threading.Thread(target=handle_client, args=(conn,)).start()

# Handle individual client connections
def handle_client(conn):
    with conn:
        while True:
            data = conn.recv(512)  # Receive up to 1024 bytes of data
            if not data:
                break  # If no data is received, exit loop
            try:
                # Assume data is in the format "(a,b,c)"
                a, b, c = map(int, data.decode('utf-8').strip('()').split(','))
                print(a, b, c)
                buffered_data.append((a, b, c))  # Append to deque
            except Exception as e:
                print(f"Error processing data: {e}")

# Run the TCP server in a separate thread
server_thread = threading.Thread(target=start_tcp_server, daemon=True)
server_thread.start()

# Display the plot
plt.show()
