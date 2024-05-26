price = float(input("What is the price of the product? $"))
new = price - (price * 5 / 100)
print("The product it cost ${:.2f}, in promotion with discount 5% will cost ${:.2f}".format(price, new))



