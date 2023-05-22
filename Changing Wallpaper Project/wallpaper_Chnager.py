import os
import time
import ctypes

def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 0x0014
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def get_image_files(directory):
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']  # Add more extensions if needed
    image_files = []
    for file in os.listdir(directory):
        if any(file.lower().endswith(ext) for ext in image_extensions):
            image_files.append(os.path.join(directory, file))
    return image_files

if __name__ == '__main__':
    wallpaper_directory = r'C:\Users\manis\Downloads\jpg'  # Replace with your wallpaper directory
    image_files = get_image_files(wallpaper_directory)
    print(image_files)
    if len(image_files) == 0:
        print("No image files found in the specified directory.")
    else:
        while True:
            for image_file in image_files:
                change_wallpaper(image_file)
                time.sleep(30)  # Change wallpaper every 2 minutes
                print(image_files)
