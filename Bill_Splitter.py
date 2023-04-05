import random


freands_count = int(input("Enter the number of friends joining (including you):"))
freands_list = {}
print('') 
if freands_count <= 0:
    try:
        print('') 
        print("No one is joining for the party") 
    except Exception:
        print('') 
        print("No one is joining for the party")    
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(freands_count):
        freand_name = input()
        freands_list[str(freand_name)] = 0
        if len(freands_list) == freands_count:
            print('') 
            bill_size = int(input("Enter the total bill value:"))
            personal_bill = bill_size / freands_count            
            for freand_name in freands_list:
                freands_list[str(freand_name)] = round(personal_bill, 2)
            print('')
            freand_answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
            if freand_answer == "Yes":
                print('')
                random_freand = random.choice(list(freands_list.keys()))
                print(random_freand)
                for freand_name in freands_list:                    
                    personal_bill = bill_size / (freands_count - 1) 
                    freands_list[str(freand_name)] = round(personal_bill, 2)
                    freands_list[str(random_freand)] = 0                
            else:
                print('')
                print("No one is going to be lucky")
    print('') 
    print(freands_list)

    
    
    

