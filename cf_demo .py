import os
from examples.pytracker import PyTracker
from lib.utils import get_ground_truthes,plot_precision,plot_success
from examples.uavdataset_config import UAVDatasetConfig
if __name__ == '__main__':
    data_dir='C:/Users/A/pyCFTrackers_1/sequences'
    data_names=sorted(os.listdir(data_dir))

    print(data_names)
    dataset_config=UAVDatasetConfig()
    for data_name in data_names:
        data_path=os.path.join(data_dir,data_name)
        gts = get_ground_truthes(data_path)
        if data_name in dataset_config.frames.keys():
            start_frame,end_frame=dataset_config.frames[data_name][:2]
            if data_name!='bike1':
                gts=gts[start_frame-1:end_frame]
        img_dir = os.path.join(data_path,'img')
        tracker = PyTracker(img_dir,tracker_type='S2',dataset_config=dataset_config)
        poses=tracker.tracking(verbose=True,video_path=os.path.join('C:/Users/A/pyCFTrackers_1/results/S2',data_name+'_vis.avi'))
        plot_success(gts,poses,os.path.join('C:/Users/A/pyCFTrackers_1/results/S2',data_name+'_success.jpg'))
        plot_precision(gts,poses,os.path.join('C:/Users/A/pyCFTrackers_1/results/S2',data_name+'_precision.jpg'))
