import serial
import time

class SMSSender:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for the modem to initialize
            self.setup_modem()
        except serial.SerialException as e:
            print(f"Error initializing serial connection: {e}")

    def setup_modem(self):
        try:
            self.send_command('AT', "Checking modem communication")
            self.send_command('AT+CMGF=1', "Setting SMS mode to text")
        except Exception as e:
            print(f"Error during modem setup: {e}")

    def send_command(self, command, debug_message):
        self.serial.write((command + '\r').encode())
        time.sleep(1)
        response = self.serial.read_all().decode()
        print(f"{debug_message}: {response}")
        return response

    def send_sms(self, phone_number, message):
        try:
            response = self.send_command(f'AT+CMGS="{phone_number}"', "Sending SMS command")
            if ">" in response:
                self.serial.write((message + '\x1A').encode())  # Ctrl+Z to send
                time.sleep(1)
                response = self.serial.read_all().decode()
                print(f"Message send response: {response}")
            else:
                print("Failed to enter SMS sending mode.")
        except serial.SerialException as e:
            print(f"Error sending SMS: {e}")

    def close(self):
        self.serial.close()

def main():
    port = 'COM3'  # Change this to your modem's port
    baudrate = 9600  # Common baudrate for GSM modems
    sender = SMSSender(port, baudrate)

    try:
        phone_number = input("Enter the recipient's phone number in the format +8801XXXXXXXXX: ")
        message = input("Enter the message: ")
        while True:
            sender.send_sms(phone_number, message)
            print("Message sent. Press Ctrl+C to stop.")
            time.sleep(10)  # Wait before sending the next message
    except KeyboardInterrupt:
        print("Stopping SMS sender.")
    finally:
        sender.close()

if __name__ == "__main__":
    main()
