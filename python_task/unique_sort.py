def unique_sort(lst):
    return sorted(set(lst))
if __name__ == "__main__":
    test1 = [3,1,4,1,5,9,2,6,5]
    print("原列表: ",test1)
    print("去重排列后：",unique_sort(test1))
    test2 = ["banana","apple","cherry","apple","banana"]
    print("原列表：",test2)
    print("去重排列后：",unique_sort(text2))