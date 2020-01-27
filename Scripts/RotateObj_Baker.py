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
    file = os.path.join(directory, cur_file_name + ".png")
    bpy.context.scene.render.filepath = file
    bpy.ops.render.render(write_still = True)



# Main
frames = 36
angle = 360/frames
file_name = "health_cube_rotate"
directory = os.path.dirname(bpy.data.filepath)


for n in range(0, frames):
    bpy.ops.transform.rotate(value=(angle * 2 * math.pi / 360.0))
    TakePhoto(n)
    
print("\nCompleted.")
