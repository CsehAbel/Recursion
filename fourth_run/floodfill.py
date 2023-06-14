def floodFill(image, sr, sc, newColor):
    # Check if the starting cell already has the new color
    if image[sr][sc] == newColor:
        return image
    
    # Retrieve the old color of the starting cell
    oldColor = image[sr][sc]
    
    # Call the helper function to perform the flood fill
    dfs(image, sr, sc, oldColor, newColor)
    
    return image

def dfs(image, row, col, oldColor, newColor):
    # Check if the current cell is out of bounds or has a different color
    if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != oldColor:
        return
    
    # Update the color of the current cell
    image[row][col] = newColor
    
    # Recursively call the function for the neighboring cells
    dfs(image, row + 1, col, oldColor, newColor)  # Down
    dfs(image, row - 1, col, oldColor, newColor)  # Up
    dfs(image, row, col + 1, oldColor, newColor)  # Right
    dfs(image, row, col - 1, oldColor, newColor)  # Left

image = [[1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
floodFill(image,sr,sc,newColor)
