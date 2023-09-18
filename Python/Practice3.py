Input_Money = int(input("투입한 돈:"))
Price = int(input("물건의 가격:"))
Change = Input_Money-Price
print("거스름 돈:",Change)
Change_500 = Change//500
print("500 동전 개수:",Change_500)
print("100 동전 개수:",(Change%500)//100)