def carre(x):
  y = x**2
  return y

def add_list(l, val):
 l.append(val)

def afficher_val(inf, sup):
    for i in range(inf, sup+1):
        print(i)


def bornes(deb, fin, pas):
    i = deb
    while i <= fin :
        print(i)
        i = i + pas
