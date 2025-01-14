from collections import deque

def is_palindrome(string):
    # Очищаємо рядок: видаляємо пробіли та переводимо в нижній регістр
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    char_deque = deque(cleaned_string) 

    # Перевіряємо, чи збігаються символи з початку і кінця
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False 
    return True

# Тестові приклади
test_strings = [
    "hello",
    "дед",
    "12321",
    "аргентина манит негра",
    "mp pm",
    "big track",
]

for string in test_strings:
    print(f"'{string}': {'паліндром' if is_palindrome(string) else 'не паліндром'}")