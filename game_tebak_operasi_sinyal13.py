import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Membuat GUI
root = tk.Tk()
root.title("Game Tebak Operasi dan Fungsi Trigonometri")

# Nama-nama operasi yang diperbolehkan
allowed_operations = ['penjumlahan', 'pengurangan', 'perkalian']

# Fungsi-fungsi trigonometri yang dapat dipilih secara acak
trig_functions = ['sin', 'cos', 'tan']

# Fungsi untuk menghasilkan sinyal sinusoidal dengan parameter amplitudo dan frekuensi acak
def generate_signal(amplitude, frequency, trig_function):
    # Memastikan frekuensi berada dalam rentang yang diinginkan (0-2)
    frequency = min(frequency, 2)
    t = np.linspace(0, 1, 1000)  # Menyusun sinyal dalam rentang waktu 0-1 detik
    if trig_function == 'sin':
        return amplitude * np.sin(2 * np.pi * frequency * t)
    elif trig_function == 'cos':
        return amplitude * np.cos(2 * np.pi * frequency * t)
    elif trig_function == 'tan':
        return amplitude * np.tan(2 * np.pi * frequency * t)

# Fungsi untuk menjalankan permainan
def start_game():
    # Memilih secara acak operasi matematika
    math_operation = np.random.choice(allowed_operations)
    # Memilih secara acak dua fungsi trigonometri
    trig_function1 = np.random.choice(trig_functions)
    trig_function2 = np.random.choice(trig_functions)
    # Memilih secara acak amplitudo dan frekuensi untuk kedua fungsi
    amplitude1 = np.random.uniform(0, 1)
    amplitude2 = np.random.uniform(0, 1)
    frequency1 = np.random.uniform(0, 2)  # Frekuensi dibatasi hingga 2 per detik
    frequency2 = np.random.uniform(0, 2)
    # Menghasilkan sinyal dari kedua fungsi trigonometri
    signal1 = generate_signal(amplitude1, frequency1, trig_function1)
    signal2 = generate_signal(amplitude2, frequency2, trig_function2)
    # Menampilkan plot sinyal pada GUI
    plot_signal(signal1, signal2, math_operation, trig_function1, trig_function2)

# Fungsi untuk menampilkan plot sinyal pada GUI
def plot_signal(signal1, signal2, math_operation, trig_function1, trig_function2):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(6, 9))  # Membuat subplot untuk setiap sinyal
    ax1.plot(signal1, label='Signal 1')
    ax1.set_ylabel('Amplitudo')
    ax1.set_title('Signal 1 (' + trig_function1 + ')')
    ax1.grid(True)
    ax1.legend()
    ax2.plot(signal2, label='Signal 2')
    ax2.set_ylabel('Amplitudo')
    ax2.set_title('Signal 2 (' + trig_function2 + ')')
    ax2.grid(True)
    ax2.legend()
    
    # Operasi antara kedua sinyal
    output_signal = signal1 + signal2
    ax3.plot(output_signal, label='Output Signal')
    ax3.set_xlabel('Waktu')
    ax3.set_ylabel('Amplitudo')
    ax3.set_title('Output Signal (' + math_operation + ')')
    ax3.grid(True)
    ax3.legend()

    plt.tight_layout()  # Menyesuaikan tata letak subplot
    plt.show()

# Fungsi untuk mengecek jawaban pengguna
def check_answer():
    user_answer = entry.get()
    if user_answer.lower() in allowed_operations:
        messagebox.showinfo("Jawaban Benar", "Selamat! Jawaban Anda benar!")
        start_game()
    else:
        messagebox.showerror("Jawaban Salah", "Maaf, jawaban Anda salah. Silakan coba lagi.")

# Button untuk memulai permainan
start_button = tk.Button(root, text="Mulai Permainan", command=start_game)
start_button.pack()

# Entry untuk input jawaban pengguna
entry = tk.Entry(root)
entry.pack()

# Button untuk memeriksa jawaban pengguna
check_button = tk.Button(root, text="Periksa Jawaban", command=check_answer)
check_button.pack()

# Label untuk informasi tentang operasi yang diperbolehkan
allowed_operations_label = tk.Label(root, text=f"Operasi yang diperbolehkan: {', '.join(allowed_operations)}")
allowed_operations_label.pack()

root.mainloop()
