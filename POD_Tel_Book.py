import pickle 

# 1. Leader Numbers
leader = {}
leader['Jacore Baptiste'] = '(845) 200-6250'
leader['Aris Carter'] = '(510) 229-6359'
leader['Andrew Lubega'] = '(925) 727-4611'
leader['Gabriel Reader'] = '(510) 326-5834'


# 2. create/open pod_nbrs.pkl
pod_file = open('pod_nbrs.pkl', 'wb')

# 3. Write POD Leader number to a file
pickle.dump(leader,pod_file)

# 4. Member Numbers
member = {}
member['Akari Johnson'] = '(510) 500-2206'
member['Akari Johnson'] = '(510) 500-2206'
member['Andrew Lubega'] = '(925) 727-4611'
member['Aris Carter'] = '(510) 229-6359'
member['David Brickley'] = '(510) 631-6288'
member['Emmanuel Torbor'] = '(510) 934-4133'
member['Gabriel Reader'] = '(510) 326-5834'
member['Glenn Ivory'] = '(510) 328-8290)'
member['Hyab Isayas'] = '(510) 612-3737'
member['Jacore Baptiste'] = '(845) 200-6250'
member['Josiah Johnson'] = '(510) 860-5112'
member['Kymari Rhodes'] = '(510) 575-1982'
member['Mallick Abdulla'] = '(510) 409-8755'
member['Matthew Dudley'] = '(510) 816-2411'
member['Maurice Richardson'] = '(510) 424-7789'
member['Milan Kral'] = '(510) 816-3232'
member['Miles Tademy'] = '(510) 604-3128'
member['Morris Jones'] = '(925) 286-5922'
member['Mousa Ndiaye'] = '(415) 717-8414'
member['Myles Wilkerson'] = '5105007266'
member['Nate Barber'] = '(510) 927-7705'
member['Prince Fields'] = '(510) 472-0804'
member['Richard Kamau'] = '(510) 228-5623'
member['Ronin Jones'] = '(415) 910-3415'
member['Zyion Williams'] = '(510) 480-5785' 


# 5. Write Member numbers to pod_file
pickle.dump(member,pod_file)

# 6. Close pod_file
pod_file.close()

# 7. Open pod.file
pod_file = open('pod_nbrs.pkl', 'rb')


# 8. Leader numbers
print('Leaders: ')
for key,value in leader.items():
    print(key, value)
    
print('\n')

# 9. Print POD members
print('Members:')
for key,value in member.items():
    print(key, value)
    
print('\n')

# 10. Close pod_file 
