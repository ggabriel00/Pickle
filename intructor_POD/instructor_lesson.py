import pickle

#1 Initialize an empty dictionary variable, name it all_pod_members

instructor_pod = {}

#2 Initialize a file variable to write data to, name it pod_file, that will
# open a file named hgp_pods that you will write data to the file. 
pod_file = open('instructor.pkl', 'wb')

#3  Initialize empty dictionary variables, name it as such;

#Instructors:
baba = {}
hodari = {}
david = {}
akeem = {}
paris = {}

#POD Leaders:
jacore_members = {}
andrew_members = {}
gabriel_members = {}
aris_members = {}
richard_members = {}


#4 Create an empty dictionary for the other 3 PODs; Aris, Gabriel and Richard

#5 Add the names and telephone numbers of each member POD

jacore_members['Jacore Baptiste'] = '(845) 200-6250'
jacore_members['Moussa Ndiaye'] = '(123) 456-7890'
jacore_members['Morris Jones'] = '(925) 286-5922'
jacore_members['Prince Fields'] = '(510) 472-0804'
jacore_members['Akari Johnson'] = '(510) 500-2206'
baba['Baba'] = jacore_members
print(baba,'\n')
"""

andrew_members['Andrew Lubega'] = '(925) 727-4611'
andrew_members['Mallick Abdullah'] = '(510) 409-8755' 
andrew_members['Ronin Youngjones'] = '(415) 910-3415'
andrew_members['Glenn Ivory'] = '(510) 328-8290'

gabriel_members['Gabriel Reader'] = '(510) 326-5834'
gabriel_members['David Brickley'] = '(510) 631-6288'
gabriel_members['Emmanuel Torbor'] = '(510) 934-4133'
gabriel_members['Myles Wilkerson'] = '(510) 589-0579'

richard_members['Rihcard Kamau'] = '(510) 228-5623'
richard_members['Matthew Dudley'] = '(510) 816-2411'
richard_members['Kymari Rhodes'] = '(510) 575-1982'
richard_members['Josiah Johnson'] = '(510) 860-5112'

aris_members['Aris Carter'] = '(510) 229-6359'
aris_members['Milan Kral'] = '(510) 816-3232'
aris_members['Maurice Richardson'] = '(510) 424-7789'
aris_members['Zyion Williams'] = '(510) 480-5785'
aris_members['Hyab Isayas'] = '(510) 612-3737'
 
#6 Add all the PODS to the all_pod_members dictionary


#7 Dump all the
pickle.dump(Paris_members,pod_file)
pickle.dump(Akeem_members,pod_file)
pickle.dump(David_members,pod_file)
pickle.dump(Hodari_members,pod_file)
pickle.dump(Baba_members,pod_file)


pickle.dump(jacore_members,pod_file)
pickle.dump(andrew_members,pod_file)
pickle.dump(gabriel_members,pod_file)
pickle.dump(richard_members,pod_file)


#8 Open the pod_file to read data
pod_file = open('instructor.pkl', 'rb')

#9 Print all the Pod leaders and POD membership
for key,value in instructor_pod.items():
  print('This POD Leader is',key)
  for key2, value2 in value.items():
    print(key2,value2)
  print('\n')
"""

pod_file.close()


