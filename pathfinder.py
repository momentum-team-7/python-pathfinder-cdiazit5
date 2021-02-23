from PIL import Image, ImageColor, ImageDraw

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
# print (dimensions_large)

def grayscale(elevation, min, max):
# func to covert elevation to RBG value
    color_value = (((int(elevation) - large_min_elevation)/(large_elevation_diff) * 255))
    return (int(color_value), int(color_value), int(color_value))

im = Image.new('RGB', (1201,1201))
for x in range(1201):
        for y in range (1201):
            im.putpixel((x,y), grayscale(large_coordinates[y][x], large_min_elevation, large_max_elevation))
im.save('elevation_large.png')
Image.open('elevation_large.png')
# print(im.getpixel((4,80)))


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
# print (dimensions_small)

# im = Image.new('RGB', (600,600))
# for x in range(600):
#         for y in range (600):
#             im.putpixel((x,y), grayscale(small_coordinates[y][x], min_elevation, max_elevation))
# im.save('elevation_small.png')
# Image.open('elevation_small.png')
# print(im.getpixel((4,80)))


# testing

# convert coord into pixel tup?
path_list = [(0,1),(0,2),(0,4),(0,5),(0,6),(0,6),(0,7), (0,8), (0,0), (1,0), (6,0)]
# path_list = [(small_coordinates[0][1], small_coordinates[0][2], small_coordinates[0][3], small_coordinates[0][4]]

# def find_shortest_distance(elevation, top, middle, bottom):
#     top_distance = elevation - top
#     middle_distance = elevation - middle
#     bottom_distance = elevation - bottom
#     lowest_dist = min([top_distance, middle_distance, bottom_distance])
#     if lowest_dist == top_distance:
#         return top_distance
#     if lowest_dist == middle_distance:
#         return middle_distance
#     else: 
#         return bottom_distance



# append the lowest elevation value to the path list to draw?
path_list = []
def path_finder():
    x = 0 
    y = 1 
    file_height = len(small_coordinates)
    file_width = len(small_coordinates)
    for coordinate in range (len(small_coordinates)):
        current_pos = small_coordinates[x][y]
        next_pos = []
        



im = Image.new('RGB', (600,600))
draw = ImageDraw.Draw(im)
for x in range(600):
        for y in range (600):
            im.putpixel((x,y), grayscale(small_coordinates[y][x], min_elevation, max_elevation))
for x in range(0, 30):
    for y in range(0, 30):
        draw.line(path_list, (150,150,00))


        #     starting_point = small_coordinates[1][0]
im.save('elevation_small.png')
Image.open('elevation_small.png')
print(im.getpixel((4,80)))
# print(im.getpixel(small_coordinates[0][1]))
print(im.getpixel((0,0)))
print(small_coordinates[1][1])
print(len(small_coordinates[0]))
print(len(small_coordinates))


# for coord in small_coordinates: