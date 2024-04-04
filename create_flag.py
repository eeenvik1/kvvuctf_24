from PIL import Image

# Загрузка исходного изображения
source_image = Image.open("flag.png")

# Определение размеров исходного изображения
width, height = source_image.size
print(width, height)

# Определение размеров квадратов
square_size = 20

# Расчет количества квадратов по горизонтали и вертикали
num_squares_horizontal = width // square_size
num_squares_vertical = height // square_size

# Создание нового изображения для склеивания
new_image = Image.new("RGB", (width, height))

# Перебор квадратов в обратном порядке
for y in range(num_squares_vertical - 1, -1, -1):
    for x in range(num_squares_horizontal - 1, -1, -1):
        # Вырезаем квадрат из исходного изображения
        left = x * square_size
        upper = y * square_size
        right = left + square_size
        lower = upper + square_size
        square = source_image.crop((left, upper, right, lower))

        # Определение координат для вставки квадрата в новое изображение
        new_x = (num_squares_horizontal - 1 - x) * square_size
        new_y = (num_squares_vertical - 1 - y) * square_size

        # Вставляем квадрат в новое изображение
        new_image.paste(square, (new_x, new_y))

# Сохраняем новое изображение
new_image.save("otvet.png")