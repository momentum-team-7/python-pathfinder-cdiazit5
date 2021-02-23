from PIL import Image, ImageColor, ImageDraw
small_mountain = "elevation_small.txt"
small_coordinates = []

path_list = [(0,1),(0,2),(0,4),(0,5),(0,6),(0,6),(0,7), (0,8), (0,0), (1,0), (6,0)]


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

def grayscale(elevation, min, max):
# func to covert elevation to RBG value
    color_value = (((int(elevation) - min_elevation)/(elevation_diff) * 255))
    return (int(color_value), int(color_value), int(color_value))

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


# def path_finder():
#     x = 0 
#     y = 1 
#     file_height = len(small_coordinates)
#     file_width = len(small_coordinates)
#     for coordinate in range (len(small_coordinates)):
#         current_pos = small_coordinates[x][y]
#         next_pos = []


path_list = [(0,1),(0,2),(0,4),(0,5),(0,6),(0,6),(0,7), (0,8), (0,0), (1,0), (6,0)]


im2 = Image.new('RGB', (600,600))
draw = ImageDraw.Draw(im2)
for x in range(600):
        for y in range (600):
            im2.putpixel((x,y), grayscale(small_coordinates[y][x], min_elevation, max_elevation))
for x in range(0, 30):
    for y in range(0, 30):
        draw.line(path_list, (150,150,00))
        


im2.save('practice_small.png')
Image.open('practice_small.png')
print(im2.getpixel((4,80)))
# print(im.getpixel(small_coordinates[0][1]))
print(im2.getpixel((0,0)))
print(small_coordinates[1][1])
print(len(small_coordinates[0]))
print(len(small_coordinates))