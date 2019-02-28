# Викторина
# Игра на выбор правильного варианта ответа, вопросы которой читаются из текстового файла
# Вопросы записываются по образцу
import sys

def open_file(file_name, mode):
    """Открывает файл"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Невозможно открыть файл", file_name, ". Работа программы будет завершена.\n", e)
        input("\n\nEnter, чтобы выйти.")
        sys.exit()
    else:
        return  the_file

def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла"""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    return category, question, answers, correct, explanation

def welcome(title):
    """Приветсвует игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру 'Векторина'!\n")
    print("Выбрана тема: ", title)

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # извлечение первого блока
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        # вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # получение ответа
        answer = input("Ваш ответ: ")

        # проверка ответа
        if answer == correct:
            print("\nДа!", end=" ")
            score += 1
        else:
            print("\nНет!", end=" ")
        print(explanation)
        print("Счет:", score, "\n\n")

        # переход к следующему вопросу
        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("Это был последний вопрос!")
    print("На вашем счету ", score)

main()
input("\nEnter, чтобы выйти.")