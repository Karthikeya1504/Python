n=20
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("Zing Bing ")
    elif i%3==0:
        print("Zing")
    elif i%5==0:
        print("Bing")    
    else:
        print(i)
    
