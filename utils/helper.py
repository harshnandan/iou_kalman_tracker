import vehicle.Vehicle

def iou(bbox1, bbox2):
    """
    Calculates the intersection-over-union of two bounding boxes.
    :param bbox1: (numpy.array, list of floats): bounding box in format x1,y1,x2,y2.
    :param bbox2: (numpy.array, list of floats): bounding box in format x1,y1,x2,y2.
    :return: (int) intersection-over-onion of bbox1, bbox2
    """

    bbox1 = [float(x) for x in bbox1]
    bbox2 = [float(x) for x in bbox2]

    (x0_1, y0_1, x1_1, y1_1) = bbox1
    (x0_2, y0_2, x1_2, y1_2) = bbox2

    # get the overlap rectangle
    overlap_x0 = max(x0_1, x0_2)
    overlap_y0 = max(y0_1, y0_2)
    overlap_x1 = min(x1_1, x1_2)
    overlap_y1 = min(y1_1, y1_2)

    # check if there is an overlap
    if overlap_x1 - overlap_x0 <= 0 or overlap_y1 - overlap_y0 <= 0:
        return 0

    # if yes, calculate the ratio of the overlap to each ROI size and the unified size
    size_1 = (x1_1 - x0_1) * (y1_1 - y0_1)
    size_2 = (x1_2 - x0_2) * (y1_2 - y0_2)
    size_intersection = (overlap_x1 - overlap_x0) * (overlap_y1 - overlap_y0)
    size_union = size_1 + size_2 - size_intersection

    return size_intersection / size_union


def box_cg(box):
    """
    Returns the cg of a box
    :param box: (numpy.array, list of floats): bounding box in format x1,y1,x2,y2.
    :return:
    """
    return [((box[0] + box[2]) / 2), ((box[1] + box[3]) / 2)]


def generate_boxes(image_width, image_height, visualize_traj=False):
    traj = []
    v1 = Vehicle(200, 500, 100, 100, image_width, image_height, 10, 5)
    traj.append(v1.trajectory_box)

    v2 = Vehicle(600, 550, 100, 100, image_width, image_height, 0, 15)
    traj.append(v2.trajectory_box)

    max_count = max(len(traj[0]), len(traj[1]))

    boxes_traj = []
    for frame_idx in range(max_count):
        boxes = []
        for vh_idx in range(2):
            if frame_idx < len(traj[vh_idx]):
                boxes.append(traj[vh_idx][frame_idx])
            else:
                boxes.append(traj[vh_idx][-1])
        boxes_traj.append(boxes)

    if visualize_traj == True:
        for frame_idx in range(max_count):
            for b in boxes:
                cv2.rectangle(img, (b[0:2]), (b[2:4]), (255, 0, 0), thickness=2)

            plt.clf()
            plt.imshow(img)
            plt.pause(0.5)

    return boxes_traj
