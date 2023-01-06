class Bus:

    def init(self, Id, seats, from_des, to_des):
        self.Id = Id
        self.from_des = from_des
        self.to_des = to_des
        self.seats = seats
        self.booked_seats =[]
buses = [
  {'no.': 1, 'route': 'Rafah to Khanyounis', 'seats': ['<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>',
   '<Y>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<C>','<C>','<C>','<C>','<C>','<C>','<C>',
   '<C>','<C>','<C>','<C>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<E>','<E>','<E>','<E>',
   '<E>','<E>'], 'returned_seats': []},

  {'no.': 2, 'route': 'Rafah to Gaza', 'seats': ['<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>',
   '<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<C>','<C>','<C>','<C>','<C>','<C>','<C>','<C>',
   '<C>','<C>','<C>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<E>','<E>','<E>','<E>','<E>',
   '<E>'], 'returned_seats': []},

  {'no.': 3, 'route': 'Gaza to Eqypt', 'seats': ['<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>','<Y>',
   '<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<B>','<C>','<C>','<C>','<C>','<C>','<C>','<C>','<C>',
   '<C>','<C>','<C>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<D>','<E>','<E>','<E>','<E>','<E>',
   '<E>'], 'returned_seats': []}
]
def view_buses():
  print('Buses:')
  for x, bus in enumerate(buses):
    print(f'{x+1}. Bus no. {bus["no."]} ({bus["route"]})')

def view_seats(bus):
    available_seats = [seat for seat in bus['seats'] if seat not in bus['returned_seats']]
    print(f'Seats available for bus {bus["no."]} ({bus["route"]}): {available_seats}')

def return_seat(bus, seat):
  if seat in bus['seats'] and seat not in bus['returned_seats']:
    bus['returned_seats'].append(seat)
    print(f'Seat {seat} successfully returned for bus {bus["no."]} ({bus["route"]})')
  elif seat in bus['returned_seats']:
    print(f'Seat {seat} is already returned for bus {bus["no."]} ({bus["route"]})')
  else:
    print(f'Seat {seat} is not available for bus {bus["no."]} ({bus["route"]})')

def delete_returnation(bus, seat):
  if seat in bus['returned_seats']:
    bus['returned_seats'].remove(seat)
    print(f'Returnation for seat {seat} on bus {bus["no."]} ({bus["route"]}) successfully canceled')
  else:
    print(f'Seat {seat} is not reserved on bus {bus["no."]} ({bus["route"]})')

while True:
    print('Enter 1 to view available buses')
    print('Enter 2 to do a returnation')
    print('Enter 3 to delete a returnation')
    print('Enter 4 to logout from the program')
    choice = input('Enter your choice: ')
    if choice == '1':
        view_buses()
        print('this is the whole bus')
    elif choice == '2':
        bus_number = int(input('Enter the bus number: '))
        bus = next(bus for bus in buses if bus['no.'] == bus_number)
        view_seats(bus)
        seat = input('Enter the seat number: ')
        print()
        return_seat(bus, seat)
    elif choice =='3':
        bus_number = int(input('Enter the bus number: '))
        seat = input('Enter the seat number: ')
        bus = next(bus for bus in buses if bus['no.'] == bus_number)
        delete_returnation(bus, seat)
    elif choice == '4':
        break
    else:
        print('Invalid choice')