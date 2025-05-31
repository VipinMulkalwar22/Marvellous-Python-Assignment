# Assignment 9 - Python Programs

This folder contains Python scripts for Assignment 9, each focusing on threading and multiprocessing concepts.

## Files Overview

### 1. Assignment9_1.py

**Description:**  
- Demonstrates basic threading by running the same function in three threads with delays.

**Example Output:**
```
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
```

---

### 2. Assignment9_2.py

**Description:**  
- Demonstrates multiprocessing by creating a separate process for each number to print its square, along with process IDs.

**Example Output:**
```
Enter the number of element
3
Enter the each element
2
4
6
0 = 2
process id: 12345
Process-1
Sqaure of 2 is 4
1 = 4
process id: 12346
Process-2
Sqaure of 4 is 16
2 = 6
process id: 12347
Process-3
Sqaure of 6 is 36
```

---

### 3. Assignment9_3.py

**Description:**  
- Uses a multiprocessing pool to compute the factorial of each number in a list.

**Example Output:**
```
Enter the number of Element
4
Enter the each element
3
4
5
6
[6, 24, 120, 720]
```

---

### 4. Assignment9_4.py

**Description:**  
- Compares the execution time of a function (sum of first N numbers) when run normally, with threading, and with multiprocessing.

**Example Output:**
```
Addition is 50000005000000
Total Time for normal fuctions is 0.5
Addition is 50000005000000
Total Time for Threading is 0.6
Addition is 50000005000000
Total Time for Multiprocessing is 0.7
```

---

## How to Run

1. Make sure you have Python 3 installed.
2. Open a terminal or command prompt.
3. Navigate to this folder.
4. Run any script using:
   ```
   python Assignment9_X.py
   ```
   Replace `X` with the script number (e.g., `python Assignment9_2.py`).

---
