

#1 Initialize an empty dictionary variable for the instructors
instructor = {}


#POD Leaders:
jacore_leader = {}
andrew_leader = {}
gabriel_leader = {}
richard_leader = {}
aris_leader = {}

#4 Create an empty dictionary for the other 3 PODs; Aris, Gabriel and Richard

#5 Add the names and telephone numbers of each member POD

jacore_members = {}
jacore_members['Jacore Baptiste'] = '(845) 200-6250'
jacore_members['Moussa Ndiaye'] = '(123) 456-7890'
jacore_members['Morris Jones'] = '(925) 286-5922'
jacore_members['Prince Fields'] = '(510) 472-0804'
jacore_members['Akari Johnson'] = '(510) 500-2206'
jacore_leader["Jacores's POD Group:"] = jacore_members
instructor["Baba:"] = jacore_leader

andrew_members = {}
andrew_members['Andrew Lubega'] = '(925) 727-4611'
andrew_members['Mallick Abdullah'] = '(510) 409-8755' 
andrew_members['Ronin Youngjones'] = '(415) 910-3415'
andrew_members['Glenn Ivory'] = '(510) 328-8290'
andrew_leader["Andrew's POD Group:"] = andrew_members
instructor["David"] = andrew_leader

gabriel_members = {}
gabriel_members['Gabriel Reader'] = '(510) 326-5834'
gabriel_members['David Brickley'] = '(510) 631-6288'
gabriel_members['Emmanuel Torbor'] = '(510) 934-4133'
gabriel_members['Myles Wilkerson'] = '(510) 589-0579'
gabriel_leader["Gabriel's POD Group:"] = gabriel_members
instructor['Paris:'] = gabriel_leader

richard_members = {}
richard_members['Rihcard Kamau'] = '(510) 228-5623'
richard_members['Matthew Dudley'] = '(510) 816-2411'
richard_members['Kymari Rhodes'] = '(510) 575-1982'
richard_members['Josiah Johnson'] = '(510) 860-5112'
richard_leader["Richard's POD Group:"] = richard_members
instructor['Akeem:'] = richard_leader

aris_members = {}
aris_members['Aris Carter'] = '(510) 229-6359'
aris_members['Milan Kral'] = '(510) 816-3232'
aris_members['Maurice Richardson'] = '(510) 424-7789'
aris_members['Zyion Williams'] = '(510) 480-5785'
aris_members['Hyab Isayas'] = '(510) 612-3737'
aris_leader["Aris's POD Group:"] = aris_members
instructor['Hodari:'] = aris_leader


#8 Open the pod_file to read data


#9 Print all the Pod leaders and POD membership


for instructor, pod_leader in instructor.items():
  print(instructor)
  for pod_leader, pod_member in pod_leader.items():
    print(pod_leader)
    for pod_member, numbers in pod_member.items():
      print(pod_member, '-',numbers)
    print('\n')





