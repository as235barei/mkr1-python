import tkinter as tk


def calculate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        num_squares = (a // c) * (b // c)
        result_label.config(text=f"Кількість квадратів: {num_squares}")

        # Границі прямокутника
        canvas.delete("rectangle")
        canvas.create_rectangle(
            0, 0, a, b, tags="rectangle", outline="darkgreen", fill="lightgreen")

        # Квадрати у прямокутнику
        canvas.delete("squares")
        for i in range(a // c):
            for j in range(b // c):
                canvas.create_rectangle(
                    i * c, j * c, (i + 1) * c, (j + 1) * c, tags="squares", fill="gold", outline="brown")

    except ValueError:
        result_label.config(text="Будь ласка, введіть цілі числа.")


# Графічне вікно
root = tk.Tk()
root.title("Кількість квадратів")

# Створення і відображення елементів
label_a = tk.Label(root, text="Довжина прямокутника «a» (мм):")
label_a.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)
entry_a.insert(0, "100")

label_b = tk.Label(root, text="Ширина прямокутника «b» (мм):")
label_b.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)
entry_b.insert(0, "100")

label_c = tk.Label(root, text="Довжина сторони квадрата «c» (мм):")
label_c.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=5)
entry_c.insert(0, "30")

calculate_button = tk.Button(root, text="Обчислити", command=calculate)
calculate_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

# Канвас
canvas = tk.Canvas(root, width=400, height=400, borderwidth=2, relief='ridge')
canvas.grid(row=5, columnspan=2)

# Старт
root.mainloop()
