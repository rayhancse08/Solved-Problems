def dfs(j,visited,input_zombies,row_len):
    for k in range(row_len):
        if input_zombies[j][k] == '1' and visited[j][k] == False and visited[k][j] == False:
                 visited[j][k] = True
                 visited[k][j] = True
                 dfs(k,visited,input_zombies,row_len) 
        
    

def zombie_cluster(input_zombies):
    row_len=len(input_zombies)
    col_len=len(input_zombies[0])
    count=0
    if row_len==0 or col_len==0:
        return count
    
    visited=[[False for j in range(col_len)] for i in range(row_len)]
    
    
    for i in range(row_len):
        bol=False
        for j in range(row_len):
            
            if input_zombies[i][j]=='1' and visited[i][j]==False and visited[j][i]==False:
                
                visited[i][j]=True
                visited[j][i]=True
                
                dfs(j,visited,input_zombies,row_len)
                if bol==False:
                    count+=1
                    bol=True
    return count

zombie_number=int(input("number of zombie: " ))
zombie_list=[]
for i in range(zombie_number):
    zombie=input()
    zombie_list.insert(i,zombie)


print(zombie_cluster(zombie_list))
    
