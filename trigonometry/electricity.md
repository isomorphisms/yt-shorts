# Electricity — trigonometry examples

This is a queue, not one Short. Electricity has several genuinely different uses of sine and cosine, and they should not be collapsed into a generic sine-wave animation.

## 1. AC voltage: what 120 V RMS means

For an ideal sinusoidal voltage,

`v(t) = V_peak sin(ωt)`.

The RMS value is

`V_RMS = V_peak / √2`.

So a 120 V RMS sine wave has a peak magnitude of about 169.7 V.

Visual idea:

- start with the horizontal 120 V RMS label;
- draw the actual sine wave growing behind it;
- mark the +169.7 V and -169.7 V peaks;
- shade or otherwise show that RMS is an equivalent heating/power measure, not the amplitude of the wave.

This needs a careful later pass if we want to explain RMS rather than merely state the conversion.

## 2. Generator / rotating vector → sine wave

This is perhaps the cleanest “why sine?” electricity Short.

- rotate a vector or coil at constant angular speed;
- project the rotating quantity onto one axis;
- trail that projection in time to draw a sine wave;
- show one full turn corresponding to one full electrical cycle.

The trig is visible as geometry before it becomes a graph.

## 3. Voltage-current phase difference

Use two sinusoids with the same frequency but a phase difference `φ`:

`v(t) = V_peak sin(ωt)`

`i(t) = I_peak sin(ωt - φ)`.

Visual idea:

- first show the two rotating phasors with angle `φ` between them;
- unwrap them into two sine waves;
- keep a vertical cursor moving across both waves so the lead/lag remains concrete.

Possible applied versions: nearly resistive load (`φ ≈ 0`), inductive load (current lags), capacitive load (current leads). Verify the specific physical model/source before turning those into production copy.

## 4. Power factor — cosine has a job

For sinusoidal steady-state voltage/current, average real power can be written

`P = V_RMS I_RMS cos φ`.

Hold `V_RMS` and `I_RMS` fixed while changing only the phase angle. Then the real-power fraction is just `cos φ`.

Useful marks:

| φ | cos φ |
|---:|---:|
| 0° | 1.00 |
| 30° | 0.87 |
| 45° | 0.71 |
| 60° | 0.50 |
| 90° | 0.00 |

Animation idea: keep two same-length phasors fixed in magnitude, open the angle between them, and simultaneously shrink the real-power projection.

## First choice

The rotating-vector/generator picture is the strongest introductory trig visual because the sine wave is *produced* by a projection rather than simply announced. Power factor is stronger as a later practical cosine example.
