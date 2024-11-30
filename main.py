import csv


def process_log(visit_log_path, funnel_log_path):

    try:
        with open(visit_log_path, 'r', newline='', encoding='utf-8', errors='replace') as infile, \
                open(funnel_log_path, 'w', newline='', encoding='utf-8') as outfile:


            reader = csv.reader(infile)
            writer = csv.writer(outfile)


            writer.writerow(['user_id', 'source', 'category'])


            for row in reader:

                if len(row) == 3:
                    user_id, source, category = row

                    if category:
                        writer.writerow([user_id, source, category])
                else:

                    print(f"Пропущена некорректная строка: {row}")
    except UnicodeDecodeError:
        print("Ошибка кодировки при чтении файла. Попробуйте использовать другую кодировку.")
        raise
    except Exception as e:
        print(f"Ошибка при обработке файла: {e}")
        raise


def main():

    visit_log_path = 'visit_log.csv'  # Путь к исходному файлу
    funnel_log_path = 'funnel.csv'  # Путь к итоговому файлу

    process_log(visit_log_path, funnel_log_path)
    print(f"Файл {funnel_log_path} успешно создан.")


if __name__ == '__main__':
    main()