import numpy as np
from PIL import Image
from scipy.spatial import cKDTree


def colorbar_mapping(
    image_file,
    cbar_box,
    cValues,    
    orientation="vertical"        
    ):
    """
    Build a color -> value mapping from a colorbar image.

    Parameters
    ----------
    image_file : str
        Path to image containing the colorbar.
    cbar_box : tuple (left, right, top, bottom)
        Pixel coordinates defining the colorbar region.
    cValues : float tuple (cvmin, cvmax)
        cvmin : float
            Minimum value on the colorbar.
        cvmax : float
            Maximum value on the colorbar.
    orientation : str
        'vertical' or 'horizontal'

    Returns
    -------
    cbar_values : ndarray (N,)
        Numerical values corresponding to colorbar colors.
    tree : cKDTree
        KD-tree for fast RGB -> value lookup.
    """

    # ---------------------------------------
    # color bar picture RGB data preparation
    # ---------------------------------------    

    img = Image.open(image_file).convert("RGB")
    img_np = np.array(img) #convert RGB to np.array

    # crop the picture RGB array 
    left, right, top, bottom = cbar_box
    cbar_img = img_np[top:bottom, left:right]

    if cbar_img.size == 0:
        raise ValueError("Colorbar crop box is empty or invalid.")

    # ---------------------------------------    
    # Extract representative colors
    # ---------------------------------------    
    vmin, vmax = cValues
    
    if orientation == "vertical":
        # Average over width → one RGB per vertical pixel
        cbar_rgb = np.mean(cbar_img, axis=1)

        # Top = vmax, bottom = vmin
        n = cbar_rgb.shape[0]
        cbar_values = np.linspace(vmax, vmin, n)

    elif orientation == "horizontal":
        # Average over height → one RGB per horizontal pixel
        cbar_rgb = np.mean(cbar_img, axis=0)

        # Left = vmin, right = vmax
        n = cbar_rgb.shape[0]
        cbar_values = np.linspace(vmin, vmax, n)

    else:
        raise ValueError("orientation must be 'vertical' or 'horizontal'")

    # Build fast nearest-neighbor lookup in RGB space
    tree = cKDTree(cbar_rgb)

    return cbar_values, tree


