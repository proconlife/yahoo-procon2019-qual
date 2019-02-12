cnt = {"1":0,"2":0,"3":0,"4":0}
for i in range(3) :
    (j,k)=input().split()
    cnt[j]+=1
    cnt[k]+=1

if cnt["1"] == 3 or cnt["2"] == 3 or cnt["3"] == 3 or cnt["4"] == 3 :
    print("NO")
else :
    print("YES")
