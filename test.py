class Bun(object):
    def __init__(self, contents, price):
        self.contents = contents
        self.price = price
        self.total_sales = 0

    def sell(self):
        self.total_sales += self.price
        print(f"{self.contents} 붕어빵이 판매되었습니다. 가격: {self.price}원")

    def eat(self):
        print(f"{self.contents} 붕어빵을 먹습니다.")

# 슈크림 붕어빵 객체 생성
cream_bun = Bun(contents="슈크림", price=1500)

# 팥 붕어빵 객체 생성
red_bean_bun = Bun(contents="팥", price=1000)

# 붕어빵 판매 및 먹기 예시
cream_bun.sell()  # 출력: "슈크림 붕어빵이 판매되었습니다. 가격: 1500원"
cream_bun.eat()   # 출력: "슈크림 붕어빵을 먹습니다."

red_bean_bun.sell()  # 출력: "팥 붕어빵이 판매되었습니다. 가격: 1000원"
red_bean_bun.eat()   # 출력: "팥 붕어빵을 먹습니다."

# 총 판매금 출력
print(f"총 판매금: {cream_bun.total_sales + red_bean_bun.total_sales}원")
