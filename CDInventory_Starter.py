#------------------------------------------#
#--------------------------------------#
# Title: CDInventory
# Desc: Script will ask for user input and write to a .txt file.
# Program will display CDInventory and asj user to add to current Inventory
# Saduq Rahman, 2021 Feburay 13, created file
#---------------------------------------#


 

# Declare variabls

strFileName = 'CDInventory.txt'
strChoice = '' # User input
dicRow1 = {'id':1, 'Artist':'Kendrick Lamar', 'Album':'DAMN'}
dicRow2 = {'id':2, 'Artist':'Outkast', 'Album':'ATliens'}
dicRow3 = {'id':3, 'Artist':'Jay-z', 'Album':'Reasonable Doubt'}
lstTble = []
lstTble.append(dicRow1)
lstTble.append(dicRow2)
lstTble.append(dicRow3)
dicRow = {}



# Get user Input

print('The Magic CD Inventory\n')
while True:
# 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

 

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    elif strChoice == 'l':
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            print(lstRow)
            objFile.close

# =============================================================================

#         objFile = open(strFileName, 'r')

#         for row in lstTble:

#             strRow = ''

#             for item in row.values():

#                 strRow += str(item) + ','

#             strRow = strRow[:-1] + '\n'

#             objFile.write(strRow)

#         objFile.close()

# =============================================================================

   

    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
       strID = int(input('Enter an ID:'))  
       strName = input('Enter the Artist Name:')
       strAlbum = input('Enter the Artist Name:')
       intID = int(strID)
       dicRow = {'id': intID, 'Artist': strName, 'Album': strAlbum}
       lstTble.append(dicRow)
       print()

    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTble:
            print(row, sep = ',')

         
    elif strChoice == 'd':
        foundit = False
        del_id = int(input('Enter ID numner to delete item in Dictionary:').strip())
        for i in range(len(lstTble)):
            if lstTble[i]['id'] == del_id:
                del lstTble[i]
                foundit = True
                break
        if foundit: 
                    print("Item has been deleted")
                    print()
                    print('Here is the current inventory list:') 
                    print('ID, CD Title, Artist')
        for row in lstTble:
            print(row, sep = ',')
            
        else:
            print('\nPlease enter an ID within the list' , 'Thank You:')
            print()
        
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTble:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()

    else:
        print('Please choose either l, a, i, d, s or x!')
        
end = input('Thank you for trying out the program press enter to exit the program:')