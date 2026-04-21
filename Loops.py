# while loop
# i = int(input())

# while i <= 5:
#     print("Hello world")
#     i += 1

list = [1, 5, 6, 2, "rajeev", "bartwal", 8.9, { "age" : 10}]
# for loop

i = 0


# while i < len(list):
#     print(list[i])
#     i += 1


for i in list:
    print(i)


# skip iteration using continue
# break will terminate the loop
for x in range(10):
    if x % 3 == 0:
        continue

    if x == 7 :
        break
    print(x)
