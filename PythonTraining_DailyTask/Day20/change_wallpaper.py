import win32gui
import win32con


def set_wallpaper(image):
    """Function to set wallpaper."""
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image, win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE)


set_wallpaper(r"C:\Users\Administrator\Desktop\PythonTraining\PythonTraining_DailyTask\Day20\download.jpg")
