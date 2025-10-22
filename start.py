from PIL import Image
import os

# Получаем путь к папке, где лежит сам скрипт
folder = os.path.dirname(os.path.abspath(__file__))

# Список допустимых расширений изображений
extensions = ('.png', '.jpeg', '.jpg', '.bmp', '.tiff', '.webp', '.gif')

# Счётчик для имён файлов
counter = 0

for filename in os.listdir(folder):
    if filename.lower().endswith(extensions) and not filename.lower().endswith('.jpg'):
        filepath = os.path.join(folder, filename)
        try:
            with Image.open(filepath) as img:
                # Конвертируем в RGB, чтобы избежать проблем с альфа-каналом
                img = img.convert('RGB')
                new_filename = f"{counter}.jpg"
                new_filepath = os.path.join(folder, new_filename)
                img.save(new_filepath, 'JPEG', quality=100, subsampling=0)
                print(f"✅ {filename} -> {new_filename}")
                counter += 1
        except Exception as e:
            print(f"❌ Ошибка при обработке {filename}: {e}")

print("Готово!")
