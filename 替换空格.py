

class Solution:
    def ReplaceSpace(self, ss):
        """

        :param ss:
        :return:
        """

        if not ss:
            return None

        #统计字符串中个空格
        count = 0
        for i in ss:
            if i == " ":
                count += 1
        print(count)
        old_len = len(ss)
        new_len  = old_len + count * 2

        #定义两个指针
        #p1指向原始字符串的末尾
        #p2指向新字符串的末尾
        p1 = old_len - 1
        p2 = new_len - 1

        #定义一个空字符串用来保存复制的字符产
        new_str = [' '] * new_len

        while p1 != p2:
            if ss[p1] != " ":
                new_str[p2] = ss[p1]
                p1 -= 1
                p2 -= 1
            else:
                new_str[p2] = '%'
                new_str[p2 -1] = '0'
                new_str[p2- 2] = '2'
                p1 -=1
                p2 -=3

        #至此只有第一个空格前的字符没有复制
        for i in range(p1, -1, -1):
            new_str[i] = ss[i]
        print(new_str)
        #现在new_str是一个列表表
        #把列表转成字符串
        new_String = ''
        for i in new_str:

            new_String += i
        return new_String

s = Solution()
print(s.ReplaceSpace('we are happy'))

