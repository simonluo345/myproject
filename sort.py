
def sort_list(list1):
	n = len(list1)
	i = 0
	while(i < n):
		j = 0
		while(j < n - i - 1):
			temp = 0
			if list1[j] > list1[j+1]:
				temp = list1[j]
				list1[j] = list1[j+1]
				list1[j+1] = temp
			j += 1
		i += 1
	return list1

def main():

	list1 = [1,3,2,7]
	sort_list(list1)
	print(list1)

main()

