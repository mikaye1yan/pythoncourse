def reverse_image(image):
    return [list(map(lambda pixel: 1 - pixel, row)) for row in image]
print(reverse_image([
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1]
])) 
print(reverse_image([
  [1, 1, 1],
  [0, 0, 0]
])) 
print(reverse_image([
  [1, 0, 0],
  [1, 0, 0]
])) 