class Solution:
    def clumsy(self, n: int) -> int:
        total,num,op=0,n,0
        flag=True
        n-=1

        while n>0:
            if op==0:
                num*=n
            elif op==1:
                num//=n
            elif op==2:
                if flag:
                    total+=num
                    flag=False
                else:
                    total-=num
                total+=n
                num=0
            elif op==3:
                num=n

            op=(op+1)%4
            n-=1

        if flag:
            total+=num
        else:
            total-=num

        return total