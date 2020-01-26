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
nthFrame = 2
startframe = 0
endframe = 20
file_name = "platform_arms"

for f in range(startframe, endframe, nthFrame):
    bpy.context.scene.frame_current = f
    n = int(f/nthFrame)
    TakePhoto(n)
    
print("\nCompleted.")
