#write a function that rotates the list by m position 
def rotate_list(lst, positions):
    if not lst:
        return lst
    positions = positions % len(lst)
    return lst[-positions:] + lst[:-positions]

l=[1,2,3,4,5]
m=2
ans=rotate_list(l,m)
print("original list:",l)
print("\n rotated list:",ans)

