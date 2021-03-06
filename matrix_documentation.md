# Matrix Documentation

A matrix class object admits as its sole argument a string whose regex expression looks like this:
```regex
\[((\[(?:\s*(?:-?'\d+\.\d+|-?\d)\s*)+\])\s*;?)\]
```
For example, a vector would look something like this:
> [[1 2 3]; [4 5 6]; [3 2 1]]

or some thing like this
> [[1.0 2.0 3.0]; [7.0 1 2.3]; [4 8 0.0]]
---
**NOTE**: The matrix class is comprised of vector objects.
## Class Functions Documentation

- ```python
    def __init__(self, string)
    ```
    - **Purpose**: Constructor
    - **Precondition**: Create a matrix object
    - **Post-condition**: Matrix object is created

- ```python
    def __str__(self)
    ```
    - **Purpose**: Overload the \_\_str\_\_ operator
    - **Precondition**: Matrix object must exist and the inserted string must conform the regex for the matrix class
    - **Post-condition**: The row vectors of the matrix will be printed thus printing the matrix in the correct orientation

- ```python
    def __add__(self, RightMatrix)
    ```
    - **Purpose**: Adds two matrix objects
    - **Precondition**: The thing in _RightMatrix_ must be a matrix object
    - **Post-condition**: A matrix object containing the sum of the elements of both matrix is returned

- ```python
    def __sub__(self,RightMatrix)
    ```
    - **Purpose**: Subtracts two matrix objects
    - **Precondition**: The thing in _RightMatrix_ must be a matrix object
    - **Post-condition**: A matrix object containing the difference of the elements of both matrix is returned

- ```python
    def scalar_multiplication(self, multiplier)
    ```
    - **Purpose**: Do the scalar multiplication of the matrix object
    - **Precondition**: Matrix object must exist
    - **Post-condition**: Returns a vector object containing the _self.elems_ of the row vectors scalar multiplied

- ```python
    def cross_product(self, rightMat)
    ```
    - **Purpose**: Do the cross product of _self_ object with another vector. For example, self.cross_product(B) means _**AB**_
    - **Precondition**: Matrix object must exist and _rightMat_ must also be a matrix object
    - **Post-condition**: A matrix object containing the cross product of two matrices is returned. If _self.numOfRows_ does not equal _rightMat.numOfRows_  

- ```python
    def transpose(self)
    ```
    - **Purpose**: Get the transpose of _self_
    - **Precondition**: Matrix object must exist
    - **Post-condition**:  A matrix object containing the transpose, meaning the rows become columns and columns become rows, of _self_ is returned

- ```python
    def det(self)
    ```
    - **Purpose**: Returns the determinant of _self_
    - **Precondition**: Matrix object must exist
    - **Post-condition**: The determinant of _self_ is returned as a float, If _self.isSqaure_ is set to false, the function will return _None_   

- ```python
    def inv(self)
    ```
    - **Purpose**: Returns the inverse of _self_ matrix object
    - **Precondition**: Matrix object must exist
    - **Post-condition**: A matrix object containing the inverse of _self_ is returned. If _self.isSquare_ is set to false, the function will return _None_   

- ```python
    def adjugate(self)
    ```
    - **Purpose**: Returns the adjugate of _self_ matrix object
    - **Precondition**: Matrix object must exist
    - **Post-condition**: A matrix object containing the adjugate of _self_ is returned. f _self.isSquare_ is set to false, the function will return _None_   

- ```python
    def __inv_and_adjugate__(self,det)
    ```
    - **Purpose**: Used for calculating inverse and adjugate functions, no intended for use.
    - **Post-condition**: A matrix whose elements are replaced by the determinant of their co-factors divided by the _det_ parameter is returned 

- ```python
    def rec_det(mat)
    ```
    - **Purpose**: Helper function that calculates the determinant of matrix _mat_. Not intended for use
    - **Precondition**: The _mat_ parameter must be a list of lists containing float or int values
    - **Post-condition**: The determinant of _mat_ is returned as a float value

- ```python
    @staticmethod
    def not_in_row_or_column(mat,size,target_row,target_column)
    ```
    - **Purpose**: Returns the co-factors of a element in position [_target_row_][_target_column_] in the matrix _mat_ of length _size_. Not intended for use.
    - **Precondition**: A list of list containing float values must be passed as _mat_, size must be the amount of lists in _mat_ and _target_row_ and _target_column_ must be in range of _mat_.
    - **Post-condition**: A list of list containing float values of the co-factors of the target are returned.

- ```python
    @staticmethod
    def FormatColumnVectors(string)
    ```
    - **Purpose**: Return a string that removes commas and single quotes from _string_. Used for formatting vector objects
    - **Post-condition**: A string that removes commas and single quotes from _string_ is returned

- ```python
    @staticmethod
    def appendZeroes(vec,initialSize ,maxColumnSize)
    ```
    - **Purpose**: Add _maxColumnSize_ minus _initial_size_ amount of zeroes to list _vec_
    - **Precondition**: _vec_  must be a list and _initial_size_ must be less than or equal to _maxColumnSize_
    - **Post-condition**: _vec_ will have been the difference of _maxColumnSize_ and _initialSize_ of zeroes appended

- ```python
    @staticmethod
    def formatList(vecList)
    ```
    - **Purpose**: Returns a string formatted in the form required by matrix class regex
    - **Precondition**: _veclist_ must be a list of vector objects
    - **Post-condition**: A string that is matrix class regex complaint is returned

- ```python
    @staticmethod
    def star(mat)
    ```
    - **Purpose**: Returns the list of lists of floats created by the co-factors of the corresponding elements transposed
    - **Precondition**: _mat_ must be a list of lists of floats
    - **Post-condition**: Returns the star matrix