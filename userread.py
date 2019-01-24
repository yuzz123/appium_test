def read_file(file):
    pos = []
    with open(file, 'r') as f:
        #print(f.read()) # 输出语句
        lines = f.readlines()
        for line in lines:
            pos.append(line)
    f.close()
    return pos

file = 'F:\\Python 3.7\\userstest.txt'
users=read_file(file)
print(users)
print(users[0])

