import numpy as np
import cv2
from matplotlib import pyplot as plt
from tracker import iou_tracker
from utils import helper

# image parameters
image_width = 1280
image_height = 720
img = 255 * np.ones((image_height, image_width, 3), dtype=np.uint8)

# get trajectory
trajectories = helper.generate_boxes(image_width, image_height, 100, False)

# initialize a tracker object
track_obj = iou_tracker.VehicleTracker()

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
videoWriter = cv2.VideoWriter('{}/video_result.mp4'.format('./output'), fourcc, 2, (image_width, image_height))

plt.figure(figsize=(14, 10))

for i in range(0, len(trajectories)):
    img_copy = img.copy()
    observation = trajectories[i]
    time_stamp = observation[0]
    boxes = observation[1:]
    boxes_np = np.array(boxes)
    track_obj.track_iou(boxes_np, time_stamp, 0.2, 60)

    for track_traces in track_obj.Ta:
        box = track_traces['bboxes']
        vehicle_id = track_traces['id']
        box_cgs = track_traces['cg']
        kf_predicted_box = track_traces['predicted_box'][-1]
        for b in boxes:
            cv2.rectangle(img_copy,
                          (b[0], b[1]),
                          (b[2], b[3]),
                          (255, 0, 0),
                          thickness=2)
        cv2.rectangle(img_copy,
                      (kf_predicted_box[0], kf_predicted_box[1]),
                      (kf_predicted_box[2], kf_predicted_box[3]),
                      (0, 0, 255),
                      thickness=2)
        for cg_idx in range(min(10, len(box_cgs))):
            cv2.circle(img_copy,
                       (int(box_cgs[len(box_cgs)-1-cg_idx][0]), int(box_cgs[len(box_cgs)-1-cg_idx][1])),
                       4,
                       (255, 0, 0),
                       thickness=-1)
            cv2.putText(img_copy,
                        str(vehicle_id),
                        (int(box_cgs[len(box_cgs)-1-cg_idx][0]), int(box_cgs[len(box_cgs)-1-cg_idx][1])),
                        0,
                        fontScale=0.6,
                        color=(0, 0, 0),
                        thickness=1)
    plt.clf()
    plt.imshow(img_copy)
    plt.pause(0.1)

    videoWriter.write(img_copy)

videoWriter.release()
plt.show()