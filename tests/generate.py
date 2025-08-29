#!/usr/bin/env python3
import os, random; random.seed(49)
def w(name, r, c, A):
    os.makedirs("tests", exist_ok=True)
    open(f"tests/input_{name}.txt","w").write(f"{r} {c}\\n"+" ".join(map(str,A))+"\\n")
    avg=sum(A)/(r*c)
    out=[0 if x<avg else x for x in A]
    with open(f"tests/output_{name}.txt","w") as f:
        for i in range(r):
            f.write(" ".join(map(str,out[i*c:(i+1)*c]))+"\\n")
def main():
    w("min",1,1,[5])
    r,c=2000,2000; A=[(i*i)%101 for i in range(r*c)]; w("max",r,c,A)
    r,c=17,19; import random
    A=[random.randint(0,100) for _ in range(r*c)]; w("rnd", r, c, A)
if __name__=="__main__": main()
