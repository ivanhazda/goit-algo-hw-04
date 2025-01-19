def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats_info.append(cat_info)
                except ValueError:
                    print(f"Помилка при обробці рядка: {line.strip()}")
                    continue
        return cats_info
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []