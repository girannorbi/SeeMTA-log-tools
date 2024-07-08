import os
import re
import time

import core


class Ticket:
    def __init__(self, price, issuer, reason, date, log, issued):
        self.price = price
        self.issuer = issuer
        self.reason = reason
        self.date = date
        self.log = log
        self.issued = issued


def get_tickets(logfile):
    """
    gets all issued tickets found in the logfile
    Paramters:
        log: string
    Returns:
        array of all the found tickets
    """
    tickets = []
    for i in range(len(logfile)):
        if logfile[i].__contains__("[SeeMTA - Ticket]:"):
            price = int(re.search("Bírság: (.*) Indok:", logfile[i]).group(1).replace(" ", "").replace("$", ""))
            issuer = re.search(r"SeeMTA - Ticket]: (.*) megbüntette", logfile[i]).group(1)
            issued = re.search(r"megbüntette (.*) játékost", logfile[i]).group(1)
            reason = re.search("Indok: (.*)", logfile[i]).group(1)
            date = re.search(r"\[(.*)\] \[Output\]", logfile[i]).group(1)
            log = logfile[i]
            tickets.append(Ticket(price, issuer, reason, date, log, issued))
    return tickets

def calc_all_tickets(tickets, chosen_issuer):
    price_total = 0
    ticket_amount = 0
    price_average = 0
    if len(tickets) != 0:
        for i in tickets:
            if i.issuer == chosen_issuer:
                price_total += i.price
                ticket_amount += 1
        price_average = price_total/ticket_amount
    return price_total, ticket_amount, price_average

def get_last_ticket(tickets, chosen_issuer):
    if len(tickets) == 0:
        return None
    last_ticket = None
    for current_ticket in tickets:
        if(current_ticket.issuer == chosen_issuer):
            last_ticket = current_ticket
    if isinstance(last_ticket, Ticket):
        return last_ticket.issued, last_ticket.price, last_ticket.reason 
    else:
        return None
