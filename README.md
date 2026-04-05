#  Quick sort
----Why quick sort is the optimal sorting algorithm for this case----

Quick sort has a much more efficient time complexity than the quadratic sorting algorithms and a better space complexity than merge sort. It still may slip into O(n^2) time complexity in the worst case where the array is divided into two parts where one has n-1 elements. At worst space complexity it is the same as merge sort O(n). In the best case its time complexity is O(n log n) and space complexity O(log n) which is what makes it such a highly useful algorithm. It is optimal in cases with large unstructured data sets where stability is not a requirement. The divide and conquer strategy can be easily visualized and understood by beginner programmers. The algorithm works on the basis of a pivot element used to partition the array. It then reorders the array into smaller subarrays recursively sorting them on the left and right if less or greater than the pivots value. 
## Demo video/gif/screenshot of test



https://github.com/user-attachments/assets/5b9666dd-6372-4187-a1a9-8713b8962409


## Problem Breakdown & Computational Thinking 
Decomposition

This algorithm uses the divide and conquer method which is a form of decomposing the array into smaller subarrays.
This essentially breaks down the larger problem into subproblems where the method of finding the median and sorting the right and left halves can be easily applied,   amalgamating to the final desired output.

Pattern Recognition

The algorithm makes a recursive call to repeatedly organize the subarrays from least to greatest, simultaneously, which increases its efficiency.
Each subarray has the function of finding a median and sorting the left and right halves from least to greatest.

Abstraction

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

START-->Receive unordered list-->Is list size ≤ 1?--- YES ----> Return list (Base case)--------------- |>
 NO-->Choose Pivot----->Partition list into:  Left (values < pivot)----Pivot----- Right (values > pivot)
 ---> Apply QuickSort recursively to Left----->Apply QuickSort recursively to Right---> Combine:
Sorted Left + Pivot + Sorted Right---> Return Sorted List------------------> END

## Steps to Run
-Steps to run program within python: Ensuring that each edge case was handled. I started with a simple version of code and made adjustements so that it satisfied each constraint highlighted below.
<img width="870" height="693" alt="Screenshot 2026-04-04 142102" src="https://github.com/user-attachments/assets/e1042a78-54b2-41ba-9cab-344c88b9c194" />
---Handling edge cases---

If list is already sorted:
<img width="870" height="91" alt="Screenshot 2026-04-04 142448" src="https://github.com/user-attachments/assets/e8efb0ca-c1f3-4b09-9e94-dd56c3af9458" />


If list has no elements:
<img width="771" height="118" alt="Screenshot 2026-04-04 151755" src="https://github.com/user-attachments/assets/37c06a17-f0f7-458a-8e47-84efba6ac15d" />


If user inputs integers without commas:
<img width="1042" height="65" alt="Screenshot 2026-04-04 142638" src="https://github.com/user-attachments/assets/b7c5b6d7-79db-4fd9-9946-9a2284c84671" />

<img width="896" height="31" alt="Screenshot 2026-04-04 142703" src="https://github.com/user-attachments/assets/c9134b27-84f9-480e-8f6f-335aa768fd63" />

<img width="1021" height="184" alt="Screenshot 2026-04-04 142857" src="https://github.com/user-attachments/assets/4d9fdd60-238b-43e1-acbb-7254fbbd2e7f" />


If list has the same repeated value for each element:

<img width="869" height="107" alt="Screenshot 2026-04-04 151856" src="https://github.com/user-attachments/assets/b1ab37af-8a2a-4336-a952-c9a50279b803" />

If input type is invalid:

<img width="1047" height="123" alt="Screenshot 2026-04-04 143038" src="https://github.com/user-attachments/assets/1f7abedc-927b-4c5d-bcf0-c5de71d36930" />

<img width="903" height="181" alt="Screenshot 2026-04-04 151605" src="https://github.com/user-attachments/assets/5e4b39b1-6bbd-4ce1-87c6-6b1ee582e91f" />


If stability is a requirement:

<img width="961" height="105" alt="Screenshot 2026-04-04 152036" src="https://github.com/user-attachments/assets/7321cf67-1628-415c-afda-0eaf96a81e49" />

Steps to run program with Gradio
Modified code for app


Program first launch

Updated version to include a bar graph and interactable features:





## Hugging Face Link

https://huggingface.co/spaces/EK555555555555555555555555555555555/quicksort-visualizer 

## Author & Acknowledgment
Ella Koroshegyi
