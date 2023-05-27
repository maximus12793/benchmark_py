# [Mandelbrot benchmark... but fast!](https://benchmarksgame-team.pages.debian.net/benchmarksgame/description/mandelbrot.html#mandelbrot)

### **Context**
The Mandelbrot set is a well-known fractal that is easily computed and yet has an intricate and beautiful structure. It is defined as the set of complex numbers c for which the function fc(z)=z2+c does not diverge when iterated from z=0, i.e., for which the sequence fc(0),fc(fc(0)), etc., remains bounded in absolute value.


> The Mandelbrot set serves as a valuable benchmark for assessing the computational efficiency of programming languages and their implementations. Python, historically considered slower compared to compiled languages like C++, faces several factors that contribute to its performance disparity. Python's interpreted nature, dynamic typing, and the Global Interpreter Lock (GIL) can impact its execution speed for computationally intensive tasks. However, recent advancements in interpreters, just-in-time (JIT) compilation, and optimized libraries have narrowed the performance gap. Python's emphasis on readability, ease of use, and extensive ecosystem has made it a popular language despite the trade-off in raw execution speed, while its integration with high-performance libraries written in C or C++ provides avenues for optimizing critical computations.



### **Test Machine Specs.**
```bash
OS: macOS 13.4 22F66 x86_64
Host: MacBookPro15,1
Kernel: 22.5.0
Uptime: 3 days, 17 hours, 27 mins
Packages: 35 (brew)
Shell: zsh 5.9
Resolution: 1680x1050
DE: Aqua
WM: Rectangle
Terminal: iTerm2
Terminal Font: MesloLGS-NF-Regular 13
CPU: Intel i7-8750H (12) @ 2.20GHz
GPU: Intel UHD Graphics 630, Radeon Pro 555X
Memory: 17491MiB / 32768MiB
```


* 🐍 Python `version 3.11.3`
* 🍎 Clang `version 14.0.3 (clang-1403.0.22.14.1)`