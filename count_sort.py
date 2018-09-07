
class CountSort(object):
    def sort(self, A):
        k = self.lagest_element(A)
        count_list = [0] * (k + 1)
        for elem in A:
            count_list[elem] += 1
        
        
        for i in range(1, len(count_list)):
            count_list[i] += count_list[i-1]
        
        sorted_list = [0] * len(A)

        for index in range(len(A) - 1, -1, -1):
            sorted_list[count_list[A[index]] - 1] = A[index]
            count_list[A[index]] -= 1        
        return sorted_list
    
    def lagest_element(self, A):
        max = None
        for x in A:
            if max is None or max < x:
                max = x
        return max

if __name__ == "__main__":
    obj = CountSort()

    ri = raw_input("Enter list items to be sorted\n").strip()
    A = ri.split(" ")
    A = list(map(int, A))
    ans = obj.sort(A)

    print(ans)