

# OOPS IN PYTHON


class MobailePhone():
    made_in='India'



Apple=MobailePhone()
samsung=MobailePhone()

Apple.model='I Phone 12'
Apple.price=120000
Apple.made_in='India'

samsung.model='s23 ultra'
samsung.price=130000

print(Apple.__dict__,samsung.__dict__)



class student:
    pass


harry=student()
larry=student()


harry.name='Harry'
harry.std=12
harry.section=1
larry.std=9
larry.subjects=['eng','hindi']

print(harry.std,larry.subjects)

print(harry,larry)
