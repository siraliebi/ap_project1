import pandas as pd
from anbar import items
import random

anbardari = pd.read_csv('C:/Users/ASUS/Downloads/my_file.csv')

class Inventory:
    def update_admin_manual(self):
        
        while True:
            javab=input('kala or mojodi')
            if javab=='mojodi':
                javab1=(input('csv or manual'))
                if javab1=='manual':
                    stock_id = int(input('Enter stock ID: '))
                    new_count = int(input('Enter new stock count: '))

                    anbardari.loc[anbardari['id'] == stock_id, 'stock'] = new_count
                    t=input('do you wanna continue')
                    if t=='yes':
                            continue
                    else:
                        anbardari.to_csv('my_file.csv',index=False)
                        break
                if javab1=='csv':
                    while True:
                        file=input()
                        file=pd.read_csv(file)
                        anbardari.set_index('id', inplace=True)
                        anbardari.update(file.set_index('id'))
                        anbardari.reset_index()
                        t=input('do you wanna continue')
                        if t=='yes':
                            continue
                        else:
                            anbardari.to_csv('my_file.csv',index=False)
                            break
                    
            elif javab=='kala':
                kala_id=input('enter the id you wanna add')
                kala_name=input('enter the name ')
                kala_price=input('enter the unit price')
                kala_color=input('enter color')
                kala_stock=input('enter ths stock')
                kala_w=input('enter w')
                anbardari.loc[len(anbardari.index)]=[kala_id,kala_name,kala_price,kala_stock,kala_color,kala_w]
                t=input('do you wanna continue')
                if t=='yes':
                    continue
                
                else:
                    anbardari.to_csv('my_file.csv',index=False)
                    break
                
                
       

t=Inventory()     
t.update_admin_manual()