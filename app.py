import ctypes
import os

# Load compiled C++ library
lib_path = os.path.abspath("./calculator.so")
lib = ctypes.CDLL(lib_path)

# Configure argument and return types
lib.calculate_volatility.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]
lib.calculate_volatility.restype = ctypes.c_float

# Sample daily return percentages (%)
returns = [1.2, -0.5, 2.1, 0.8, -1.0]
c_arr = (ctypes.c_float * len(returns))(*returns)

# Execute C++ volatility calculation
volatility = lib.calculate_volatility(c_arr, len(returns))
print(f"Daily Portfolio Volatility: {volatility:.2f}%")
