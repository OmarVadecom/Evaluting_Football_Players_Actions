from django.shortcuts import render

from .forms import ChooseMatch
from matplotlib import pyplot as plt
from moviepy import editor as mpy
from moviepy.video.io.bindings import mplfig_to_npimage
# Create your views here.
from . import footyviz
import pandas as pd
# import os.path
# import threading
from os.path import exists

def index(request):
    form = ChooseMatch()
    match = 'waiting for choose!'
    data = pd.read_csv('liverpool2019/datasets/liverpool_2019.csv', index_col=('play', 'frame'))
    if request.GET:
        match = request.GET['choose_match']
        df = data.loc[match]
        clip = make_animation(df)
        clip_voronoi = make_animation(df,voronoi=True)
        # composite_clip = mpy.CompositeVideoClip([clip, clip_voronoi.resize(0.3).set_position((200,10))])
        path = 'liverpool2019/static/liverpool2019/'+match
        if not exists(path+'1.mp4'):
            try:
                write_video(clip,path+'1.mp4')
            except:
                print("Error: unable to make a video")
        elif not exists(path+'2.mp4'):
            try:    
                write_video(clip_voronoi,path+'2.mp4')
            except:
                print('Error: unable to make a video')   
    return render(request, "liverpool2019/home.html", {'form':form,'match':match})   
   
def write_video(clip,path):
       clip.write_videofile(path)
     

# def test(request):
#     print("I am here")
#     print(request['fields'])
#     path = ""
#     # path = FILES_FOLDER+'test.mp4'
#     print(request.GET['geeks_field'],'here')
#     if  os.path.exists(path):
#         print(path)       
#     return render(request, "liverpool2019/view_match.html", {'path':path})        
     
def draw_frame_x(df, t, fps, voronoi=False):
        fig,ax,dfFrame = footyviz.draw_frame(df, t=t, fps=fps,goal_info='Barcelone',display_num=True, display_time=True)
        if voronoi:
            fig, ax, dfFrame = footyviz.add_voronoi_to_fig(fig, ax, dfFrame)
        image = mplfig_to_npimage(fig)
        plt.close()
        return image    

def make_animation(df, fps=20, voronoi=False):
    #calculated variables
    length=(df.index.max()+20)/fps
    clip = mpy.VideoClip(lambda x: draw_frame_x(df, t=x, fps=fps, voronoi=voronoi), duration=length-1).set_fps(fps)
    return clip
