n = int(input())
 
for _ in range(n):
    name_len = int(input())
    first_name, second_name = input().split(" ")
    
    f_arr = sorted(list(first_name))
    s_arr = sorted(list(second_name))
    
    is_pass = True
    for i in range(name_len):
        if f_arr[i] != s_arr[i]:
            print("NO")
            is_pass = False
            break
    if is_pass:
        print("YES")
        