import pickle 

# 1. Leader Numbers
leader = {}
leader['Jacore Baptiste'] = '(845) 200-6250'
leader['Aris Carter'] = '(510) 229-6359'
leader['Andrew Lubega'] = '(925) 727-4611'
leader['Gabriel Reader'] = '(510) 326-5834'
leader['Richard Kamau'] = '(510) 228-5623'

# 2. create/open pod_nbrs.pkl
pod_file = open('pod_nbrs.pkl', 'wb')

# 3. Write POD Leader number to a file
pickle.dump(leader,pod_file)

# 4. Member Numbers
member = {}
member['David Brickley'] = '(510) 631-6288'
member['Emmanuel Torbor'] = '(510) 934-4133'
member['Myles Wilkerson'] = '5105007266'

# 5. Write Member numbers to pod_file
pickle.dump(member,pod_file)

# 6. Close pod_file
pod_file.close()

# 7. Open pod.file
pod_file = open('pod_nbrs.pkl', 'rb')


# 8. Leader numbers
print('POD Leaders: ')
for key,value in leader.items():
    print(key, value)
    
print('\n')

# 9. Print POD members
print('My POD Members:')
for key,value in member.items():
    print(key, value)
    
print('\n')

# 10. Close pod_file 
