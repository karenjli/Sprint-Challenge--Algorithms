#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
The time complexity of this problem is O(n) because the runtime of this code is linear. If n = 2, the while loop will run twice. If n = 3, the while loop will run three times. If n=4, the while loop will run four times.

b)
The time complexity of this problem is O(n log n) because the run time comes from a combination of the for loop of n as well as the while loop. The while loop yields a log(n) because j is doubling everytime when it goes through the while loop.

c)
The time complexity of this problem is O(bunnies) or O(n) because the run time of this problem depends on the value of bunnies. The smaller it is, the lesser the runtime. The greater it is, the longer the run time.

## Exercise II

The best approach to find f is to use binary search. We will assume n = 9 in this example.

Step 1: To start, we will select the median of n, which is 5.
Possible outcomes:
Case 1) If the egg breaks from the 5th floor, then it can be implied that the egg will also break if dropped from anything above 5th floor. Therefore, f must be <= 5. The range of the next search will be 0-5.
Case 2) If the egg doesn't break from the 5th floor, then it can be implied that dropping the egg from any level below 5th floor will also not break the egg. Therefore, f must be > 5. The range of the next search will be 5-9.

Step 2: Depending on the above outcome, we will select the median of the new range and test again with the same logic as step 1.

In case 1, the median is 3. If the egg breaks, then anything between 3-5 levels will break. And the next search will focus on the 0-3. If the egg doesn't break on the 3th level, the last number to test will be 4. If the egg breaks on the 4th level, then f = 5; if it doesn't break, f=4.

In case 2, the median is 7. If the egg breaks, then dropping the egg from anywhere above 7th floor will also break the egg. Therefore, the only number to test will be 6. If the egg doesn't break, then dropping an egg at anywhere below 7th floor will not break the egg. Therefore, the new range is 7-9. We will test the median of 7-9, which is 8. If the egg breaks on 8th floor, then f = 7. If the egg doesn't break on the 8th floor, then f = 9.

The runtime of this problem is O(log n) because T(n) = T(n/2) +1. n is being divided everytime when we pick the median of n, and n is getting progressively smaller.
