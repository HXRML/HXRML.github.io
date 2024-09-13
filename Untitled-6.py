num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("num_int 数据类型为:",type(num_int))
print("num_flo 数据类型为:",type(num_flo))

print("num_new 值为:",num_new)
print("num_new 数据类型为:",type(num_new))

def reverse_words(input_str):
    # 通过空格将字符串分隔，得到单词列表
    words = input_str.split()
    
    # 逆序每个单词内的字符
    reversed_words = [word[::-1] for word in words]
    
    # 重新组合字符串
    output = ' '.join(reversed_words)
    
    return output

if __name__ == "__main__":
    input_str = 'I like runoob'
    rw = reverse_words(input_str)
    print(rw)