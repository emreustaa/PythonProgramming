student_details= [
  {'id' : 1, 'subject' : {'math': (70, 82), 'cs': (75, 87)}},
  {'id' : 2, 'subject' : {'math': (73, 74), 'cs': (78, 79)}},
  {'id' : 3, 'subject' : {'math': (75, 86), 'cs': (80, 91)}}
]

averages = {s['id']: {subject: sum(points)/2 for subject, points in s['subject'].items()} for s in student_details}
print(averages)


durum = False

print(durum)

set1 = set("Emre Usta")
print(set1)

liste =[2,5,1,0,6,8,7,9,4]
print("Sıralanmadı",liste)
liste.sort()
print("Sıralandı" , liste)
print(liste)

print("")
takimlar = ['gs','fb','bjk','ts']
y_takimlar = sorted(takimlar)
print(y_takimlar)
print(takimlar)
takimlar.sort()
print(takimlar)
yeni = sorted(takimlar,reverse=True)
print(yeni)

l1 = ["eat", "sleep", "repeat"]
s1 = "geek"



print(abs(-5))

print(bin(7))
list(filter(lambda x:x%2==0,[1,2,0,False]))

a,b=2,3
print("a={0} and b={1}".format(a,b))

print(list({1,3,2,2}))