import unittest
import numpy as np
from chromotools.module import morphological_filter

class TestMorphologicalFilter(unittest.TestCase):
    def test_median_filter(self):
        # Test case for median filter
        image = np.random.rand(100, 100, 3)  # Example RGB image
        filtered_image = morphological_filter(image, filter_type='median')
        self.assertEqual(filtered_image.shape, (100, 100))  # Ensure output shape is grayscale

        # Additional assertions based on expected behavior of median filter
        self.assertTrue(np.min(filtered_image) >= 0)
        self.assertTrue(np.max(filtered_image) <= 1)

    def test_gaussian_filter(self):
        # Test case for Gaussian filter
        image = np.random.rand(100, 100, 3)  # Example RGB image
        filtered_image = morphological_filter(image, filter_type='gaussian', sigma=1.5)
        self.assertEqual(filtered_image.shape, (100, 100))  # Ensure output shape is grayscale

        # Additional assertions based on expected behavior of Gaussian filter
        self.assertTrue(np.min(filtered_image) >= 0)
        self.assertTrue(np.max(filtered_image) <= 1)

    def test_gamma_correction(self):
        # Test case for gamma correction filter
        image = np.random.rand(100, 100, 3)  # Example RGB image
        filtered_image = morphological_filter(image, filter_type='gamma', gamma=0.8)
        self.assertEqual(filtered_image.shape, (100, 100))  # Ensure output shape is grayscale

        # Additional assertions based on expected behavior of gamma correction
        self.assertTrue(np.min(filtered_image) >= 0)
        self.assertTrue(np.max(filtered_image) <= 1)

    def test_non_local_mean_filter(self):
        # Test case for non-local mean filter
        image = np.random.rand(100, 100, 3)  # Example RGB image
        filtered_image = morphological_filter(image, filter_type='nonlocal-mean-filter', sigma=0.1)
        self.assertEqual(filtered_image.shape, (100, 100))  # Ensure output shape is grayscale

        # Additional assertions based on expected behavior of non-local mean filter
        self.assertTrue(np.min(filtered_image) >= 0)
        self.assertTrue(np.max(filtered_image) <= 1)

if __name__ == "__main__":
    unittest.main()
