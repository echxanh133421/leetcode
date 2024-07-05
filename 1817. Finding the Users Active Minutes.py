class Solution:
    def findingUsersActiveMinutes(self, logs, k: int) :
        users=[]
        for i in range(len(logs)):
            if logs[i][0] not in users:
                users.append(logs[i][0])
        uam_users=[]
        count_uam_user=[]
        for user in users:
            uam_user=[]
            count=0
            for j in range(len(logs)):
                if logs[j][0]==user and logs[j][1] not in uam_user:
                    uam_user.append(logs[j][1])
                    count+=1
            count_uam_user.append(count)
            uam_users.append(uam_user)
        answer=[]
        for j in range(k):
            answer.append(count_uam_user.count(j+1))
        return answer

if __name__=="__main__":
    a=Solution()
    logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
    k = 5
    b=a.findingUsersActiveMinutes(logs,k)
    print(b)
    '''time limited'''