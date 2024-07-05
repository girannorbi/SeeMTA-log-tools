import re

import core


class Ticket:
    def __init__(self, price, issuer, reason, date, log):
        self.price = price
        self.issuer = issuer
        self.reason = reason
        self.date = date
        self.log = log


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
            price = re.search("Bírság: (.*) Indok:", logfile[i]).group(1)
            issuer = re.search(r"SeeMTA - Ticket]: (.*) megbüntette", logfile[i]).group(1)
            reason = re.search("Indok: (.*)", logfile[i]).group(1)
            date = re.search(r"\[(.*)\] \[Output\]", logfile[i]).group(1)
            log = logfile[i]
            tickets.append(Ticket(price, issuer, reason, date, log))
    return tickets


files = ["C:/SeeMTA/mta/logs/console-2024-07-05.log", "C:/SeeMTA/mta/logs/console-2024-07-04.log", "C:/SeeMTA/mta/logs/console-2024-07-03.log", "C:/SeeMTA/mta/logs/console-2024-07-01.log"]
log = core.read_log_file(files)
tickets = get_tickets(log)
for i in tickets:
    print("")
    print(i.issuer)
    print(i.reason)
    print(i.price)
print("\nÖsszesen:")
print(str(len(tickets)) + " darab")
