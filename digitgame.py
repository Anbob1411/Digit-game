import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("4-Digit Two Player Game")
root.geometry("420x450")


# ---------- Game Logic ----------
def check_guess(guess, secret):
    same_pos = 0
    same_digit = 0

    for i in range(4):
        if guess[i] == secret[i]:
            same_pos += 1

    for d in set(guess):
        if d in secret:
            same_digit += 1

    return same_digit, same_pos


def submit_guess():
    p1_secret = e_p1_secret.get()
    p2_secret = e_p2_secret.get()
    p1_guess = e_p1_guess.get()
    p2_guess = e_p2_guess.get()

    # Validation
    if not all(x.isdigit() and len(x) == 4 for x in
               [p1_secret, p2_secret, p1_guess, p2_guess]):
        messagebox.showerror("Error", "All entries must be exactly 4 digits")
        return

    d1, p1 = check_guess(p1_guess, p2_secret)
    d2, p2 = check_guess(p2_guess, p1_secret)

    result.set(
        f"Player-1:\nCommon digits: {d1}\nMatching positions: {p1}\n\n"
        f"Player-2:\nCommon digits: {d2}\nMatching positions: {p2}"
    )

    if p1 == 4:
        messagebox.showinfo("Winner", "🎉 Player-1 Wins!")
    elif p2 == 4:
        messagebox.showinfo("Winner", "🎉 Player-2 Wins!")


# ---------- UI ----------
tk.Label(root, text="4-Digit Two Player Game",
         font=("Arial", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Player-1 Secret").grid(row=0, column=0)
tk.Label(frame, text="Player-2 Secret").grid(row=1, column=0)

e_p1_secret = tk.Entry(frame, show="*")
e_p2_secret = tk.Entry(frame, show="*")

e_p1_secret.grid(row=0, column=1)
e_p2_secret.grid(row=1, column=1)

tk.Label(frame, text="Player-1 Guess").grid(row=2, column=0)
tk.Label(frame, text="Player-2 Guess").grid(row=3, column=0)

e_p1_guess = tk.Entry(frame)
e_p2_guess = tk.Entry(frame)

e_p1_guess.grid(row=2, column=1)
e_p2_guess.grid(row=3, column=1)

tk.Button(root, text="Check Guess",
          command=submit_guess,
          bg="green", fg="white",
          font=("Arial", 12)).pack(pady=15)

result = tk.StringVar()
tk.Label(root, textvariable=result,
         font=("Arial", 11),
         justify="left").pack(pady=10)

root.mainloop()

# cp1=input("Enter player-1 4-digit number:")
# cp2=input("Enter player-2 4-digit number:")

# def ply1():
#     p1=input("Enter player-1 number:")
#     sd1=0
#     sp1=0
#     for i in range(4):
#         if p1[i]==cp2[i]:
#             sp1+=1
#     for digit in p1:
#         if digit in cp2:
#             sd1+=1
#     print("Total common digits:", sd1)
#     print("Matching positions:", sp1)
#     if sp1==4:
#         print("YAY! You Won")
#         return True
#     return False