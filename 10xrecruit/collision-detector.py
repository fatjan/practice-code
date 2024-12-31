def time_to_collide(obj_1, obj_2):
    x1, y1, z1, r1, vx1, vy1, vz1 = obj_1[0], obj_1[1], obj_1[2], obj_1[2], obj_1[4], obj_1[5], obj_1[6]
    x2, y2, z2, r2, vx2, vy2, vz2 = obj_2[0], obj_2[1], obj_2[2], obj_2[3], obj_2[4], obj_2[5], obj_2[6]
    
    if (vx1 < 0 and vx2 > 0) or (vy1 < 0 and vy2 > 0) or (vz1 < 0 and vz2 > 0) or (vx1 > 0 and vx2 < 0) or (vy1 > 0 and vy2 < 0) or (vz1 > 0 and vz2 < 0):
        return "No Collision"

    distance = r1 + r2
    distance = sqrt((x2 - x1 + (vx2 - vx1) * t)^2 + (y2 - y1 + (vy2 - vy1) * t)^2 + (z2 - z1 + (vz2 - vz1) * t)^2)

    return "No Collision"


obj_1 = [10, 3, -10, 5, -9, 3, -8]
obj_2 = [2, 0, 0, 6, -4, 3, -10]
print(time_to_collide(obj_1, obj_2))

obj_1 = [-7, 5, 0, 3, -1, 0, 3]
obj_2 = [10, 7, -6, 6, -2, 0, 4]
print(time_to_collide(obj_1, obj_2))

obj_1 = [-4, -1, 0, 3, -1, -5, -6]
obj_2 = [2, 1, 8, 6, 4, 0, -1]
print(time_to_collide(obj_1, obj_2))




