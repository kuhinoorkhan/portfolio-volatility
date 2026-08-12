#include <cmath>

extern "C" float calculate_volatility(const float* returns, int size) {
    float sum = 0.0f, var = 0.0f;
    for (int i = 0; i < size; ++i) sum += returns[i];
    float mean = sum / size;
    for (int i = 0; i < size; ++i) var += (returns[i] - mean) * (returns[i] - mean);
    return std::sqrt(var / size);
}
