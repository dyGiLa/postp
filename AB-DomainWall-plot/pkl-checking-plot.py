import pickle
import numpy as np
import matplotlib.pyplot as plt

# Function to load the pickle file
def load_pickle_file(file_path):
    """Load a pickle file and return the data."""
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

# Function to process the data for plotting
def process_data(data):
    """Extract and return the necessary data for plotting."""
    if not data:
        return None, None, None

    grid_data = data['grid']
    x = grid_data['x']  # Grid for x > 0
    x_minus = grid_data['x_minus']  
    x_minus = -np.abs(x_minus[1:])  # x-coords for x<0

    print(x)
    print(x_minus)
    
    x_arr = np.concatenate((x_minus, x))
    x_arr = np.sort(x_arr)
    
    #x_array = np.concatenate((x_minus, x))  # Combining x <0 and x>0 grids
    
    A = data['A']  # The solution matrix

    # Extract the real part of A
    A_real = [np.real(matrix) for matrix in A]
    # Extract the img part of A
    A_img = [np.imag(matrix) for matrix in A]
    
    return x_arr[::2]*0.5, np.array(A_real), np.array(A_img)

# Function to plot the data
def plot_pde_solution(x, A_real, A_img):

    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    # Plot the real part of A for the positive side of the grid (x > 0)
    ax.plot(x, A_real[:, 0, 0], label=fr"$ReA_{{11}}$ from Mark", color='blue')
    ax.plot(x, A_real[:, 1, 1], label=fr"$ReA_{{22}}$ from Mark", color='green')
    ax.plot(x, A_real[:, 2, 2], label=fr"$ReA_{{33}}$ from Mark", color='red')

    ax.plot(x, A_img[:, 0, 1], label=fr"$ImA_{{12}}$ from Mark", color='orange')
    ax.plot(x, A_img[:, 1, 0], label=fr"$ImA_{{21}}$ from Mark", color='cyan')
    
    ax.set_title(fr"$ReA_{{\alpha i}}$ and $ReA_{{\alpha i}}$ from Diffenet Solvers")
    ax.set_xlabel('x')
    ax.set_ylabel('Real(A)')
    ax.legend()

    plt.tight_layout()
    plt.show()

def main():
    # Load the data from the pickle file
    file_path = 'AB_wall_data_p28.pkl'  # Replace with your actual pickle file path
    data = load_pickle_file(file_path)

    # Process the data to extract the necessary arrays
    x_arr, A_real, A_img = process_data(data)

    print(x_arr)
    print(A_real)
    print(x_arr.shape)    
    print(A_real.shape)

    # Step 3: Plot the data
    plot_pde_solution(x_arr, A_real, A_img)

if __name__ == "__main__":
    main()
