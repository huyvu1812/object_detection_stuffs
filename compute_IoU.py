IOU =   Area of union /  area of intersection

def IOU(box1, box2):

    x1, y1, w1, h1 = box1

    x2, y2, w2, h2 = box2

    w_intersection = min(x1 + w1, x2 + w2) - max(x1, x2)

    h_intersection = min(y1 + h1, y2 + h2) - max(y1, y2)

    if w_intersection <= 0 or h_intersection <= 0: 

        return 0

    I = w_intersection * h_intersection

    U = w1 * h1 + w2 * h2 - I 

    return I / U

iou = [IOU(y_test[i], y_pred[i]) for i in range(len(x_test))] 
