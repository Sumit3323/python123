Laptops={'HP':50000,'Lenovo':60000,'ASUS':45000,'Mackbook':120000}

inp=int(input('Enter The Price In Laptops :-'))


def fun(aa):
    # print(aa)
    if Laptops[aa]<=inp:
       return aa
ap=list(filter(fun,Laptops))
print(ap)
     