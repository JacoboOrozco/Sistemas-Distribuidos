import zmq
import time
import socket
import sys
import json
"""
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:5555")
"""

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client Socket Created')
host = 'localhost'
port = 5433



def main():
    userControler()


def printMenu():
    print('----- Welcome to our Calculator Service -----')
    print('Press a to add')
    print('Press s to subtract')
    print('Press m to multiply')
    print('Press d to divide')
    print('Press p to power')
    print('Press l for logarithm')
    print('Press e to exit')

def add(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = json.dumps({"data": arrayData})
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        client_socket.sendto(data.encode(), (host, 5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print('From middleserver: ', confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        res = "0"
        client_socket.sendto(res.encode(), (host, 5432))
        result, socket = client_socket.recvfrom(4096)
        result = result.decode()
        print('The result of adding: ' + result)
    except Exception as e:
        print(e)

def subtract(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = json.dumps({"data": arrayData})
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        client_socket.sendto(data.encode(), (host, 5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print('From middleserver: ', confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        res = "0"
        client_socket.sendto(res.encode(), (host, 5432))
        result, socket = client_socket.recvfrom(4096)
        result = result.decode()
        print('The result of subtracting: ' + result)
    except Exception as e:
        print(e)

def multiply(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = json.dumps({"data": arrayData})
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        client_socket.sendto(data.encode(), (host, 5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print('From middleserver: ', confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        res = "0"
        client_socket.sendto(res.encode(), (host, 5432))
        result, socket = client_socket.recvfrom(4096)
        result = result.decode()
        print('The result of multiplying: ' + result)
    except Exception as e:
        print(e)

def divide(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = json.dumps({"data": arrayData})
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        client_socket.sendto(data.encode(), (host, 5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print('From middleserver: ', confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        res = "0"
        client_socket.sendto(res.encode(), (host, 5432))
        result, socket = client_socket.recvfrom(4096)
        result = result.decode()
        print('The result of dividing: ' + result)
    except Exception as e:
        print(e)

def power(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = json.dumps({"data": arrayData})
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        client_socket.sendto(data.encode(), (host, 5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print('From middleserver: ', confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        res = "0"
        client_socket.sendto(res.encode(), (host, 5432))
        result, socket = client_socket.recvfrom(4096)
        result = result.decode()
        print('The result of exponentiation: ' + result)
    except Exception as e:
        print(e)

def logarithm(opt, number1, number2):
    arrayData = [opt, number1, number2]
    data = json.dumps({"data": arrayData})
    """Sending numbers 1 & 2 and recieving confirmation"""
    try:
        print('Client first number: '+ number1)
        print('Client second number: '+ number2)
        client_socket.sendto(data.encode(), (host, 5432))
        confirmation, socket = client_socket.recvfrom(4096)
        confirmation = confirmation.decode()
        print('From middleserver: ', confirmation)
    except Exception as e:
        print(e)
    """Getting result"""
    try:
        res = "0"
        client_socket.sendto(res.encode(), (host, 5432))
        result, socket = client_socket.recvfrom(4096)
        result = result.decode()
        print('The result of logarithm: ' + result)
    except Exception as e:
        print(e)

def userControler():
    option = True
    while option:
        printMenu()
        opt = input('>>>')
        if opt == 'a':
            number1 = input('Please enter the first number for addition: ')
            number2 = input('Please enter the second number for addition: ')
            add(opt, number1, number2)
        elif opt == 's':
            number1 = input('Please enter the first number for subtraction: ')
            number2 = input('Please enter the second number for subtraction: ')
            subtract(opt, number1, number2)
        elif opt == 'm':
            number1 = input('Please enter the first number for multiplication: ')
            number2 = input('Please enter the second number for multiplication: ')
            multiply(opt, number1, number2)
        elif opt == 'd':
            number1 = input('Please enter the first number for division: ')
            number2 = input('Please enter the second number for division: ')
            divide(opt, number1, number2)
        elif opt == 'p':
            number1 = input('Please enter the base: ')
            number2 = input('Please enter the power/exponent: ')
            power(opt, number1, number2)
        elif opt == 'l':
            number1 = input('Please enter the base: ')
            number2 = input('Please enter the number: ')
            logarithm(opt, number1, number2)
        elif opt == 'e':
            client_socket.close()
            print('Client socket closed')
            option = False
        else:
            print('Please enter a valid option')
            sleep(2)
            userControler()
        """







        """



if __name__ == "__main__":
    main()
