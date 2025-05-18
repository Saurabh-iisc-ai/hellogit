import os
import cv2
import numpy as np
from tqdm import tqdm



# Example usage:
# compare_images_pixelwise('path/to/folder1', 'path/to/folder2')


import os
import cv2
import numpy as np
from tqdm import tqdm

def compare_images_pixelwise(folder1, folder2, every_nth_image=1):
    files1 = sorted([f for f in os.listdir(folder1) if f.endswith('.png')])
    files2 = sorted([f for f in os.listdir(folder2) if f.endswith('.png')])
    
    results = []
    
    # Ensure we only iterate over the minimum length to avoid index errors
    num_pairs = min(len(files1), len(files2))
    
    for index in tqdm(range(num_pairs), desc="Comparing image pairs pixelwise"):
        if index % every_nth_image != 0:
            continue

        file1 = files1[index]
        file2 = files2[index]
        path1 = os.path.join(folder1, file1)
        path2 = os.path.join(folder2, file2)
        
        image1 = cv2.imread(path1, cv2.IMREAD_UNCHANGED)
        image2 = cv2.imread(path2, cv2.IMREAD_UNCHANGED)
        
        if image1 is None:
            print(f"Error: Image not found at {path1}")
            results.append("error")
            continue
        if image2 is None:
            print(f"Error: Image not found at {path2}")
            results.append("error")
            continue
        
        if np.array_equal(image1, image2):
            results.append("same")
        else:
            results.append("different")
    
    print(results)
    return results

# Example usage:
#compare_images_pixelwise(r'C:\Users\SAUSHRI\Downloads\7files', r'C:\Users\SAUSHRI\Downloads\AlgoVisual_10bit_pngs\AlgoVisual_10bit_pngs')
def compare_images_with_stats(folder1, folder2, every_nth_image=1):
    """
    Compares corresponding PNG images in two folders by computing mean and median intensities,
    and determines if the images are the same (pixel-wise identical) or different.

    Parameters:
        folder1 (str): Path to the first folder containing PNG images.
        folder2 (str): Path to the second folder containing PNG images.
        every_nth_image (int): Process every nth image for comparison.

    Returns:
        results (list of dict): Each dictionary contains:
            - pair: Pair number (starting at 1)
            - image1: Filename from folder1
            - mean1: Mean intensity of image1
            - median1: Median intensity of image1
            - image2: Filename from folder2
            - mean2: Mean intensity of image2
            - median2: Median intensity of image2
            - status: "same" if images are pixel-wise identical, "different" otherwise
    """
    files1 = sorted([f for f in os.listdir(folder1) if f.endswith('.png')])
    files2 = sorted([f for f in os.listdir(folder2) if f.endswith('.png')])
    
    results = []
    num_pairs = min(len(files1), len(files2))
    pair_number = 1

    for index in tqdm(range(num_pairs), desc="Comparing image pairs"):
        if index % every_nth_image != 0:
            continue
        
        file1 = files1[index]
        file2 = files2[index]
        path1 = os.path.join(folder1, file1)
        path2 = os.path.join(folder2, file2)
        
        # Load the images preserving the original bit depth (e.g., 10-bit images)
        image1 = cv2.imread(path1, cv2.IMREAD_UNCHANGED)
        image2 = cv2.imread(path2, cv2.IMREAD_UNCHANGED)
        print(image1[0:5,0:5])
        print(image2[0:5,0:5])
        ee
        
        if image1 is None:
            print(f"Error: Unable to load {file1} from {folder1}")
            continue
        if image2 is None:
            print(f"Error: Unable to load {file2} from {folder2}")
            continue
        
        # Calculate mean and median intensities for both images
        mean1 = np.mean(image1)
        median1 = np.median(image1)
        mean2 = np.mean(image2)
        median2 = np.median(image2)
        
        # Determine if the two images are pixel-wise identical
        status = "same" if np.array_equal(image1, image2) else "different"
        
        # Store the result for this pair
        results.append({
            "pair": pair_number,
            "image1": file1,
            "mean1": mean1,
            "median1": median1,
            "image2": file2,
            "mean2": mean2,
            "median2": median2,
            "status": status
        })
        
        pair_number += 1

    # Print results in a neat table-like format
    print("{:<6} {:<15} {:<10} {:<10} {:<15} {:<10} {:<10} {:<10}".format(
        "Pair", "Image1", "Mean1", "Median1", "Image2", "Mean2", "Median2", "Status"
    ))
    print("-" * 90)
    for r in results:
        print("{:<6} {:<15} {:<10.2f} {:<10.2f} {:<15} {:<10.2f} {:<10.2f} {:<10}".format(
            r["pair"], r["image1"], r["mean1"], r["median1"],
            r["image2"], r["mean2"], r["median2"], r["status"]
        ))
    
    return results

# Example usage:
results = compare_images_with_stats(r'C:\Users\SAUSHRI\Downloads\7files', r'C:\Users\SAUSHRI\Downloads\AlgoVisual_10bit_pngs\AlgoVisual_10bit_pngs')