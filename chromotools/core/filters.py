import numpy as np
from skimage import color, filters, exposure, img_as_float
from skimage.restoration import denoise_nl_means, estimate_sigma
import skimage
import inspect


def get_function_params_with_description(func):
    doc = inspect.getdoc(func)
    params_section = doc.split("Parameters\n")[1].split("Returns")[0]
    return params_section.strip()

median_params_with_description = get_function_params_with_description(filters.median)


def morphological_filter(image: np.ndarray, filter_type: str = 'median', **kwargs) -> np.ndarray:
    """
    Apply a morphological filter to an RGB image.

    Note:
        This function uses the following library versions:
        - numpy: {numpy_version}
        - skimage: {skimage_version}

    Parameters:
        image (np.ndarray):
            The input RGB image.
        filter_type (str):
            The type of filter to apply. Options are 'median', 'gaussian', 'gamma', and 'non-local-mean-filter'. Default is 'median'.
        kwargs:
            Additional arguments to pass to the filter function. Refer to the official documentation of the respective skimage filter for details on these parameters.

    Returns:
        np.ndarray: The filtered image in grayscale.

    Justification:
        This function centralizes the application of various morphological filters, ensuring compatibility with specific versions of numpy and skimage.
        By using this function, you avoid potential incompatibilities and version conflicts when using different filters directly from the skimage package.
        It provides a unified interface for applying different filters, making your code cleaner and more maintainable.

    filters.median parameters:
        {median_params_with_description}
    """

    im = np.uint8(image)
    im = color.rgb2gray(im)

    if filter_type == 'median':
        filtered_image = filters.median(im, **kwargs)
    elif filter_type == 'gaussian':
        filtered_image = filters.gaussian(im, **kwargs)
    elif filter_type == 'gamma':
        filtered_image = exposure.adjust_gamma(im, **kwargs)
    elif filter_type == 'nonlocal-mean-filter':
        im_ = img_as_float(im)
        sigma = kwargs.get('sigma', 0.08)
        noisy = im_ + sigma * np.random.standard_normal(im_.shape)
        noisy = np.clip(noisy, 0, 1)

        patch_size = kwargs.get('patch_size', 5)
        patch_distance = kwargs.get('patch_distance', 6)
        h = kwargs.get('h', 0.6)
        sigma_est = np.mean(estimate_sigma(noisy))

        # Merge patch_kw with default values
        patch_kw = kwargs.get('patch_kw', {})
        patch_kw.setdefault('h', 0.6 * sigma_est)
        patch_kw.setdefault('sigma', sigma_est)
        patch_kw.setdefault('patch_size', patch_size)
        patch_kw.setdefault('patch_distance', patch_distance)
        patch_kw.setdefault('fast_mode', True)

        filtered_image = denoise_nl_means(noisy, **patch_kw)
    else:
        raise ValueError(f"Unsupported filter type: {filter_type}")

    return filtered_image

numpy_version = np.__version__
skimage_version = skimage.__version__

docstring = morphological_filter.__doc__
formatted_docstring = docstring.format(
    numpy_version=numpy_version,
    skimage_version=skimage_version,
    median_params_with_description=median_params_with_description
)
morphological_filter.__doc__ = formatted_docstring
