import bpy
import os
import math

renderer = bpy.data.scenes["Scene"].render
renderer.use_file_extension = True

         
def TakePhoto(n):
    # append 0 for the 0th - 9th frames.
    cur_file_name = file_name;
    if(n < 10):
        cur_file_name += "0"
    cur_file_name += str(n);
    
    # Take Photo
    file = os.path.join("C:/Users/Sean-PC/Desktop", cur_file_name)
    bpy.context.scene.render.filepath = file
    bpy.ops.render.render(write_still = True)



# Main
frames = 6
angle = 360/frames
file_name = "golden_scrap"

for n in range(0, frames):

    # Rotate all selected objects on z by angle
    for obj in bpy.context.selected_objects:
        obj.rotation_euler[2] += angle
        
    TakePhoto(n)
    
print("\nCompleted.")