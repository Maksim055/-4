import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt

# Нормы высева
SEED_RATE = {
    "Подсолнечник": 0.2,
    "Ячмень": 2.9,
    "Пшеница": 2.5
}

def calculate_production():
    try:
        area = float(entry_area.get())
        yield_ = float(entry_yield.get())
        production = area * yield_
        entry_production.delete(0, tk.END)
        entry_production.insert(0, round(production, 2))
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числовые данные")

def calculate_waste():
    try:
        production = float(entry_production.get())
        waste = production * 0.03
        entry_waste.delete(0, tk.END)
        entry_waste.insert(0, round(waste, 2))
    except ValueError:
        messagebox.showerror("Ошибка", "Сначала рассчитайте объем производства")

def show_seed_rate():
    culture = culture_var.get()
    rate = SEED_RATE[culture]
    entry_rate.delete(0, tk.END)
    entry_rate.insert(0, rate)

def calculate_seeds():
    try:
        area = float(entry_area.get())
        rate = float(entry_rate.get())
        seeds = area * rate
        entry_seeds.delete(0, tk.END)
        entry_seeds.insert(0, round(seeds, 2))
    except ValueError:
        messagebox.showerror("Ошибка", "Проверьте введенные данные")

def calculate_sales():
    try:
        production = float(entry_production.get())
        waste = float(entry_waste.get())
        seeds = float(entry_seeds.get())
        sales = production - waste - seeds
        entry_sales.delete(0, tk.END)
        entry_sales.insert(0, round(sales, 2))
    except ValueError:
        messagebox.showerror("Ошибка", "Сначала выполните все расчеты")

def show_chart():
    try:
        waste = float(entry_waste.get())
        seeds = float(entry_seeds.get())
        sales = float(entry_sales.get())

        labels = ["Зерноотходы", "Семена", "Реализация"]
        values = [waste, seeds, sales]

        plt.barh(labels, values)
        plt.xlabel("Объем, ц")
        plt.title("Распределение урожая")
        plt.show()
    except ValueError:
        messagebox.showerror("Ошибка", "Недостаточно данных для диаграммы")

# ---------- GUI ----------
root = tk.Tk()
root.title("Расчет плана продажи продукции растениеводства")
root.geometry("500x500")

culture_var = tk.StringVar(value="Подсолнечник")

ttk.Label(root, text="Тип культуры").pack()
ttk.Combobox(root, textvariable=culture_var,
             values=list(SEED_RATE.keys()),
             state="readonly").pack()

ttk.Label(root, text="Площадь посева, га").pack()
entry_area = ttk.Entry(root)
entry_area.pack()

ttk.Label(root, text="Урожайность, ц/га").pack()
entry_yield = ttk.Entry(root)
entry_yield.pack()

ttk.Button(root, text="Объем производства, ц", command=calculate_production).pack()
entry_production = ttk.Entry(root)
entry_production.pack()

ttk.Button(root, text="Объем зерноотходов, ц", command=calculate_waste).pack()
entry_waste = ttk.Entry(root)
entry_waste.pack()

ttk.Button(root, text="Норма посева на 1 га", command=show_seed_rate).pack()
entry_rate = ttk.Entry(root)
entry_rate.pack()

ttk.Button(root, text="Объем зерна на семена, ц", command=calculate_seeds).pack()
entry_seeds = ttk.Entry(root)
entry_seeds.pack()

ttk.Button(root, text="Реализация продукции, ц", command=calculate_sales).pack()
entry_sales = ttk.Entry(root)
entry_sales.pack()

ttk.Button(root, text="Гистограмма распределения урожая", command=show_chart).pack(pady=10)

root.mainloop()
