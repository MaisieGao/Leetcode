**1.quicksort**

quick sort use divide and conquer
pick an element as pivot (could pick the last element in the list)
make all the smaller than x elements before x and put all greater elements after x. this process should be done in linear time

![quicksort partition](../screenshots/QuickSort2.png)

average time complexity: O(n logn)

worst: O(n^2)

QuickSort is an *unstable* algorithm because we do swapping of elements according to pivot's position (without considering their original positions).

To elaborate on this a bit, [5(1st), 5(2nd), 5(3rd), 1, 4] as the example, where 4 is the pivot, when we swap 1 with the first 5, we get [1, 5(2nd), 5(3rd), 5(1st), 4], swapping the second 5 with the pivot gives us [1, 4, 5(3rd), 5(1st), 5(2nd)], which is the final result we will get with quicksort, clearly, the original order of 5 is not preserved, i.e., not stable. 


<hr>

**2.mergesort**

merge sort use divide and conquer
divide the array in half recursively

Time complexity of Merge Sort is  θ(nLogn) in all 3 cases (worst, average and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.

Merge Sort is a *stable* sort which means that the same element in an array maintain their original positions with respect to each other.

<hr>
quicksort是先compare,交换，然后再call two sub quicksort
mergesort是先分mid,call two sub mergesort, 然后再将两个有序的sublist合起来

<hr>

**list add item**
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")

**list remove specific item**

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

**list remove specific index**

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

**Join two list**
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

or

for x in list2:
  list1.append(x)

or

list1.extend(list2)

<hr>

**add item to the set:**

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

**remove item for set:**

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

用pop()只能remove最后一个item,因为set没有index

**join sets:**

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

<hr>

**remove item from dict**
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")

<hr>

**sort**
interval.sort(可以用lambda)
sorted(tuple/set/string/可以用lambda)->sort完之后是list