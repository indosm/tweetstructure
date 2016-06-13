'''
2015410087 김지헌
version 0.0.2
2016/06/13
'''
def read_data():
    print("its 1")
def disp_stat():
    print("its 2")
def top5_word():
    print("its 3")
def top5_user():
    print("its 4")
def find_usr():
    a=10
def find_friend():
    a=10
def del_ment():
    a=10
def del_usr():
    a=10
def find_scc():
    a=10
def find_short_path():
    a=10
if __name__ == "__main__":
    print("0. Read data files\n\
1. display statistics\n\
2. Top 5 most tweeted words\n\
3. Top 5 most tweeted users\n\
4. Find users who tweeted a word (e.g., ’연세대’)\n\
5. Find all people who are friends of the above users\n\
6. Delete all mentions of a word\n\
7. Delete all users who mentioned a word\n\
8. Find strongly connected components\n\
9. Find shortest path from a given user\n\
99. Quit")
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
        "99":quit
        }
    while True:
        menu = input("Select Menu: ")
        if menu in menuMap:
            menuMap.get(menu)()
        else :
            print("There is no Menu!. Plz select another number")
