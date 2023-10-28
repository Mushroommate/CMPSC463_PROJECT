<h1 align="center">CMPSC463 PROJECT: Hybrid Sorting</h1>
<h2 align="center">Hi 👋, I'm Gwen Hu</h2>

Description: An union of various sorting techniques that are selected and applied based on heuristics to optimize the sorting process. <br>
<br>
Goal: To optimize efficient sorting performance by implementing different algorithms and provide an in-depth understanding.<br>
<br>
1)Algorithms Implemented: <br>
- Insertion Sort
 >FOR _Small-sized_ array. Simple and efficient.<br> 
- Merge Sort<br>
 >FOR _Medium-sized_ array. Divide-and-conquer.<br>
- Bubble Sort
 >FOR _Nearly sorted_ array. Adjacent compared and swap as needed.<br>
- Parallel Sort: [Merge Sort],[Quick Sort]<br>
> FOR _larger_ array. Multi-threading leads to sort quicker by dividing and conquering.

<br><br>
2) Heuristic:
 >Any added heuristics allow the algorithm to adapt to different data characteristics, improving efficiency.
- Sorted
  >check if the input array is already sorted.
- Nearly Sorted:
  >check if the input array is nearly sorted which performs better with bubble sort.
- Reverse Sorted:
  >check if the input array is already sorted reversely.
- Duplicate:
  >Any duplicated(same) element.
  
  
<br><br>  

3) Benchmark Result:
>Test Case: [320, 323, 444, 2888, 2901, 9038, 29681]
- Memory Usage:<br>-The usage of the hybrid sorting algorithm was generally higher than it for small arrays.<br>
-If many duplicate elements exist, the hybrid algorithm performed better in terms of memory usage.<br>
-For larger sized, the multi-threaded sorting techniques consumed more memory.<br>
  >Average: 21.0 MiB
  
<br><br>
- Exectiion Time:<br>-For small arrays (with fewer than 64 elements), the insertion sort showed the fastest execution time.<br>
-For medium arrays (up to 10,000 elements), the hybrid algorithm's combination of merge sort and quick sort exhibited competitive performance.<br>
-For larger arrays, the multi-threaded sorting techniques significantly improved the execution time.<br>
  >Average: 1.38 sec on Test Case.
   >Compared to bubble sort, 36% quicker.  
4) Summary on performance:<br>

 
The hybrid-sort scans out an appropriate sorting technique based on heuristics.
Whether the data is already sorted or nearly sorted, any sorting is performed.
Different algorithm used depends on the duplicates and size.

  





<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>
