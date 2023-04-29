import networkx as nx
import matplotlib.pyplot as plt
from lib import *
g = Graph()

while True:
    print("\nВведите текстовое описание графа, 'load' для загрузки графа из файла или 'exit' для выхода:")
    user_input = input().strip().lower()

    if user_input == 'exit':
        break
    elif user_input == 'load':
        print("Введите имя файла:")
        filename = input().strip()
        g.load_from_file(filename)
    else:
        g.generate_graph(user_input)

    g.visualize()
    print("Сохранить граф в файл? (y/n)")
    save = input().strip().lower()
    if save == 'y':
        print("Введите имя файла:")
        filename = input().strip()
        g.save_to_file(filename)