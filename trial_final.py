# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:04:04 2021

@author: chaoyan
"""
import datetime

def Grey(num):  #order_int[0]
    return 4.95*num

def Green(num):  #order_int[1]
    return 3.95*num

def Yellow(num):  #order_int[2]
    return 2.95*num

def Red(num):  #order_int[3]
    return 1.95*num

def Blue(num): #order_int[4]
    return 0.95*num

def Soup(num): #order_int[5]
    return 2.5*num
    
def check_weekday():
    
    weekday = [0,1,2,3,4]

#     datetime.datetime.today()
    tmp = datetime.datetime.today().weekday()
    if tmp in weekday:
        return True
    return False
#    return True

def check_time():   # return True if within the 11-17 range, return False if not

    now = datetime.datetime.now()

    start = "11:00:00"
    end = "17:00:00"
#     start = datetime.time(11, 0, 0)
#     end = datetime.time(17, 0, 0)
    current_time = now.strftime("%H:%M:%S")
#     current_time = "18:00:00"    
    if current_time >= start and current_time < end:
        return True
    return False
#    return True

def User1(num):
    result = Grey(num[0]) + Green(num[1]) +  Yellow(num[2]) + Red(num[3]) + Blue(num[4]) + Soup(num[5])
    return ("%.2f" % result)
    
def User2(num): #soup menu + more  order_int[5] = 1
    
    if sum(num[:5]) < 4: #less than a menu
        return User1(num)
    
    elif sum(num[:5]) == 4: #a menu 
        print('It is a menu 2!')
        return 8.5
    else:   # more than a menu
        tmp_count = 0
        for i in range(5):
            if tmp_count < 4:
                tmp_count += num[i]
            else:                
                ii = i
                print(ii)
                break
        num[ii-1] = tmp_count - 4
        for j in range(ii-1):
            num[j] = 0

        num[-1]=0
        print('It includes a menu 2!')
        result =  float(User1(num)) + 8.5
        
        return result
                       
    
def User3(num): # no soup menu 


    if  (num[3] == 0 and num[4] == 0): # not eligible for a menu
        return User1(num)
    else:
        
        if sum(num[:5]) == 5:
            print('It is a menu 3!')
            return 8.5
            
        elif sum(num[:5]) < 5:
            return User1(num)
        else:
            
    
            tmp_count = 0
            for i in range(6):
                if tmp_count < 5:
                    tmp_count += num[i]
                else:                
                    ii = i
                    print(ii)
                    break
            num[ii-1] = tmp_count - 5
            for j in range(ii-1):
                num[j] = 0
    
            num[-1]=0
            print('It includes a menu 3!')
            result =  float(User1(num)) + 8.5
            return result
        
        

def start_app(order_str):
#    order_str = list(tmp) #seperate raw input  

    order_int = [] # convert str to int
    for i in order_str:
        order_int.append(int(i))
    return order_int

def check_input(tmp):
    Tmp = tmp.split()
    soup_range = ['0','1']
    if len(Tmp) != 6:  # check if six input
        return False
    else:
        for i in Tmp: # check if input is number
            if i.isnumeric() == False:
                return False 
            if Tmp[-1] not in soup_range:
                return False
        return True

if __name__ == "__main__":

#    tmp = '000000'

    status = True
    while status:
        tmp = input("Please input the number of dishes you would like to order: ") 
        if tmp == 'exit':
            break
        elif check_input(tmp) == False:
            print('Wrong order!Please try again!')
            print('Type "exit" to exit!') 
            continue
        elif check_input(tmp):
            
            order_str = tmp.split()
            print('You ordered ' + order_str[0] +' Grey plate(s), ' + order_str[1] +' Green plate(s), '
                  + order_str[2] +' Yellow plate(s), '+ order_str[3] +' Red plate(s), '
                  + order_str[4] +' Blue plate(s), and '+ order_str[5] +' Soup!' )
              
            order_int = start_app(order_str)
        
            if check_weekday() and check_time():
                if order_int[-1] == 1:
                    print('The cost is: ' + str(User2(order_int)) + ' Euros')
                elif order_int[-1] == 0:
                    print('The cost is: ' + str(User3(order_int)) + ' Euros')
                else: 
                    print('The cost is: ' + str(User1(order_int)) + ' Euros')
    #            break
        
            else:
                print('The cost is: ' + str(User1(order_int)) + ' Euros')
    #            break
            print('Type "exit" to exit!')  

    
    

    


    