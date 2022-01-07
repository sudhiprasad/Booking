import PySimpleGUI as psg

psg.theme('light blue')

def payment_window():
    psg.theme('light blue')
    layout_p = [
        [psg.Text('Payment page',size=(20, 1),justification='left')],
        [psg.Text('Amount to be payed =Rs.'+price,size=(40, 1),justification='left',key='amount')],
        [psg.Button('Pay',key='pay'),psg.Cancel('Exit', key='pexit')]
    ]

    window = psg.Window("Payment",layout_p,size=(300,200),auto_close=False,)

    events,values = window.read()

    while True:
        
        if events == psg.WIN_CLOSED:
            break
        
        elif events == "pexit":
            break

        elif events == "pay":
            psg.popup("Your booking was successfull !",
                        '\nYou will Travel from :\n'+ value['board']+' to '+value['dest']+'\n\n Seats booked = ' +strx[0:len(strx)], button_type='POPUP_BUTTONS_OK',
                        button_color='orange', background_color='light blue', text_color='dark blue')
            break


    window.close()


layout1=[[psg.Text('Departure City',size=(20, 1), font='Lucida',justification='left')],
        [psg.Combo(['Bangalore', 'Chennai','Mumbai', 'Kolkata'],size=(40,1),key='board')],
        [psg.Text('Arrival City',size=(30, 1),font='Lucida',justification='left')],
        [psg.Combo(['Delhi'],size=(40,1), key='dest',default_value='Delhi')],
        [psg.Text('Choose the number of seats: ',size=(30, 1), font='Lucida',justification='left')],
        [
            [psg.Radio("1","RADIO1",key='1', default=True,circle_color='orange'),
            psg.Radio("2","RADIO1",key='2',circle_color='orange'),
            psg.Radio("3","RADIO1",key='3',circle_color='orange'),
            psg.Radio("4","RADIO1",key='4',circle_color='orange')
            ]
        ],
        [psg.Button('Next',key='next',mouseover_colors=('orange', 'grey')),psg.Cancel('Exit', key='exit')]]


window =psg.Window('Booking Project',layout1,size=(400,300))

event,value=window.read()

strx=""

for val in value:
    if window.FindElement(val).get() == True:
        strx = strx+ " "+val

departure = value['board']
tic_price = 0
seats=int(strx[0:len(strx)])

if departure == 'Bangalore':

    tic_price = 2000*seats

elif departure == 'Chennai':

    tic_price = 3000*seats

elif departure == 'Mumbai':

    tic_price = 2500*seats

elif departure == 'Kolkata':

    tic_price = 2800*seats    

price = str(tic_price)

while True:

    if event == psg.WIN_CLOSED:

        break
    
    elif event == "exit":

        break

    elif event == "next":
        
        payment_window()

        break
    
    window.close()