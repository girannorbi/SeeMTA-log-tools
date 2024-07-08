import os
import re
import core
from  ticketcalculator import calc_all_tickets, get_tickets, get_last_ticket
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfile("r").name


chosen_issuer = input("Kinek a csekkjeit szeretnéd mérni?\n")
os.system("cls")

while True:
    log = core.read_log_file(file_path)
    price_total, ticket_ammount, price_average = calc_all_tickets(get_tickets(log), chosen_issuer)
    last_issued, last_price, last_reason = get_last_ticket(get_tickets(log), chosen_issuer)
    print(f"Kiválasztott név: {chosen_issuer}")
    if price_total != 0 and ticket_ammount != 0 and chosen_issuer != 0:
        print(f"\n"
              f"Összesen: {price_total}$\n"
              f"Csekkek darabszáma: {ticket_ammount}db\n"
              f"Átlag büntetés: {price_average}"
              f"\n\n")
        if last_issued:
            print(f"Legutolsó büntetés:\n"
                  f"Büntetett neve: {last_issued}\n"
                  f"Büntetés összege: {last_price}$\n"
                  f"Büntetés oka: {last_reason}")
    time.sleep(15)
    os.system('cls')