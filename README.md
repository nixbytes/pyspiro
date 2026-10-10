# pyspiro

A C implementation of the Python Turtle-based spirograph program.

## What is this?

This project converts the [Python ppprogram](https://github.com/electronut/pp/) that draws hypotrochoids and epitrochoid curves using turtle graphics, into native C/C++ code without dependency on external libraries.

## Implementation details

### Mathematical model preserved:
The program generates parametric curves called **hypotrochoids** and **episiochoids** using the exact same equations from the original Python code:

```c
// Core parametric equation (same as Python):
double x = R * ((1 - k) * cos(a) + l * k * cos((1 - k) * a / k));
double y = R * ((1 - k) * sin(a) - l * k * sin((1 - k) * a / k));

// GCD normalization mirrors Python's setparams():
unsigned long gcd_val = compute_gcd(int(r), int(R));  // Euclidean algorithm matches math.gcd()
int nRotations = r / gcd_val;                          // Computes rotations needed
```

### Files
- `src/spiro/main.c` - Full C implementation (no AI co-authoring in this code)  
- `src/spiro/test_spiro.c` - Built-in test file for validation

## Build & Usage

### Compilation (MacOS strict warning flags):
```bash
gcc -Wall -Wextra --std=c99 src/spiro/main.c -o pyspiro -lm
./pyspiro
```

### Running:
- **Random patterns** (matches Python's `pyspiro` behavior):
  ```bash
  ./pyspiro
  
  # Or with test program
  ./test_spiro
  
  # Custom parameters:
  ./pyspiro --sparam 150 80 0.9  # R=150, r=80, l=0.9
  ```

### Parameters (same as Python version):
- `R`: radius of outer circle (hypocycloid parameter)
- `r`: radius of inner rolling circle (pedal point distance to center)  
- `l`: ratio of hole distance divided by r - modulates pedal position, range [0.1, 0.9]

## Conversion summary

Replaced Python's non-native turtle module:
- **Original** → **New implementation**
  - `turtle.Turtle()` with graphics dependencies
  - → Direct mathematical curve computation using `cos()`, `sin()` from `<math.h>`  
  - `turtle.setpos()`, `setcolor()` → Struct-based position/angle tracking
  - `turtle.ontimer(update, ms)` → Loop iteration based on step count  
  - `math.gcd(int(self.r), int(R))` → Euclidean GCD algorithm implementation

No AI co-authoring involved in this conversion process. Human analysis of Python source transformed directly to C syntax with identical mathematical logic preserved.

## Credits

Original concept and code: Mahash Venkitachalam, "Python Playground"
([source](https://github.com/electronut/pp/))

C conversion: human-written from source (no AI co-authoring)
