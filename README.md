## Line Overlap Checker
Checks if two lines (x1,x2) and (x3,x4) on the x-axis overlap
   

#### Quick example
- Run `python3` to set up interactive mode
- Import `line_overlap_checker` and call with arguments
```
>>> from program import line_overlap_checker
>>> line_overlap_checker((1,5), (2,6))
True
>>> line_overlap_checker((1,5), (6,8))
False
>>> line_overlap_checker((6,5), (4,8))
True
```

#### Running tests
 - Run `python3 tests.py`
