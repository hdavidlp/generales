from pprint import pprint as pp

""" Model for aircraft Flights """
class Flight:

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"No airline code in '{number}")
        
        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code '{number}")

        if not (number[2:].isdigit() and int (number[2:])<=9999):
            raise ValueError(f"Invalid route number '{number}")
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()
    
    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        row, letter  = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger
    
    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid sea row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return row, letter 

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)


    def relocate_passenger(self, from_seat, to_seat):
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in seat {from_seat}")
        
        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError (f"Seat {to_seat} already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def make_bording_cards(self, card_printer):
        for passenger, seat in sorted (self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())
    
    def _passenger_seats(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")




class Aircraft:
    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration


    """def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration
    
    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])"""

def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f"│ Name     : {passenger}"     \
             f"  Flight   : {flight_number}" \
             f"  Seat     : {seat}"          \
             f"  Aircraft : {aircraft}"      \
              "│ "
    banner = "+" + "-" * (len(output)-3) + "+"
    border = "│" + " " * (len(output)-3) + "│"
    lines  = [banner, border, output, banner]
    card = "\n".join(lines)
    print(card)
    print()


class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"
    
    def seating_plan(self):
        return range(1,23), "ABCDEF"

class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"
    
    def seating_plan(self):
        return range(1,56), "ABCDEGHJK"
            


def make_flights():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("1A", "David")
    f.allocate_seat("1B", "Hector")
    f.allocate_seat("1C", "Lopez")
    f.allocate_seat("1D", "Paez")

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat("2A", "Juan")
    g.allocate_seat("2B", "ito")
    g.allocate_seat("2C", "Gonzalez")
    g.allocate_seat("2D", "Gonzalez")



    return f, g



f, g = make_flights()
print (f.num_available_seats())
print (g.num_available_seats())

a = Boeing777(":G-EZBT")
print (a.num_seats())

print (f._aircraft.num_seats())



# pp(f._seating)
#
# f.relocate_passenger("1A","2A")
# f.make_bording_cards(console_card_printer)