# density_extractor.py

import numpy as np
from PIL import Image

import colorbar_mapping as cmap


def extract_density_to_csv(
    image_file,
    cbar_img_file,        
    plot_box,
    cbar_box,
    cValues,        
    x_range,
    y_range,
    output_csv,
    orientation="vertical"
    ):
    """
    Extract a 2D density field from a plot image and save as CSV.

    Parameters
    ----------
    image_file : str
        Path to the image containing density plot.
    cbar_img_file : str
        Path to the image containing colorbar image.    
    plot_box : tuple (left, right, top, bottom)
        Pixel coordinates of the density plot region.
    cbar_box : tuple (left, right, top, bottom)
        Pixel coordinates of the colorbar region.
    cValues : float tuple (cvmin, cvmax)
        cvmin : float
            Minimum value on the colorbar.
        cvmax : float
            Maximum value on the colorbar.    
    x_range : tuple (x_min, x_max)
        Physical x-axis limits.
    y_range : tuple (y_min, y_max)
        Physical y-axis limits.
    output_csv : str
        Output CSV filename.
    orientation : str
        'vertical' or 'horizontal' colorbar.
    """

    # -------------------------------------------------
    # Load image
    # -------------------------------------------------
    img = Image.open(image_file).convert("RGB")
    img_np = np.array(img)

    # -------------------------------------------------
    # Crop density plot
    # -------------------------------------------------
    left, right, top, bottom = plot_box
    plot_img = img_np[top:bottom, left:right]

    if plot_img.size == 0:
        raise ValueError("Plot crop box is empty or invalid.")

    ny, nx, _ = plot_img.shape

    # -------------------------------------------------
    # Load colorbar mapping 
    # -------------------------------------------------
    cbar_values, tree = cmap.colorbar_mapping(
        cbar_img_file,
        cbar_box,
        cValues,        
        orientation=orientation
    )

    # -------------------------------------------------
    # MAP PLOT COLORS to SCALAR VALUES
    # -------------------------------------------------
    flat_plot = plot_img.reshape(-1, 3)
    _, idx = tree.query(flat_plot)
    data = cbar_values[idx].reshape(ny, nx)

    # -------------------------------------------------
    # BUILD PHYSICAL COORDINATES
    # -------------------------------------------------
    x_min, x_max = x_range
    y_min, y_max = y_range

    xCoords = np.linspace(x_min, x_max, nx)
    yCoords = np.linspace(y_max, y_min, ny)  # image y-axis is inverted

    # make meshgrid
    X, Y = np.meshgrid(xCoords, yCoords)

    # -------------------------------------------------
    # SAVE CSV into row-major format
    # -------------------------------------------------
    np.savetxt(
        output_csv,
        np.column_stack([X.ravel(), Y.ravel(), data.ravel()]),
        delimiter=",",
        header="'x','y','densityValue'",
        comments=""
    )

