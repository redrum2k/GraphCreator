import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
import json
import time
import tkinter.messagebox as mb

#Класс Graph соержит в себе основную функцию, необзодимую для генерации графа
class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    #generate_graph позволяет генерировать граф с помощью текстового описания
    def generate_graph(self, description):
        self.graph.clear()
        words = description.split()
        print(words)
        if "полный" in words:
            for i in range(len(words)):
                if '0' in words[i] or '1' in words[i] or '2' in words[i] or '3' in words[i] or '4' in words[i] or '5' in words[i] or '6' in words[i] or '7' in words[i] or '8' in words[i] or '9' in words[i]:
                    n = int(words[i])
                    break
            if n > 40:
                mb.showerror("Ошибка", "Превышено максимальное количество вершин")
                return
            self.graph = nx.complete_graph(n)
        elif "дерево" in words:
            for i in range(len(words)):
                if words[i] == "вершинах" or words[i] == "вершинами" or words[i] == "вершиной":
                    n = int(words[i-1])
                    if n > 100:
                        mb.showerror("Ошибка", "Превышено максимальное количество вершин")
                        return
                    self.graph = nx.balanced_tree(n-1, 1)
                    break
                elif words[i] == 'листьями' or words[i] == "листьях" or words[i] == "листом":
                    n = int(words[i - 1])
                    if n > 100:
                        mb.showerror("Ошибка", "Превышено максимальное количество вершин")
                        return
                    self.graph = nx.balanced_tree(n, 1)
                    break

        elif "связность" in words or "связности" in words or "связностями" in words:
            n = int(words[words.index("связности") - 2])
            if n > 33:
                mb.showerror("Ошибка", "Превышено максимальное количество вершин")
                return
            self.graph = nx.caveman_graph(n, 3)

    #save_to_file позволяет пользователю сохранять граф с любую директорию
    def save_to_file(self, filename):
        graph_data = nx.to_dict_of_dicts(self.graph)
        with open(filename, "w") as f:
            json.dump(graph_data, f)

    #load_from_file позволяет пользователю открывать созданный ранее граф. Он может загружать его из любой директории на своем компьютере
    def load_from_file(self, filename):
        with open(filename, "r") as f:
            graph_data = json.load(f)
        self.graph = nx.from_dict_of_dicts(graph_data)

#generate_graph передает с функцию generaph_graph класса Graph текстовое описание, по которому генерирует граф. После этого, оно визуализирует его и выдает его в GUI
def generate_graph():
    description = graph_description.get("1.0", "end-1c")
    g.generate_graph(description)
    visualize_graph(g.graph)
    save_button.pack(side=tk.LEFT, padx=5)

#load_graph открывает файл, переданный пользователем (файл должен быть формата .grp), и, используя его содержимое, делает граф
def load_graph():
    filename = filedialog.askopenfilename()
    if filename:
        g.load_from_file(filename)
        visualize_graph(g.graph)
        save_button.pack(side=tk.LEFT, padx=5)

#save_graph сохраняет созданный пользователем граф
def save_graph():
    filename = filedialog.asksaveasfilename(defaultextension=".grp")
    if filename:
        g.save_to_file(filename)
#visualize_graph визуализирует созданный пользователем граф
def visualize_graph(graph):
    plt.clf()
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    canvas.draw_idle()

#Далее идет основной цикл программы, в котором созадется весь GUI
g = Graph()
root = tk.Tk()
root.geometry("700x500")
root.title("Генератор случайных графов")

graph_description = tk.Text(root, wrap=tk.WORD, height=5)
graph_description.pack(padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(padx=10, pady=10)

send_button = tk.Button(btn_frame, text="Отправить", command=generate_graph())
send_button.pack(side=tk.LEFT)

load_button = tk.Button(btn_frame, text="Загрузить граф", command=load_graph)
load_button.pack(side=tk.LEFT)

save_button = tk.Button(btn_frame, text="Сохранить граф", command=save_graph, bg="red")
save_button.pack_forget()

figure = plt.figure(figsize=(5, 4))
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

root.mainloop()