# Scientific Calculator
# Description: Design a calculator for scientific computations with classes for different types of calculations (e.g., algebra, trigonometry, statistics).
# Key Features:
# Use NumPy for mathematical functions like sine, cosine, and logarithms.
# Define classes like AlgebraCalculator, TrigCalculator.
# Extend functionality with modular design.
# Skills Gained:
# OOP for extensibility.
# NumPy for mathematical operations.

import numpy as np

class ScientificCalculator:
    @staticmethod
    def start():
        print("Scientific Calculator Initialized")
class AlgebraCalculator(ScientificCalculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
class TrigCalculator(ScientificCalculator):
    def sine(self, angle_rad):
        return np.sin(angle_rad)

    def cosine(self, angle_rad):
        return np.cos(angle_rad)

    def tangent(self, angle_rad):
        return np.tan(angle_rad)
class StatisticsCalculator(ScientificCalculator):
    def mean(self, data):
        return np.mean(data)

    def median(self, data):
        return np.median(data)

    def std_dev(self, data):
        return np.std(data)
if __name__ == "__main__":
    # Algebra Calculator
    algebra = AlgebraCalculator()
    print("Addition:", algebra.add(10, 5))
    print("Division:", algebra.divide(10, 2))
    
    # Trigonometry Calculator
    trig = TrigCalculator()
    print("Sine of 45 degrees:", trig.sine(np.radians(45)))
    print("Cosine of 90 degrees:", trig.cosine(np.radians(90)))

    # Statistics Calculator
    stats = StatisticsCalculator()
    data = [1, 2, 3, 4, 5]
    print("Mean:", stats.mean(data))
    print("Standard Deviation:", stats.std_dev(data))
    
