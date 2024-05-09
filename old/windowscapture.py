from functions import load_settings, open_settings, get_resource_path
import mss
from PIL import Image
import numpy as np

settings = open_settings()

class WindowCapture:
    
    def __init__(self, window_name=None):
        settings = load_settings()
        if settings:
            self.x1 = int(settings.get("alert_region_1", {}).get("x", None))
            self.y1 = int(settings.get("alert_region_1", {}).get("y", None))
            self.x2 = int(settings.get("alert_region_2", {}).get("x", None))
            self.y2 = int(settings.get("alert_region_2", {}).get("y", None))
            self.detection = settings.get("detectionscale", {}).get("value", None)
            self.mode = settings.get("detection_mode", {}).get("value", "picture")
            self.detection = self.detection / 100
            #print(detection)
        else:
            print("No configuration found...")
            exit()

    def get_screenshot(self):
        with mss.mss() as sct:
            monitor = {"top": self.y1, "left": self.x1, "width": self.x2 - self.x1, "height": self.y2 - self.y1}
            screenshot = sct.grab(monitor)

        # Convert the Image to a NumPy array and drop the alpha channel
        img_array = np.array(screenshot)
        img_array = img_array[:, :, :3]  # Keep only RGB channels, drop the alpha channel

        # Create an Image object directly from the NumPy array
        img = Image.fromarray(img_array)
        # Convert the Image to a NumPy array and drop the alpha channel
        img_array = np.asarray(img)

        return img_array, screenshot
    
    def get_screenshot_value(self, y1, x1, x2, y2):
        with mss.mss() as sct:
            monitor = {"top": y1, "left": x1, "width": x2 - x1, "height": y2 - y1}
            try:
                screenshot = sct.grab(monitor)
            except:
                return None, None

        # Convert the Image to a NumPy array and drop the alpha channel
        img_array = np.array(screenshot)
        
        img_array = img_array[:, :, :3]  # Keep only RGB channels, drop the alpha channel
        #img_array.setflags(write=1)
        # Create an Image object directly from the NumPy array
        img = Image.fromarray(img_array)
        # Convert the Image to a NumPy array and drop the alpha channel
        img_array = np.asarray(img)

        return img_array, screenshot
    
    def take_screenshot(self, x1, y1, y2, x2):
        with mss.mss() as sct:
            monitor = {"top": y1, "left": x1, "width": x2, "height": y2}
            screenshot = sct.grab(monitor)

        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb, "raw", "RGB")

        img.save("img/image_replace.png")

        if img:
            return True
        
        return False