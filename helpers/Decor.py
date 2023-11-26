import cv2
import mss
import numpy as np

class Helper:
    def screen_capture_routine(func):
        def inner(self):
            print("executing", func.__name__, "Function")
            with mss.mss() as sct:
                # Part of the screen to capture. Multi-monitor setup, capture whole monitor stream to other.
                monitor = sct.monitors[0]
                
                while "Screen capturing":
                    # Get raw pixels from the screen, save it to a Numpy array
                    img = np.array(sct.grab(monitor))

                    # Display the captured frame
                    cv2.imshow("Screen Capture", img)

                    func(self, img)

                    # Press "q" to quit
                    if cv2.waitKey(25) & 0xFF == ord("q"):
                        cv2.destroyAllWindows()
                        break
            print("Finished")
            cv2.destroyAllWindows()
        return inner