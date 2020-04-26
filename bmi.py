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
        self.value = weight / (height ** 2)
        if not (10 <= self.value <= 40):
            raise ValueError("BMIが正常値の範囲を超えています。")


    def __str__(self):
        # return f"{self.value:.2f}"
        return str(round(self.value,2))





# BMIのクラスのインスタンス化
hibiki_bmi = BMI(height=1.67, weight=67.0)
noriya_bmi = BMI(height=1.78, weight=75.0)

print(hibiki_bmi)




