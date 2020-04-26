'''

class BMI:
関連しそうな属性
        ー身長
        ー体重
        ーBMIという値そのもの
    ルール：
        ー　１０位上４０以下＜ーー常識的な範囲
        ー　表示するときは、小数点第二位まで
            ーex: 23.6778 ->23.67
            -ex: 23.671 ->23.67
'''


class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        if not 10 <= self.calculate_bmi() <= 40:
            print("アウト")

    def calculate_bmi(self):
        return self.weight / (self.height **2)




# BMIのクラスのインスタンス化
hibiki_bmi = BMI(height=1, weight=67.0)
noriya_bmi = BMI(height=1.78, weight=75.0)

print (hibiki_bmi.calculate_bmi())



