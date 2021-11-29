y = 2021
d = 365

J1 = 'Friday'

J  = 31
F  = 28
M  = 31
A  = 30
Ma = 31
J  = 30
Ju = 31
Au = 31
S  = 30
O  = 31
N  = 30
D  = 31

month_list = [J , F , M , A , Ma , J , Ju , Au , S , O , N , D]

l = ['Sunday' , 'Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday' , 'Saturday']


a = int(input("Enter the Month : "))

for i in range(a) :
    t = 1 + i
    w = month_list[i]
print("Month days : " , w , "days")

f = int(input("Enter the date : "))

g = w - f

t = w - g

print(t)



# for i in range(w + 1) :
#     g = w - i
#     t = w - g
# print(t)













        