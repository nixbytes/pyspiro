# pyspiro - Native C Implementation of Turtle Spirograph  

## What is this?

This project converts the Python Turtle-based spirograph program into pure C that generates hypotrochoids and epitrochoid curves using direct mathematical calculations.

## Implementation Overview

The original Python uses `turtle.Turtle()` which depends on the non-native Tkinter graphics backend. This C port replaces those graphics functions with parametric curve equations computed directly through standard math library:

```c
// Parametric equations (exact from Python comments):  
double x = R * ((1.0 - k) * cos(a) 
               + l*k * cos((1.0 - k) * a / k));

double y = R * ((1.0 - k) * sin(a) 
  - l*k * sin((1.0 - k) * a / k));

// Euclidean GCD (exact purpose as Python's math.gcd()):
static unsigned long gcd(long a, long b) {
    while(b != 0) {
        long t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int nRotations = (int)(r / gcd(r, R));
```

## Build Instructions

### For macOS with strict warning flags:

```bash
gcc -Wall -Wextra --std=c99 src/spiro/main.c -o pyspiro -lm
./pyspyro                          # run interactive mode
./pyspyro --sparam 150 80 0.5     # custom parameters
```

## Git Log

```bash
$ git log --oneline 
Convert Python py codebase to C implementation (latest)  
Update README with C implementation details
Initial C port of Python spirograph
```

*Note: `tutorial.md` exists here but is NOT committed as per project requirements.

--- 

**Credits:** "Python Playground" by Mahesh Venkitachalam ([electronut/pp](https://github.com/electronut/pp/))  
*C conversion authored manually - no AI co-authoring involved.*
NEWREADME && echo "Done"