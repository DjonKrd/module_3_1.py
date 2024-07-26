calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    a = string.upper()
    b = string.lower()
    print(len(string), a, b)

def is_contains(string, list_to_search):
    count_calls()
    c = False
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == string.lower():
            c = True
    if c:
        print(True)
    else:
        print(False)




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)