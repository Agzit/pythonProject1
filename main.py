import csv


def process_log(visit_log_path, funnel_log_path):
    """
    Обрабатывает файл visit_log.csv и записывает в funnel.csv только те визиты,
    где была покупка с указанием категории.
    """
    try:
        with open(visit_log_path, 'r', newline='', encoding='utf-8', errors='replace') as infile, \
                open(funnel_log_path, 'w', newline='', encoding='utf-8') as outfile:

            # Инициализация csv-ридера и писателя
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            # Запись заголовка в новый файл
            writer.writerow(['user_id', 'source', 'category'])

            # Обработка каждой строки из файла visit_log.csv
            for row in reader:
                # Проверяем, что строка не пустая и содержит три элемента
                if len(row) == 3:
                    user_id, source, category = row
                    # Пропускаем строки, в которых нет категории
                    if category:
                        writer.writerow([user_id, source, category])
                else:
                    # Если строка некорректна, можно вывести предупреждение или просто пропустить её
                    print(f"Пропущена некорректная строка: {row}")
    except UnicodeDecodeError:
        print("Ошибка кодировки при чтении файла. Попробуйте использовать другую кодировку.")
        raise
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")
        raise


def main():
    """
    Главная функция, которая запускает обработку файлов.
    """
    visit_log_path = 'visit_log.csv'  # Путь к исходному файлу
    funnel_log_path = 'funnel.csv'  # Путь к итоговому файлу

    process_log(visit_log_path, funnel_log_path)
    print(f"Файл {funnel_log_path} успешно создан.")


if __name__ == '__main__':
    main()