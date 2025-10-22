from PIL import Image
import os

# Получаем путь к папке, где лежит сам скрипт
folder = os.path.dirname(os.path.abspath(__file__))

# Список допустимых расширений изображений
extensions = ('.png', '.jpeg', '.jpg', '.bmp', '.tiff', '.webp', '.gif', 'jfif', 'webp')

counter = 0

for filename in os.listdir(folder):
    if filename.lower().endswith(extensions) and not filename.lower().endswith('.jpg'):
        filepath = os.path.join(folder, filename)
        try:
            with Image.open(filepath) as img:
                # Конвертация в RGB для корректного сохранения в JPEG
                img = img.convert('RGB')
                new_filename = f"{counter}.jpg"
                new_filepath = os.path.join(folder, new_filename)
                img.save(new_filepath, 'JPEG', quality=100, subsampling=0)
            
            # Удаляем оригинал только если сохранение прошло успешно
            os.remove(filepath)
            print(f"✅ {filename} -> {new_filename} (оригинал удалён)")
            counter += 1
        except Exception as e:
            print(f"❌ Ошибка при обработке {filename}: {e}")

counter = 24
for filename in os.listdir(folder):
    if  int(filename.title) > 24 and filename.lower().endswith('.jpg'):
        os.rename(filename, f"{counter}.jpg")
        counter += 1
print("Готово!")