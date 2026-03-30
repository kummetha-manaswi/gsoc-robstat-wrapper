# RobStatTM Python Wrapper using RPy2

## Overview
This project provides Python wrappers for robust statistical functions from the RobStatTM R package using RPy2.

## Features
- Access R robust statistics from Python
- Functions implemented:
  - locScaleM
  - scaleM

## Example

```python
from wrapper import loc_scale_m, scale_m

data = [1,2,3,100,5]

print(loc_scale_m(data))
print(scale_m(data))
### Sample Output

locScaleM: [2.75, 0.7395, 2.3077]  
scaleM: 4.8136
## Contribution
Initial wrapper implementation and testing using RPy2 for RobStatTM functions.
