#Declaring Variables
d={}
l=[]
temp=[]
result=[]
#Taking input : N => Number of goodies"  M =>Number of employees
N=int(input("Number of goodies"))
M=int(input("Number of employees"))
M=M-1

#Reading Input Goodies
with open("sample_input.txt") as f:
    for i in range(N):
        line=f.readline().rstrip("\n")
        index=line.find(":")
        number=int(line[index+2:])
        d[line]=number
        l.append(number)
    # Applying Algorithm
    l.sort()   #sort the list of numbers
    diff=float("inf")
    ind=0
    for i in range(M,len(l)):
        if (l[i]-l[i-M])<diff:
            diff=l[i]-l[i-M]
            ind=i
    temp=l[ind-M:ind+1]
#Creating the result list
for k,v in d.items():
    if v in temp:
        result.append(k)
# Writing to outputfile
outfile=open("output.txt","w")
for i in result:
    outfile.write(i)
    outfile.write("\n")
outfile.close()
