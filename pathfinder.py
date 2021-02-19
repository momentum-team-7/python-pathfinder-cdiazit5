from PIL import Image

large_mountain = "elevation_large.txt"
small_mountain = "elevation_small.txt"
coordinates = []
# small text is 600 x 600
# test_coordinates = []

# def small_mountain_ele():
with open('elevation_small.txt', "r") as file:
    for line in file.readlines():
        coordinates.append(line.split())
        # for each line we are spliting, and adding to list of lists
    # print(coordinates) 

# small_mountain_ele()

min_elevation = int(min(map(min, coordinates)))
print(min_elevation)

max_elevation = int(max(map(max, coordinates)))
print(max_elevation)

elevation_diff = int((max_elevation)-(min_elevation))
print(elevation_diff)

dimensions_small = len(coordinates), len(coordinates[0])
print (dimensions_small)

def grayscale(elevation, min, max):
    color_value = (((int(elevation) - min_elevation)/(elevation_diff) * 255))
    return (int(color_value), int(color_value), int(color_value))
# func to covert elevation to RBG value

im = Image.new('RGB', (600,600))
im.save('elevation_small.png')
Image.open('elevation_small.png')
print(im.getpixel((4,80)))

for x in range(600):
        for y in range (300):
            im.putpixel((x,y), (210, 100, 170))


# for x in range(600):
#         for y in range (600):
#             im.putpixel((x,y), grayscale(coordinates[x][y], min_elevation, max_elevation))










# with open('testgrid.txt', "r") as file:
#     for line in file.readlines():
#         test_coordinates.append(line.split())
#         # for each line we are spliting, and adding to list of lists
#     # print(test_coordinates) 

# min_testelevation = int(min(map(min, test_coordinates)))
# max_testelevation = int(max(map(max, test_coordinates)))
# print(min_testelevation)
# print(max_testelevation)
