class Teacher:
    def __init__(self, first_name, last_name, age, email, assigned_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.assigned_subjects = set(assigned_subjects)

def create_schedule(subjects, teachers):
    """Розподіл викладачів по предметах"""
    uncovered_subjects = subjects.copy()
    schedule_map = {}

    teachers = sorted(teachers, key=lambda x: len(x.assigned_subjects), reverse=True)

    for teacher in teachers:
        for subject in teacher.assigned_subjects:
            if subject in uncovered_subjects:
                schedule_map[subject] = teacher
                uncovered_subjects.remove(subject)

    return schedule_map if not uncovered_subjects else None

if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', ['Математика', 'Фізика']),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', ['Хімія']),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', ['Інформатика', 'Математика']),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', ['Біологія', 'Хімія']),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', ['Фізика', 'Інформатика']),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', ['Біологія'])
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Розклад занять:")
        for subject, teacher in schedule.items():
            print(f"{subject}: {teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
