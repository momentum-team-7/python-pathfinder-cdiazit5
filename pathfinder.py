from PIL import Image

large_mountain = "elevation_large.txt"
small_mountain = "elevation_small.txt"
small_coordinates = []
large_coordinates = []
# small text is 600 x 600
# test_coordinates = []

with open('elevation_large.txt', 'r') as file:
    for line in file.readlines():
        large_coordinates.append(line.split())

large_min_elevation = int(min(map(min, large_coordinates)))
# print(min_elevation)

large_max_elevation = int(max(map(max, large_coordinates)))
# print(max_elevation)

large_elevation_diff = int((large_max_elevation)-(large_min_elevation))
# print(elevation_diff)

dimensions_large = len(large_coordinates), len(large_coordinates[0])
print (dimensions_large)

def grayscale(elevation, min, max):
# func to covert elevation to RBG value
    color_value = (((int(elevation) - large_min_elevation)/(large_elevation_diff) * 255))
    return (int(color_value), int(color_value), int(color_value))

im = Image.new('RGB', (1201,1201))
for x in range(1201):
        for y in range (1201):
            im.putpixel((x,y), grayscale(large_coordinates[x][y], large_min_elevation, large_max_elevation))
im.save('elevation_large.png')
Image.open('elevation_large.png')
print(im.getpixel((4,80)))


# def small_mountain_ele():
with open('elevation_small.txt', "r") as file:
    for line in file.readlines():
        small_coordinates.append(line.split())
        # for each line we are spliting, and adding to list of lists
    # print(coordinates) 

min_elevation = int(min(map(min, small_coordinates)))
# print(min_elevation)

max_elevation = int(max(map(max, small_coordinates)))
# print(max_elevation)

elevation_diff = int((max_elevation)-(min_elevation))
# print(elevation_diff)

dimensions_small = len(small_coordinates), len(small_coordinates[0])
print (dimensions_small)

im = Image.new('RGB', (600,600))
for x in range(600):
        for y in range (600):
            im.putpixel((x,y), grayscale(small_coordinates[x][y], min_elevation, max_elevation))
im.save('elevation_small.png')
Image.open('elevation_small.png')
print(im.getpixel((4,80)))














# with open('testgrid.txt', "r") as file:
#     for line in file.readlines():
#         test_coordinates.append(line.split())
#         # for each line we are spliting, and adding to list of lists
#     # print(test_coordinates) 

# min_testelevation = int(min(map(min, test_coordinates)))
# max_testelevation = int(max(map(max, test_coordinates)))
# print(min_testelevation)
# print(max_testelevation)
