def count_inversions(arr):
    """
    Function to count the total number of inversions in an array.
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
    """
    def merge_and_count(arr, temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0

        # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # There are mid - i inversions, because all the remaining elements in the left subarray
                # (arr[i], arr[i+1], ..., arr[mid]) are greater than arr[j]
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        # Copy the remaining elements of left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy the sorted subarray into Original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    def merge_sort_and_count(arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
            inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
            inv_count += merge_and_count(arr, temp_arr, left, mid, right)

        return inv_count

    # Create a temporary array
    temp_arr = [0] * len(arr)
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)



if __name__ == "__main__":
    array = [16, 8, 4, 2, 1]
    print("Number of inversions are:", count_inversions(array))