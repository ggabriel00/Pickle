import pickle

# 1. Staff Numbers
staff = {}
staff['Brandon'] = '(510) 268-2584'
staff['Hodari'] = '1(510) 415-2594'
staff['Akeem'] = '(510) 684-0505'
staff['Sean'] = '(510) 910-7233'
staff['Baba Lemon'] = '(510) 205-0980'

# 2. create/open hgp_file
hgp_file = open('hgp_nbr2.pkl', 'wb') 

# 3. Write Staff numbers to a file
pickle.dump(staff,hgp_file)

# 4. Genius Numbers
genius = {}
genius['Paris'] = '(510) 485-2564'
genius['Galanafai'] = '(510) 635-8807'
genius['Lemuel'] = '(510) 809-5503'
genius['Kelinde'] = '(510) 227-5312' 

# 5. write Genius numbers to telephone file
pickle.dump(genius,hgp_file) 

# 6. close hgp_file
hgp_file.close() 

# 7. Open hgp_file
hgp_file = open('hgp_nbr2.pkl', 'rb') 

# 8. Print Staff numbers
print('Staff: ')
for key,value in staff.items():
        print(key, value)
                
print('\n')
                
# 9. Print Geniuses
print('Geniuses: ')
for key,value in genius.items():
        print(key, value) 
