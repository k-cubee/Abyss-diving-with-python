print("\033c")
friends = ["Kevin", "Jim", "Karen", "Mike", "Mosh"]
luckyNumbers = [1, 22, 3, 4, 5, 6]
friends.insert(1, "Poppy")
friends.pop()
friends[1] = "John"
friends.append("Marija")
print(friends)
luckyNumbers.sort()
luckyNumbers.reverse()
luckyNumbers.extend(friends)
print(luckyNumbers)
