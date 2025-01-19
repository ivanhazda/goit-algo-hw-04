def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            total_salary = 0
            count = 0
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total_salary += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка при обробці рядка: {line.strip()}")
                    continue

            if count == 0:
                return 0, 0

            average_salary = round(total_salary / count, 2)
            return total_salary, average_salary
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return 0, 0