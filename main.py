import re

substance = input("Введите вещество: ")

print(re.findall('[A-Z][^A-Z]*', substance))