# Coding Assignment

This repository contains the solutions to the coding assignment problems described on the [`Coding Assignment.md`](Coding%20Assignment.md) file.
All the problems are solved in Python 3.10.

## Executing each problem

### Problem 1

```bash
python3 problem1.py
```
The program will prompt you to enter the number of jobs, start time, end time, and earnings for each job. The program will return the number of tasks and earnings available for others.

Constraints:
- The number of jobs in the day is less than 100 i.e. 0<_n<_10
- The start time is always less than the end, and Hours can go only up to 2359.

If any of the constraints are violated, the program will raise an error and end the execution.
### Problem 2

```bash
python3 problem2.py input_file output_file
```

The program will read the input from the input file and write the output to the output file. 
The Input file should follow the following format:
```
Number of employees: 4
Goodies and Prices:
Fitbit Plus: 7980
IPods: 22349
MI Band: 999
Cult Pass: 2799
Macbook Pro: 229900
Digital Camera: 11101
Alexa: 9999
Sandwich Toaster: 2195
Microwave Oven: 9800
Scale: 4999
```

If the input file is not provided, the program will read the input from `sample_input.txt`
If the output file is not provided, the program will write the output to `sample_output.txt`