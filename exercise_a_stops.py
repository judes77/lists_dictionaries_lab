stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

# #1. Add "Edinburgh Waverley" to the end of the list
# stops.append("Edinburgh")
# #2. Add "Glasgow Queen St" to the start of the list
# stops.insert(0, "Glasgow Queen St",)
# #3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
# stops.insert(4, "Polmont")
# #4. Print out the index position of "Linlithgow"
# print(stops.index("Linlithgow"))
# #5. Remove "Livingston" from the list using its name
# stops.remove("Livingston")
# #6. Delete "Cumbernauld" from the list by index
# stops.pop(2)
# #7. Print the number of stops there are in the list
# print(len(stops))
# #8. Sort the list alphabetically
# stops.sort()
# #9. Reverse the positions of the stops in the list
# stops.reverse()
# #10 Print out all the stops using a for loop
# for stop in stops:
#     print(stop)
#11. Print out only the stops that begin with the letter L using a for loop
# for stop in stops:
#     if stop [0] == "L":
#         print(stop)
#12. Remove all stops that begin with the letter C using a for loop
# for stop in stops:
#     if stop[0] == "C":
#         stops.remove(stop)
for stop in stops:
    if stop[0] != "C":
        print(stop)
        

        

print(stops)