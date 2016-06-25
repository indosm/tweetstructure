#-*- coding : utf-8 -*-
'''
2015410087 김지헌
version 0.8.0
2016/06/24
'''

import codecs
import rbtree
import adj
import friend

def find_num(T,num):
    """Arg : HashTable, usernumber
       finds if usernumber is exists on HashTable"""
    for u in T[int(num)%1000]:
        if num == u.number:
            return u
    return False

def read_data():
    """reads word.txt file, Insert usernumber,tw to hashTable
       and Insert tw to RBTree"""
    f = codecs.open("word.txt",'r','utf-8')
    while True:
        add = False
        number = f.readline()[:-1]
        date   = f.readline()[:-1]
        string = f.readline()[:-1]
        f.readline()
        if not number : break
        u = find_num(hashTable,number)
        if u:
            word = u.search_st(string)
            if not word:
                u.add_tw(string)
                add = True
            else :
                u.count_tw+=1
                word.count+=1
                
        else :
            user = adj.USER(number)
            user.add_tw(string)
            hashTable[int(number)%1000].append(user)
            u=user
            add = True
            #dfs = friend.DFSVertex(number)
            #vertices.append(dfs)
        tw = tweet.search(string)
        if tw!=tweet.nil:
            tw._count+=1
            if add:
                u.head.down=tw.user
                tw.user.up = u.head
                tw._user = u.head
        else:
            tweet.insert_key(string,u.head)
            
    f.close()

    """reads user.txt, Make usernumber to usernickname"""
    f = codecs.open("user.txt",'r','utf-8')
    while True:
        number = f.readline()[:-1]
        date   = f.readline()[:-1]
        nick   = f.readline()[:-1]
        f.readline()
        if not number : break
        u = find_num(hashTable,number)
        if u :
            u.nickname(nick)
        else :
            print("What????")
    f.close()

    """reads friend.txt, """
    f = codecs.open("friend.txt",'r','utf-8')
    #DFS = friend.DepthFirstSearch()
    #DFS.set_vertices(vertices)
    while True:
        friend1 = f.readline()[:-1]
        friend2 = f.readline()[:-1]
        f.readline()
        if not friend1 : break
        u = find_num(hashTable,friend2)
        if u :
            friend = u.search_fr(friend1)
            if not friend:
                u.add_fr(friend1)
            else :
                u.count_fr+=1
            
    f.close()

    
    global To_user
    global To_word
    global To_friend
    To_user=0
    To_word=0
    To_friend=0
    for x in hashTable:
        To_user += len(x)
        for y in x:
            To_word+=y.count_tw
            To_friend+=y.count_fr
    print("Total users : ",To_user)
    print("Total friendship records: ",To_friend)
    print("Total tweets: ",To_word,"\n")
def disp_stat():
    minfr=1E10
    maxfr=0
    mintw=1E10
    maxtw=0
    for x in hashTable:
        for y in x:
            minfr=min(minfr,y.count_fr)
            maxfr=max(maxfr,y.count_fr)
            mintw=min(mintw,y.count_tw)
            maxtw=max(maxtw,y.count_tw)
    print("Average number of friends: ",To_friend/To_user)
    print("Minimum number of friends: ",minfr)
    print("Maximum number of friends: ",maxfr,"\n")
    print("Average tweets per user: ",To_word/To_user)
    print("Minium tweets per user: ",mintw)
    print("Maximu tweets per user: ",maxtw,"\n")
def find_word(tree,list):
    if tree.right != tweet.nil:
        list=find_word(tree.right,list)
    for index in range(5):
        if tree.count > list[index][1]:
            list=list[0:index]+[[tree.string,tree.count]]+list[index:-1]
            break
    if tree.left != tweet.nil:
        list=find_word(tree.left,list)
    return list
def top5_word():
    top_list=[["",0]for x in range(5)]
    top_list=find_word(tweet.root,top_list)
    for i in range(5):
        print("Most Tweeted Word Top "+str(i)+": ",top_list[i][0],"\t, #"+str(top_list[i][1]))
def top5_user():
    top_list=[["",0]for x in range(5)]
    for x in hashTable:
        for y in x:
            for index in range(5):
                if y.count_tw > top_list[index][1]:
                    top_list=top_list[0:index]+[[y.nick,y.count_tw]]+top_list[index:-1]
                    break
    for i in range(5):
        print("Most Tweeted User Top "+str(i)+": ",top_list[i][0],"\t, #"+str(top_list[i][1]))
def find_usr():
    string = input("찾을 단어를 입력해주세요 : ")
    tw = tweet.search(string)
    if tw == tweet.nil:
        print("단어가 존재하지 않습니다..")
    else:
        x=tw.user
        num=0
        global memory_menu4
        memory_menu4=[]
        while x!=None:
            print(x.own.nick,end="\n"if x.down==None else",")
            memory_menu4.append(x.own)
            num+=1
            x=x.down
        print("총",num,"명이 단어를",tw.count,"번 사용했습니다.")
    return memory_menu4
def find_friend():
    num_fr=0
    for user in memory_menu4:
        print("friends of",user.nick,":",end="")
        x = user.friend
        num_fr +=user.count_fr
        while x != None:
            u = find_num(hashTable,x.string)
            print(u.nick,end="\n"if x.next == None else ",")
            x=x.next
    print("총",num_fr,"명의 친구가 검색되었습니다.")
def del_ment():
    string = input("삭제할 단어를 입력해주세요 : ")
    tw = tweet.search(string)
    if tw == tweet.nil:
        print("삭제할 단어가 존재하지 않습니다..")
    else:
        x = tw.user
        global memory_menu6
        memory_menu6=[]
        while x != None:
            x.own.count_tw=0
            memory_menu6.append(x.own)
            if x.next:
                x.next.prev = x.prev
            if x.prev:
                x.prev.next = x.next
            else :
                x.own.head = x.next
            x = x.down
        print("%s단어가 %d개 삭제되었습니다"%(tw.string,tw.count))
        tw._count=0
        #tweet.delete_node(tw)
        global To_word
        To_word-=tw.count
def del_usr():
    num_usr=0
    num_tw=0
    num_fr=0
    for user in memory_menu6:
        x = user.head
        while x != None:
            tw = tweet.search(x.string)
            if x.next:
                x.next.prev = x.prev
            if x.prev:
                x.prev.next = x.next
            if x.up:
                x.up.down = x.down
            else:
                tw._user = x.down
            if x.down:
                x.down.up = x.up
            num_tw+=x.count
            tw._count-=x.count
            #if tw.count==0:
            #    tweet.delete_node(tw)
            x=x.next
        num_usr+=1
        num_fr+=user.count_fr
        global hashTable
        for index in range(len(hashTable[int(user.number)%1000])):
            if hashTable[int(user.number)%1000][index].number == user.number:
                del hashTable[int(user.number)%1000][index]
                break
    global To_user
    global To_friend
    global To_word
    To_user -= num_usr
    To_friend-=num_fr
    To_word -= num_tw
    print("총",num_usr,"명의 유저,",num_fr,"명의 친구,",num_tw,"개의 트윗이 삭제되었습니다.")
def find_scc():
    print("지원되지 않는 기능입니다")
def find_short_path():
    user = input("찾고 싶은 User number를 입력해 주세요(닉네임 X)")
    u = find_num(hashTable,user)
    if u:
        list = [[]for x in range(5)]
        print("지원되지 않는 기능입니다")
    else:
        print("User가 존재하지 않습니다.")
if __name__ == "__main__":
    menuMap = {
        "0" :read_data,
        "1" :disp_stat,
        "2" :top5_word,
        "3" :top5_user,
        "4" :find_usr,
        "5" :find_friend,
        "6" :del_ment,
        "7" :del_usr,
        "8" :find_scc,
        "9" :find_short_path,
        "99":quit,
        }
    #user를 저장하기 위한 hashTable
    hashTable = []
    for x in range(0,1000):
        hashTable.append([])
    #word를 저장하기 위한 tweet
    tweet = rbtree.Tweet()
    #friend를 저장하기 위한 list
    vertices=[]
    #4번,6번 메뉴에서 나온 user를 저장하기 위한 memory buffer
    memory_menu4 = []
    memory_menu6 = []
    while True:
        print("-"*15+"*"*10+"-"*15)
        print("""0. Read data files
1. display statistics
2. Top 5 most tweeted words
3. Top 5 most tweeted users
4. Find users who tweeted a word (e.g., ’연세대’)
5. Find all people who are friends of the above users
6. Delete all mentions of a word
7. Delete all users who mentioned a word
8. (Not finished)Find strongly connected components
9. (Not finished)Find shortest path from a given user
99. Quit""")
        print("-"*15+"*"*10+"-"*15)
        menu = input("Select Menu: ")
        if menu in menuMap:
            menuMap.get(menu)()
        else :
            if menu == "55":break
            print("There is no Menu!. Plz select another number")
        
        #for x in hashTable:
        #    print(x)
