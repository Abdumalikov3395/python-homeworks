import numpy as np

# 51
dtype = [('position', [('x', float), ('y', float)]),
         ('color', [('r', int), ('g', int), ('b', int)])]

data = np.array([
    ((1.0, 2.0), (255, 0, 0)),
    ((3.5, 4.5), (0, 255, 0)),
    ((5.2, 1.2), (0, 0, 255))
], dtype=dtype)

print(data)

# 52
points = np.random.rand(100, 2)

# Calculate pairwise distances manually
diffs = points[:, np.newaxis, :] - points[np.newaxis, :, :]
distances = np.sqrt(np.sum(diffs**2, axis=-1))

print(distances.shape)  # Output: (100, 100)

# 53

arr=np.array([1.2,2.3,3.4], dtype=np.float32)
arr_int=arr.astype(np.int32)
print(arr_int.dtype)

# 54
with open("vf.txt", mode="r") as file:
    a=file.read()
b=a.split("\n")
c=[i.split(",") for i in b]
e = [[int(el.strip()) if el.strip() else 0 for el in row] for row in c]
num1=np.array(e)
print(num1)

# 55 Answer: np.ndenumerate

# 56 ----

# 57. How to randomly place p elements in a 2D array?
p = 5
array = np.zeros((5, 5))
indices = np.random.choice(array.size, p, replace=False)
np.put(array, indices, 1)
print("57. Randomly placed elements in 2D array: ", array)

# 58. Subtract the mean of each row of a matrix
matrix = np.random.rand(4, 4)
row_mean = matrix.mean(axis=1, keepdims=True)
matrix_centered = matrix - row_mean
print("58. Matrix with mean subtracted from each row: ", matrix_centered)

# 59. How to sort an array by the nth column?
matrix = np.random.rand(4, 4)
sorted_matrix = matrix[matrix[:, 1].argsort()]
print("59. Matrix sorted by the nth column: ", sorted_matrix)

# 60. How to tell if a given 2D array has null columns?
matrix = np.array([[1, 2, 0], [4, 5, 6], [7, 8, 9]])
null_columns = np.any(matrix == 0, axis=0)
print("60. Null columns in the matrix: ", null_columns)

# 61. Find the nearest value from a given value in an array
arr = np.array([1, 2, 3, 4, 5])
value = 3.6
nearest_value = arr[np.abs(arr - value).argmin()]
print("61. Nearest value: ", nearest_value)

# 62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator?
A = np.array([[1, 2, 3]])
B = np.array([[1], [2], [3]])
sum_result = np.add(A, B)
print("62. Sum using iterator: ", sum_result)

# 63. Create an array class that has a name attribute
class NamedArray(np.ndarray):
    def __new__(cls, shape, dtype=float, name="Unnamed"):
        obj = super(NamedArray, cls).__new__(cls, shape, dtype)
        obj.name = name
        return obj

arr = NamedArray((3, 3), name="MyArray")
print("63. Named array: ", arr, "Name: ", arr.name)

# 64. How to add 1 to each element indexed by a second vector (careful with repeated indices)?
arr = np.array([0, 1, 2, 3])
indices = np.array([0, 2, 2])
arr[indices] += 1
print("64. Array with added values: ", arr)

# 65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)?
X = np.array([1, 2, 3])
F = np.zeros(4)
I = np.array([0, 1, 3])
np.add.at(F, I, X)
print("65. Accumulated array: ", F)

# 66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors
image = np.random.randint(0, 256, (4, 4, 3), dtype=np.uint8)
unique_colors = len(np.unique(image.reshape(-1, 3), axis=0))
print("66. Number of unique colors: ", unique_colors)

# 67. Considering a four dimensions array, how to get sum over the last two axis at once?
arr = np.random.rand(4, 4, 4, 4)
sum_result = arr.sum(axis=(-2, -1))
print("67. Sum over the last two axes: ", sum_result)

# 68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset indices?
D = np.array([1, 2, 3, 4, 5])
S = np.array([0, 0, 1, 1, 1])
means = [D[S == i].mean() for i in np.unique(S)]
print("68. Means of subsets: ", means)

# 69. How to get the diagonal of a dot product?
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
dot_product = np.dot(A, B)
diagonal = np.diag(dot_product)
print("69. Diagonal of the dot product: ", diagonal)

# 70. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value?
arr = np.array([1, 2, 3, 4, 5])
result = np.zeros(len(arr) + 4)
result[::4] = arr
print("70. Interleaved zeros array: ", result)

# 71. Consider an array of dimension (5,5,3), how to multiply it by an array with dimensions (5,5)?
arr_3d = np.random.rand(5, 5, 3)
arr_2d = np.random.rand(5, 5)
result = arr_3d * arr_2d[:, :, None]
print("71. 3D array multiplied by 2D array: ", result)

# 72. How to swap two rows of an array?
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr[[0, 2]] = arr[[2, 0]]
print("72. Swapped rows: ", arr)

# 73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the triangles
triplets = np.array([[0, 1, 2], [1, 2, 3], [2, 3, 4], [0, 1, 2], [1, 2, 3]])
line_segments = np.unique(np.sort(triplets[:, None, :], axis=-1), axis=0)
print("73. Unique line segments: ", line_segments)

# 74. Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C?
C = np.array([2, 3, 1])
A = np.repeat(np.arange(len(C)), C)
print("74. Array A from bincount: ", A)

# 75. How to compute averages using a sliding window over an array?
arr = np.array([1, 2, 3, 4, 5, 6, 7])
window_size = 3
avg = np.convolve(arr, np.ones(window_size)/window_size, mode='valid')
print("75. Sliding window average: ", avg)

# 76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z[0],Z[1],Z[2]) and each subsequent row is shifted by 1
Z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
result = np.array([Z[i:i+4] for i in range(len(Z)-3)])
print("76. Shifted 2D array: ", result)

import numpy as np

# 77. How to get the first non-zero value in a 2D array?
arr = np.array([[0, 0, 3], [0, 4, 0], [5, 0, 0]])
first_non_zero = arr[arr != 0][0]
print("77. First non-zero value: ", first_non_zero)

# 78. How to compute the sum of all columns in a 2D array where each column contains nan values?
arr = np.array([[1, 2, np.nan], [3, 4, 5], [np.nan, 6, 7]])
sum_columns = np.nansum(arr, axis=0)
print("78. Sum of columns with nan values: ", sum_columns)

# 79. How to find the number of unique values in an array with nan?
arr = np.array([1, 2, np.nan, 2, np.nan, 3])
unique_values = np.unique(arr[~np.isnan(arr)])
print("79. Unique values without nan: ", unique_values)

# 80. How to generate a 2D Gaussian array with specific standard deviation and mean?
mean = 0
std_dev = 1
gaussian_array = np.random.normal(mean, std_dev, (4, 4))
print("80. 2D Gaussian array: ", gaussian_array)

# 81. How to reverse the rows of a 2D array?
arr = np.array([[1, 2], [3, 4], [5, 6]])
reversed_rows = arr[::-1]
print("81. Reversed rows: ", reversed_rows)

# 82. How to create an array where the elements are powers of 2, starting from 2^0 to 2^9?
powers_of_two = np.array([2**i for i in range(10)])
print("82. Powers of 2: ", powers_of_two)

# 83. How to create a matrix with all ones and then replace its diagonal with zeros?
arr = np.ones((4, 4))
np.fill_diagonal(arr, 0)
print("83. Matrix with ones and diagonal zeros: ", arr)

# 84. How to generate a random integer array with values between a given range?
arr = np.random.randint(1, 100, size=(5, 5))
print("84. Random integer array: ", arr)

# 85. How to find the unique rows in a 2D array?
arr = np.array([[1, 2], [3, 4], [1, 2], [5, 6]])
unique_rows = np.unique(arr, axis=0)
print("85. Unique rows: ", unique_rows)

# 86. How to find the indices of the maximum value in a 2D array?
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices_of_max = np.unravel_index(np.argmax(arr), arr.shape)
print("86. Indices of max value: ", indices_of_max)

# 87. How to sort an array by the nth column?
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sorted_by_column = arr[arr[:, 1].argsort()]
print("87. Sorted by nth column: ", sorted_by_column)

# 88. How to compute the running sum of a 1D array?
arr = np.array([1, 2, 3, 4])
running_sum = np.cumsum(arr)
print("88. Running sum: ", running_sum)

# 89. How to reshape a 1D array into a 2D array with a specific shape?
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
print("89. Reshaped array: ", reshaped_arr)

# 90. How to remove all rows in a 2D array that contain zeros?
arr = np.array([[1, 0], [2, 3], [4, 5], [0, 6]])
arr_no_zeros = arr[~np.any(arr == 0, axis=1)]
print("90. Array without rows containing zeros: ", arr_no_zeros)

# 91. How to create a 2D matrix with random numbers between 0 and 1?
arr = np.random.rand(3, 3)
print("91. 2D random matrix: ", arr)

# 92. How to compute the pairwise distances between rows of a matrix?
from scipy.spatial.distance import pdist, squareform
arr = np.array([[1, 2], [3, 4], [5, 6]])
pairwise_distances = pdist(arr)
print("92. Pairwise distances: ", pairwise_distances)

# 93. How to compute the element-wise product of two arrays?
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
product = np.multiply(arr1, arr2)
print("93. Element-wise product: ", product)

# 94. How to create an identity matrix?
identity_matrix = np.eye(4)
print("94. Identity matrix: ", identity_matrix)

# 95. How to compute the dot product of two 2D arrays?
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
dot_product = np.dot(arr1, arr2)
print("95. Dot product: ", dot_product)

# 96. How to subtract the row mean from each element of the matrix?
arr = np.random.rand(4, 4)
row_mean = arr.mean(axis=1, keepdims=True)
mean_subtracted = arr - row_mean
print("96. Row mean subtracted: ", mean_subtracted)

# 97. How to add a new row to an existing 2D array?
arr = np.array([[1, 2], [3, 4]])
new_row = np.array([5, 6])
arr_with_new_row = np.vstack([arr, new_row])
print("97. Array with new row: ", arr_with_new_row)

# 98. How to add a new column to an existing 2D array?
arr = np.array([[1, 2], [3, 4]])
new_column = np.array([5, 6])
arr_with_new_column = np.column_stack([arr, new_column])
print("98. Array with new column: ", arr_with_new_column)

# 99. How to create a 3D array from two 2D arrays?
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr_3d = np.array([arr1, arr2])
print("99. 3D array from two 2D arrays: ", arr_3d)


