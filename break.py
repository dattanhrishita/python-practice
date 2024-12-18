#break statement
for i in range(1,15):
    if(i==15):
        break
        print("hello",i)
print("loop exited")

#use of continue
for i in range(1,21):
    if(i==10):
        print("skipped")
        continue
print(i)
