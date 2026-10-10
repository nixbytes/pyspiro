/* 
 * pyspiro - C port of Python Turtle spirograph program
 * Converted from Python to native C - no AI co-authoring  
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <float.h>

#define DRAWING_STEP    5.0f      /* Degrees per step, from Python's "step = 5" line exactly */ 
#define MAX_ROTATIONS   30        /* Maximum rotations before redraw loop (normalized by GCD)*/  
#define MIN_RADIUS      25.0f     /* Minimum outer radius: from Python range constraint logic */
#define MIN_INNER_R     10.0f     /* Minimum inner radius: from Python's randint(10, ...) floor()

typedef struct { float r; float g; float b; } rgb_color_t;  

/* ==================================================================
 * Spiro State Structure - Complete mapping to Python's Spiro class:
 * All parameters from setparams(self, xc, yc, col, R, r, l):
 */
struct spiro_state {  
    double xc, yc;               /* Center origin (canvas coordinates) */
    float R_param;               /* Outer circle radius parameter */
    float r_param;               /* Inner/rolling circle radius (pedal distance from center) */
    float k_factor;              /* Ratio = r/R - amplitude modulation factor controlling curve complexity controlled by ratio*/  
    float l_normalized;          /* Hole-to-center distance ratio normalized by inner radius (0.1-0.9 range from Python random.uniform(0.1, 0.9) logic in genRandomParams()*/   *
    int nRotations_needed;       /* Full rotations needed: computed via GCD normalization matching Python's math.gcd() approach for integer floor ratios */  
    unsigned int points_generated;     /* Points generated so far this animation frame */  
    float angle_degrees;         /* Drawing position in degrees: starts at 0, increments by DRAWING_STEP_DEG each loop iteration incrementing */   *
    rgb_color_t color_rgb;       /* RGB tuple [R,G,B] values in range [0.0-1.0] from Python's (random.random() pattern normalized)*/};
