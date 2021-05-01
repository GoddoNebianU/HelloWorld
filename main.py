import os, time, copy

class Dfs:

    def __init__(self, amap, p1, p2):
        self.amap = amap
        self.p1 = p1
        self.p2 = p2

        self.I = 0
        self.mark = []

        self.bmap = copy.deepcopy(self.amap)

    def show(self):
        s = ''
        for i in self.bmap:
            for j in i:
                s += j + '\t'
            s += '\r\n'
        print(s)

    def pt(self, l):

        # 勾股定理计算优先度
        distance = []
        l2 = {}
        for i in range(len(l)):
            distance = ((self.p1[0] + l[i][0]) - (self.p2[0])) ** 2 + ((self.p1[1] + l[i][1]) - self.p2[1]) ** 2
            l2[distance] = l[i]
        keys = list(l2.keys())
        keys.sort()
        l = []
        for key in keys:
            l.append(l2[key])
        return l

    def dfs(self):

        # 标记当前位置
        self.mark.append(self.p1)
        
        # 展示bmap
        self.bmap[self.p1[0]][self.p1[1]] = str(self.I)
        os.system('clear')
        self.show()
        self.I += 1
        print(self.mark)
        time.sleep(0.2)

        # 检测是否到达终点
        if self.p1 == self.p2:
            return True

        can_walk = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # 检测四周是否有路，如果有就记录下来
        walk = []
        for l in can_walk:
            try:
                if self.amap[self.p1[0] + l[0]][self.p1[1] + l[1]] == '' and [self.p1[0] + l[0], self.p1[1] + l[1]] not in self.mark:
                    walk.append(l)
            except Exception as e:
                print(e)
        print(walk)
        
        if  not walk:
            return False
        
        # 排序
        walk = self.pt(walk)

        # 枚举每一种可能进行递归
        for l in walk:
            if [self.p1[0] + l[0], self.p1[1] + l[1]] in self.mark:
                continue

            bakp1 = copy.deepcopy(self.p1)

            self.p1 = [self.p1[0] + l[0], self.p1[1] + l[1]]
            r = self.dfs()

            if r:
                return True
            else:
                self.p1 = bakp1
        return False

if __name__ == '__main__':
    amap = [
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', '', '', '', '', '', '', 'X'],
            ['X', 'X', 'X', '', '', '', '', 'X'],
            ['X', '', 'X', '', '', '', '', 'X'],
            ['X', '', 'X', '', '', '', '', 'X'],
            ['X', '', 'X', '', '', '', '', 'X'],
            ['X', '', '', '', '', '', '', 'X'],
            ['X', 'X', '', '', '', '', '', 'X'],
            ['X', 'X', 'X', 'X', '', 'X', 'X', 'X'],
            ['X', 'X', 'X', '', '', '', '', 'X'],
            ['X', '', '', '', 'X', '', '', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
    a = Dfs(amap, [1, 1], [10, 1])
    print(a.dfs())
