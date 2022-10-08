import base64


file = open('Readme_encoded_1000_Female.txt', 'r')
lines = file.readlines()

count = 0

for line in lines:
        count += 1
        base64_message = line.strip()
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')
        print(message)

file.close()
