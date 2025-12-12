import array as a

#create
arr = a.array('i',[12,25,37,45,58])
#display
print(f"original array: {arr}")
#append
arr.append(92)
print("afer append:  ",arr)
#insert
arr.insert(2,30)
print("after insert:   ",arr)
#reverse
arr.reverse()
print("after reverse:   ",arr)