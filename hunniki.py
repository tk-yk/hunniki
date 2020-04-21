'''
データ型宣言　：　UsewrName
    属性：
    　実際のユーザー名
    ルール：
    　・４文字以上２０文字以下である
    できること
    　・ユーザー名を大文字に変換する
'''

class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f"{name}は文字数のルール違反です！")
        self.name = name

    def screen_name(self):
        return self.name.upper()



hibiki = UserName(name="hibiki")

# sho = UserName("sho")

print(type(hibiki))
print (hibiki.screen_name())

# print (sho.name)







