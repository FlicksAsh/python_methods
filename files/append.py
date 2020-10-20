from datetime import datetime
from time import sleep

for i in range(5):
    file_builder = open("files/logger.txt", "a+")
    file_builder.write(f'{datetime.now()}\n')
    file_builder.close()

    print("file created")

    sleep(1)