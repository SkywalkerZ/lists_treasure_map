#creating lists
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
#nesting lists
map = [row1, row2, row3]
#print matrix
print(f"{row1}\n{row2}\n{row3}")

#index logic
position = input("Where do you want to put the treasure? ")
position_index=[int(i) for i in str(position)]
position_index_0=position_index[0]
position_index_1=position_index[1]
map_index_0=position_index_0-1
map_index_1=position_index_1-1
map[map_index_1][map_index_0] = 'X'

#print final matrix
print(f"{row1}\n{row2}\n{row3}")

