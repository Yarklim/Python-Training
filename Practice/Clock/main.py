import time
import tkinter as tk


def update_clock(label: tk.Label) -> None:
    label.config(text=time.strftime("%H:%M:%S"))
    label.after(1000, update_clock, label)


def main() -> None:
    root = tk.Tk()
    root.title("Clock")
    root.resizable(width=False, height=False)

    clock_label = tk.Label(root, font=("Arial", 100))
    clock_label.pack()

    update_clock(clock_label)

    root.mainloop()


if __name__ == "__main__":
    main()
