import numpy as np
import matplotlib.pyplot as plt

from densityPlot_extractor import extract_density_to_csv


def linePlotData_harvester(
        image_file,
        cbar_file,
        plot_box,
        cbar_box,
        cValues,
        x_range,
        y_range,
        output_csv,
        slice_axis,
        slice_coord,                        
        orientation = 'vertical'
):
    """
        Generate a 1D slice plot from a density plot image via an intermediate 2D CSV.

        Parameters
        ----------
        image_file : str
            Path to density plot image.
        cbar_file : str
            Path to the image containing colorbar image.    
        plot_box : tuple (left, right, top, bottom)
            Pixel coordinates of density plot.
        cbar_box : tuple (left, right, top, bottom)
            Pixel coordinates of colorbar.
        cValues : float tuple (cvmin, cvmax)
            cvmin : float
                Minimum value on the colorbar.
            cvmax : float
                Maximum value on the colorbar.    
        x_range : tuple (x_min, x_max)
            Physical x-axis range.
        y_range : tuple (y_min, y_max)
            Physical y-axis range.
        output_csv : str
            Temporary CSV file for 2D density data.
        slice_axis : str
            'x' or 'y'
        slice_coord : float
            Physical coordinate of the slice.
        orientation : str
           'vertical' or 'horizontal' colorbar.

        Returns
        -------
        coord, lineDataArray : line plot data arrays
    """

# -------------------------------------------------
#  extract 2D density plot and save as CSV
# -------------------------------------------------
    extract_density_to_csv(
        image_file,
        cbar_file,
        plot_box,
        cbar_box,
        cValues,
        x_range,
        y_range,
        output_csv,
        orientation
    )

# -------------------------------------------------
# load 2D CSV and prepare coordinates arrays
# -------------------------------------------------
    data = np.loadtxt(output_csv, delimiter=",", skiprows=1)

    x_all = data[:, 0]
    y_all = data[:, 1]
    val_all = data[:, 2]

    x_min, x_max = x_range
    y_min, y_max = y_range

    # number of grid point of x
    nx = int(round(len(x_all) / len(np.unique(y_all))))
    # number of grid point of y    
    ny = int(round(len(y_all) / len(np.unique(x_all))))

    xArray = np.linspace(x_min, x_max, nx)
    yArray = np.linspace(y_max, y_min, ny)   # same convention as extraction

# -------------------------------------------------
# Extract 1D slice
# -------------------------------------------------
    if slice_axis == "y":
        yIndex = int(round(((slice_coord - yArray[0]) / (yArray[-1] - yArray[0])) * (ny - 1)))
       
        # out of boud controling
        yIndex = np.clip(yIndex, 0, ny - 1)

        start = yIndex * nx
        end = start + nx

        coord = xArray
        lineDataArray = val_all[start:end]
    elif slice_axis == "x":
        xIndex = int(round((slice_coord - xArray[0]) / (xArray[-1] - xArray[0]) * (nx - 1)))

        # out of boud controling
        xIndex = np.clip(xIndex, 0, nx - 1)

        coord = yArray
        lineDataArray = val_all[xIndex::nx]
    else:
        raise ValueError("slice_axis must be 'x' or 'y'")

    return coord, lineDataArray

