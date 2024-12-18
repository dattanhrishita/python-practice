#wap to generate even number take range from user 

start=int(input("Give the range "))
end=int(input("Eneter the end range"))
for i in range(start,end+1):
    if i%2==0:
        print(i)
