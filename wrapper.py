import os
import rpy2.robjects as ro

# Set R path (important for Windows)
os.environ['R_HOME'] = r"C:\Program Files\R\R-4.5.3"
os.environ['PATH'] += r";C:\Program Files\R\R-4.5.3\bin\x64"

# Load R package
ro.r('library(RobStatTM)')


def loc_scale_m(data):
    """
    Compute robust location and scale using RobStatTM

    Parameters:
        data (list): Numeric values

    Returns:
        list: [location, scale, extra value]
    """
    ro.globalenv['x'] = ro.FloatVector(data)
    result = ro.r('locScaleM(x)')
    
    return [float(val[0]) for val in result]


def scale_m(data):
    """
    Compute robust scale using RobStatTM

    Parameters:
        data (list): Numeric values

    Returns:
        float: scale value
    """
    ro.globalenv['x'] = ro.FloatVector(data)
    result = ro.r('scaleM(x)')
    
    return float(result[0])
