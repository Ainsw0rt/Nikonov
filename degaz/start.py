from PIL import Image
import os

# Путь к папке, где находится сам скрипт
folder = os.path.dirname(os.path.abspath(__file__))

# Допустимые расширения изображений
extensions = ('.png', '.jpeg', '.jpg', '.bmp', '.tiff', '.webp', '.gif', 'jfif')

# Счётчик для новых имён
counter = 0

# Сначала собираем список всех файлов с изображениями
files = [f for f in os.listdir(folder) if f.lower().endswith(extensions)]

# Чтобы избежать конфликтов имён, сортируем и создаём временные имена
for filename in sorted(files):
    filepath = os.path.join(folder, filename)
    try:
        with Image.open(filepath) as img:
            # Конвертируем в RGB, чтобы избежать проблем с альфа-каналом
            img = img.convert('RGB')
            new_filename = f"{counter}.jpg"
            new_filepath = os.path.join(folder, new_filename)
            
            # Сохраняем в JPEG без сжатия
            img.save(new_filepath, 'JPEG', quality=100, subsampling=0)
        
        # Удаляем оригинал
        os.remove(filepath)
        print(f"✅ {filename} -> {new_filename} (оригинал удалён)")
        counter += 1
    except Exception as e:
        print(f"❌ Ошибка при обработке {filename}: {e}")

print("Готово!")
