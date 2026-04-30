# move_files.py
import shutil
import os

source = "sample.txt"
destination_dir = "Practice6/data/nested_dir"
destination = os.path.join(destination_dir, "sample.txt") #чтоб правильно соединять пути

# Move file
shutil.move(source, destination) #файлдармен жумыска керек для копирования файла
print(f"{source} moved to {destination_dir}")

# Copy file back
shutil.copy(destination, ".") #файл обратно копируется
print(f"{source} copied back to current directory")