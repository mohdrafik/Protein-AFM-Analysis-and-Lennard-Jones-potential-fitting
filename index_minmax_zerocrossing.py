import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def analyze_force(distance_sliced, force):
    # Find the index and value of the maximum force

    # distance_sliced = pd.DataFrame(distance_sliced)
    distance_sliced.reset_index(drop=True, inplace=True)

    max_index = np.argmax(force)
    max_value = force[max_index]

    # Find the index and value of the minimum force
    min_index = np.argmin(force)
    min_value = force[min_index]

    # Ensure max occurs before min
    if max_index > min_index:
        raise ValueError("Max value occurs after min value, which is unexpected.")

    # Find the index and value where the force first crosses zero before the min value
    zero_cross_index = np.where(np.diff(np.signbit(force)))[0]
    zero_cross_index = zero_cross_index[zero_cross_index < min_index][0]
    zero_cross_value = force[zero_cross_index]

    # Plot the force vs. distance_sliced
    plt.figure(figsize=(10, 6))
    plt.plot(distance_sliced, force, label='Force vs. Distance')
    plt.scatter(distance_sliced[max_index], max_value, color='red', zorder=5, label='Max Force')
    plt.scatter(distance_sliced[min_index], min_value, color='blue', zorder=5, label='Min Force')
    plt.scatter(distance_sliced[zero_cross_index], zero_cross_value, color='green', zorder=5, label='Zero Cross Force')
    plt.xlabel('Distance')
    plt.ylabel('Force')
    plt.title('Force vs. Distance with Key Points')
    plt.legend()
    plt.show()

    return {
        "max_value": max_value,
        "max_index": max_index,
        "min_value": min_value,
        "min_index": min_index,
        "zero_cross_value": zero_cross_value,
        "zero_cross_index": zero_cross_index
    }

# Example usage
if __name__ == "__main__":
    # Replace these arrays with your actual data
    distance_sliced = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    force = np.array([0, 2, 4, 3, 1, -1, -3, -5, -4, -2, 0])

    results = analyze_force(distance_sliced, force)
    print("Results:", results)
