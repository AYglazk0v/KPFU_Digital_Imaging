import cv2
from easygui import fileopenbox

def ft_detectShape(c):
    shape = ""
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.01 * peri, True)
    if len(approx) > 5:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        if (ar >= 0.9 and ar <= 1.1):
            shape = "circle"
    return shape

def main():
    name_files = []
    flt=["*.jpg", "*.png"]
    path = fileopenbox("image",
                       "select file",
                       default = flt[0],
                       filetypes = flt)
    if path:
        try:
            image = cv2.imread(path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,31,4)
            cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            cnt = 0
            for c in cnts:
                shape = ft_detectShape(c)
                if (shape == "circle"):
                    cnt+=1
                x,y,w,h = cv2.boundingRect(c)
                cv2.putText(image, shape, (x, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,0), 2)
            print(cnt)
            cv2.imshow('image', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        except IOError:
            print("Are you crazy?!")

main()