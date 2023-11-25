class Star_cinema:
    hall_list =[]

    def entry_Hall(self,obj):
        self.hall_list.append(obj)


      
class Hall(Star_cinema):
    show_list = []
    seats ={}
        
    def __init__(self,_rows,_cols,hall_no) -> None:
       
        self._rows = _rows 
        self._cols = _cols 
        self.hall_no = hall_no
        self.entry_Hall(self)
        super().__init__()
    def entry_show(self,id,movie_name,time):
        self.show_list.append((id,movie_name,time))
        seat=[] 
        for i in range(self._rows):
            row=[]
            for j in range(self._cols):
               ele = 0
               row.append(ele)
            seat.append(row)
        self.seats[id] = seat
                  
    
    def book_seat(self):
        ID = input('SHOW ID: ')
        x = 0
        tickets = 0
        for id,_ ,_ in self.show_list:
            if id == ID:
                x = 1
                n = int(input('Number of tickets?: ')) 
                seat = self.seats[id] 
                rows = len(seat)
                cols = len(seat[0])
                tickets = rows*cols
                if n <= tickets:  
                    while n!=0:
                       row = int(input('Enter seat row: '))
                       col = int(input('Enter seat column: '))
                       if(rows >= row and cols >= col):
                           if seat[row-1][col-1] != 1:
                               seat[row-1][col-1] = 1
                               print('\n')
                               print('\n')
                               print(f'You have booked {row,col} seat for {id} show. Thanks.')
                               print('\n')
                               print('\n')
                           else:
                               print('\n')
                               print('\n')
                               print(f'SORRY. No ticked available for ({row,col}) seat. It is already booked')
                               print('\n')
                               print('\n')
                       else: 
                           print('\n')
                           print('\n')
                           print(f'Enter valid tickets number please. To see available tickets ENTER option 2. Thanks.')
                           print('\n')
                           print('\n')
                           n+=1
                            
                       n -= 1
                else:
                    print('\n') 
                    print(f'There are only {tickets} seat available. To see the seat details ENTER OPTION 2. Thanks.')
                    print('\n') 
                    print('\n') 
                        
                    
        if x == 0:
            print('\n')
            print('\n')
            print('Sorry, You have given a wrong ID')
            print('\n')
            print('\n')
                   

            





            
    def view_show_list(self):
        print(f'.....................')
        for id,name ,time in self.show_list:
           
            print(f'MOVIE NAME: {name}({id}) SHOW ID:{id} TIME: {time}')
        print(f'.....................')
        print('\n')

    def view_available_seats(self):
        ID = input('SHOW ID : ')
        x = 0
        print('\n')
        print('\n')
        print(f'UPDATED TICKET SEATS of HALL {self.hall_no} ')
        print('\n')
        for id,_ ,_ in self.show_list:
            if id == ID:
                for ele in self.seats[id]:
                    x = 1
                    print(ele) 
        print('\n') 
        print('\n')
        if x == 0:
            print('Sorry, You have given a wrong ID')  
            print('\n')
            print('\n')  
          
    
my_ticket = Hall(10,10,2)
my_ticket.entry_show('111','The money masters-The rise of Bankers','07/12/2016  10:24 AM')
Her_ticket =Hall(4,4,4) 
Her_ticket.entry_show('112','Money as debt','11/10/2012  7:30 PM') 
sons_ticket = Hall(7,7,2)
sons_ticket.entry_show('113','Animal','11/11/2023  9:30 PM')


while True:
    print('1. VIEW ALL SHOW TODAY:')
    print('2. VIEW AVAILABLE SEATS:')
    print('3. BOOK TICKET:')
    print('4. EXIT:')
    op = int(input('ENTER OPTION: '))
    if op == 1:
        my_ticket.view_show_list()
    elif op == 2:
       my_ticket.view_available_seats()
    elif op == 3:
        my_ticket.book_seat()
    else:
        break







