# inversion_in_array

This repository contains a Python program to calculate the total number of inversions in an array.

## What is an Inversion?

An inversion in an array is a pair of indices `(i, j)` such that:
- `i < j`
- `arr[i] > arr[j]`

For example, in the array `[16, 8, 4, 2, 1]`, there are 10 inversions:
- `(0, 1), (0, 2), (0, 3), (0, 4)`
- `(1, 2), (1, 3), (1, 4)`
- `(2, 3), (2, 4)`
- `(3, 4)`

## How the Program Works

The program uses a modified merge sort algorithm to count the number of inversions efficiently. The merge sort divides the array into smaller subarrays, counts the inversions in each subarray, and then counts the inversions across the subarrays during the merge step.

### Key Functions:
1. **`merge_and_count`**:
   - Merges two sorted subarrays and counts the number of inversions across them.
   - For every element in the left subarray that is greater than an element in the right subarray, the number of inversions is incremented by the number of remaining elements in the left subarray.

2. **`merge_sort_and_count`**:
   - Recursively divides the array into smaller subarrays and calls `merge_and_count` to count inversions.

3. **`count_inversions`**:
   - The main function that initializes a temporary array and calls `merge_sort_and_count`.

## How to Run the Program

1. Clone this repository to your local machine.
2. Run the `inversion.py` file using Python:
   ```bash
   python inversion.py

## Example Output
1. For the array [16, 8, 4, 2, 1], the program will output: 
2. Number of inversions are: 10


## Customizing the Input
**To test the program with a different array:**

1. Open the inversion.py file.
2. Modify the array variable in the if __name__ == "__main__": block:
3. array = [your, custom, array, here]
4. Save the file and re-run the program

## Complexity
1. Time Complexity: O(n log n) (due to the merge sort algorithm).
2. Space Complexity: O(n) (for the temporary array used during merging).
