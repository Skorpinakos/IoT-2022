from prototype_for_plant_finder import process_image #process_image takes the path where take_photo stores and the current photo filaname and returns
# a list of th y dimension pixel height where lines occur and also centers_x and centers_y which are the x,y coordinates for each plant

def make_move(dx):
    pass
def take_photo(path,filename):
    return path,filename

path="Edge_Compute/images/"
out_path="Edge_Compute/diagnostics/"
filename='Capture1.png' #set image to test
default_distance=0.20 




#first shoot

start=0
end=0
dx=default_distance
lines_multitude=[0]
step=0
while True:
    step=step+1
    make_move(dx)
    path,filename=take_photo(path,filename)
    lines_y,centers_x,centers_y=process_image(filename,path,out_path,diagnostics_mode='none')
    if len(lines_y)==0:
        print('no plants, i finished') #this wouldn't happen we need an error handler in image_process to return 0 y_lines if no plants
        break
    lines_multitude.append(len(lines_y))
    flag_changed_line=True
    if lines_multitude[step]==lines_multitude[step-1]:
        #no new rows have appeared no old rows have dissapeared (or both if dx too big)
        flag_changed_line=False
        pass
        
    if lines_multitude[step]>lines_multitude[step-1]:
        #new rows have appeared 
        end=end+(lines_multitude[step]-lines_multitude[step-1]) #whatever was gained add to end (! keep in mind to get the current bottom row you want end-1 , not end)
        
    if lines_multitude[step]<lines_multitude[step-1]:
        #top row has dissapeared
        start=start+abs((lines_multitude[step]-lines_multitude[step-1])) #whatever was lost add to start

    focus_line_index=(end-2)-start #make docus line the one before the bottom

    if focus_line_index<0:
        print('only on row left on picture, breaking!')
        break
    focus_line_pixel=lines_y[focus_line_index]
    if flag_changed_line==True:
        #MAKE FUNC TO GET CENTERS BELONGING TO FOCUS LINE AND THEIR RESPECTIVE ELEMENTS

    #find focus lane and focus plants centers
