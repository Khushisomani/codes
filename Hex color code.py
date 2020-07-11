# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for i in range(int(input())):
    s=input()
    x=s.split()
    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
        for i in x:
            print(i)
