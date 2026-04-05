# Quick-Sort-Program--CISC-121-Project
Implementing the quick sort algorithm to a visual app so that beginners may understand the logic behind this algorithm.
#  Quick sort
Why quick sort is the optimal sorting algorithm for this case
Quick sort has a much more efficient time complexity than the quadratic sorting algorithms and a better space complexity than merge sort. It still may slip into O(n^2) time complexity in the worst case where the array is divided into two parts where one has n-1 elements. At worst space complexity it is the same as merge sort O(n). In the best case its time complexity is O(n log n) and space complexity O(log n) which is what makes it such a highly useful algorithm. It is optimal in cases with large unstructured data sets where stability is not a requirement. The divide and conquer strategy can be easily visualized and understood by beginner programmers. The algorithm works on the basis of a pivot element used to partition the array. It then reorders the array into smaller subarrays recursively sorting them on the left and right if less or greater than the pivots value. 
## Demo video/gif/screenshot of test
## Problem Breakdown & Computational Thinking 
Decomposition
This algorithm uses the divide and conquer method which is a form of decomposing the array into smaller subarrays.
This essentially breaks down the larger problem into subproblems where the method of finding the median and sorting the right and left halves can be easily applied,   amalgamating to the final desired output.
Pattern Recognition
The algorithm makes a recursive call to repeatedly organize the subarrays from least to greatest, simultaneously, which increases its efficiency.
Each subarray has the function of finding a median and sorting the left and right halves from least to greatest.
""Abstraction""
The algorithm focuses on applying identical functions to each smaller subarray rather than dealing with the whole array at once.
The pivot and partition process allows the key details of sorting the median and organizing left and right halves to be the main driver of the program.
The subgoals are easily attained so the larger goal is within reach. 
Algorithmic design
Choose a pivot element. It can be the first, last, median, or random element.
Partition the array, rearranging elements from smallest value on the left of the pivot to the largest on the right side of the pivot.
Add recursive calls. Applying the same logic to the left and right subarrays until the base case is reached.
Input: Unordered list of data(integers) where stability is not a requirement.
Processing: Choose pivot, partition and rearrange into subarrays, recursive call applied to each subarray till base case reached and list is sorted from least to greatest valued elements. All edge cases must be handled.
Output: Must show each step of this process including the subarrays in which the list is divided and the logic behind the way they are continuously sorted from least to greatest. Must also include a copy of the input list and the newly sorted list.
START
 |
 v
Receive unordered list
 |
 v
Is list size ≤ 1?
 |---- YES ----> Return list (Base case)
 |
 NO
 |
 v
Choose Pivot
 |
 v
Partition list into:
  Left (values < pivot)
  Pivot
  Right (values > pivot)
 |
 v
Apply QuickSort recursively to Left
Apply QuickSort recursively to Right
 |
 v
Combine:
Sorted Left + Pivot + Sorted Right
 |
 v
Return Sorted List
 |
 v
END

## Steps to Run
Steps to run program within python

Handling edge cases
If list is already sorted:

If list has no elements:


If user inputs integers without commas:



If list has the same repeated value for each element:

If input type is invalid:

If stability is a requirement:

Steps to run program with Gradio

## Hugging Face Link
## Author & Acknowledgment

