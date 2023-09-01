from src.guest import Guest

class KaraokeBar:

    def __init__(self, name, till, entry_fee):

        self.name = name
        self.rooms = []
        self.till = till
        self.entry_fee = entry_fee





    def take_payment(self, guest):

        guest.pay(self.entry_fee)
        self.till += self.entry_fee

