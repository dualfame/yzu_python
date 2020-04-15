symbol = "2330"
name = "台積電"
price = 286.5
shares = int(input('股數='))

print("2330 台積電成交價 286.5 買進 5000股 (5張) 成本 1,432,500")
# %s text, %d int, %.nf floating (n=位數)
print("%s %s 成交價 %.1f 買進 %07d股 (%d張) 成本 %.2f" %
      (symbol, name, price, shares, shares/1000, price*shares))
