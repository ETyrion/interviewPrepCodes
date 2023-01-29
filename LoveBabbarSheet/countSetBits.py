def setBits(N:int) -> int:
    binary_num = int(bin(N).replace("0b", ""))
    count = 0
    num = binary_num
    while num != 0:
        rem = num % 10
        count = count + rem
        num = num//10
    print(count)
setBits(6)
