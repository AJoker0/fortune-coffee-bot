# tasks.py
import random
tasks = [
    "Позвони бабушке или дедушке — им это очень важно ❤️",
    "Убери одну вещь в доме. Чисто вокруг = чисто в голове.",
    "Сделай кому-то комплимент сегодня 😌",
    "Напиши другу, с которым давно не общался.",
    "Выключи телефон на 15 минут и просто подыши.",
    "Подари кому-нибудь улыбку 😄",
    "Разгрузи старую папку на рабочем столе!",
    "Полей растение или посади новое 🌱",
    "Напиши себе благодарность за что-то.",
    "Не забудь попить воды 💧",
    "Сделай 10 отжиманий или попрыгай!",
    "Спроси у кого-то: 'Как у тебя дела?' — и выслушай.",
    "Съешь фрукт. Без сахара, но с кайфом 🍎",
    "Выйди на свежий воздух хотя бы на 5 минут.",
    "Сделай доброе дело и никому не говори об этом 🙏",
    "Тщательно отмой плитку в ванной.",
    "Проверь состояние инвестиционного портфеля или начни разбираться в нём.",
    "Составь меню на неделю.",
    "Обнови своё резюме.",
    "Разбери гардероб и отдай ненужное.",
    "Наведи порядок в холодильнике и на кухне.",
    "Добавь напоминания о днях рождения близких.",
    "Вымой окна.",
    "Почисти плинтуса и выключатели.",
    "Разгрузи рабочий стол и сделай систему папок.",
    "Разбери электронную почту.",
    "Начни изучать программирование.",
    "Сделай коллаж, заведи дневник или карту желаний.",
    "Переукрась комнату или освежи интерьер.",
    "Нарисуй что-нибудь под музыку.",
    "Попробуй приготовить новое блюдо.",
    "Сыграй на инструменте или попой песню.",
    "Сделай кому-нибудь комплимент.",
    "Разберись в личном бюджете.",
    "Составь список стран, куда хочешь поехать.",
    "Проверь сроки годности лекарств и косметики.",
    "Сделай домашнее мороженое или смузи.",
    "Сходи на прогулку или катайся на велосипеде.",
    "Позвони родителям или другу, с кем давно не общался.",
    "Послушай лекцию на TED или подкаст.",
    "Разберись в подписках и удали лишнее.",
    "Посети парк, закат или посмотри на звёзды.",
    "Сходи в библиотеку, музей или на выставку.",
    "Организуй пикник или вечер без гаджетов.",
    "Сделай расслабляющий массаж или ванну.",
    "Заведи новое растение и пересади старое.",
    "Сделай украшение своими руками.",
    "Сделай уборку в тех местах, где всегда забываешь.",
    "Попробуй новый стиль в одежде или укладке.",
    "Прочитай книгу по саморазвитию.",
    "Устрой вечеринку для себя или близких.",
    "Повесь новые шторы или зеркало.",
    "Попробуй онлайн-курс по интересной теме.",
    "Напиши письмо себе в будущее или прошлое.",
    "Создай арт-объект из подручных материалов.",
    "Попробуй пилатес, йогу или растяжку.",
    "Понаблюдай за птицами на улице с чашкой кофе.",
    "Собери букет и подари незнакомцу.",
    "Сделай уборку в машине или на балконе.",
    "Придумай 3 способа сделать мир добрее.",
    "Пусть весь день тобой правит твой внутренний ребёнок.",
]


# Функция выдачи случайного задания (без повторов подряд)
last_task = None

def get_random_task():
    global last_task
    new_task = random.choice(tasks)
    while new_task == last_task:
        new_task = random.choice(tasks)
    last_task = new_task
    return new_task