
#---------------------------------------------------------------------------------------------------------------------#
class GENERALAspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "width": ("INT", {"default": 1024, "min": 64, "max": 2048}),
                "height": ("INT", {"default": 1024, "min": 64, "max": 2048}),
                "aspect_ratio": (["custom", "SDXL 1:1 square 1024x1024", "SDXL 3:4 portrait 896x1152", "SDXL 5:8 portrait 832x1216", "SDXL 9:16 portrait 768x1344", "SDXL 9:21 portrait 640x1536", "SDXL 4:3 landscape 1152x896", "SDXL 3:2 landscape 1216x832", "SDXL 16:9 landscape 1344x768", "SDXL 21:9 landscape 1536x640", "SD1.5 1:1 square 512x512", "SD1.5 2:3 portrait 512x768", "SD1.5 3:4 portrait 512x682", "SD1.5 3:2 landscape 768x512", "SD1.5 4:3 landscape 682x512", "SD1.5 16:9 cinema 910x512", "SD1.5 2:1 cinema 1024x512"],),
                "swap_dimensions": (["Off", "On"],),#
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
            }
        }
    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("width", "height", "batch_size")
    FUNCTION = "Aspect_Ratio"

    CATEGORY = "Winston"

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions,batch_size):
        if aspect_ratio == "SDXL 1:1 square 1024x1024":
            width, height = 1024, 1024
        elif aspect_ratio == "SDXL 3:4 portrait 896x1152":
            width, height = 896, 1152
        elif aspect_ratio == "SDXL 5:8 portrait 832x1216":
            width, height = 832, 1216
        elif aspect_ratio == "SDXL 9:16 portrait 768x1344":
            width, height = 768, 1344
        elif aspect_ratio == "SDXL 9:21 portrait 640x1536":
            width, height = 640, 1536
        elif aspect_ratio == "SDXL 4:3 landscape 1152x896":
            width, height = 1152, 896
        elif aspect_ratio == "SDXL 3:2 landscape 1216x832":
            width, height = 1216, 832
        elif aspect_ratio == "SDXL 16:9 landscape 1344x768":
            width, height = 1344, 768
        elif aspect_ratio == "SDXL 21:9 landscape 1536x640":
            width, height = 1536, 640
        elif aspect_ratio == "SD1.5 1:1 square 512x512":
            width, height = 512, 512
        elif aspect_ratio == "SD1.5 2:3 portrait 512x768":
            width, height = 512, 768
        elif aspect_ratio == "SD1.5 3:2 landscape 768x512":
            width, height = 768, 512
        elif aspect_ratio == "SD1.5 16:9 cinema 910x512":
            width, height = 910, 512
        elif aspect_ratio == "SD1.5 3:4 portrait 512x682":
            width, height = 512, 682
        elif aspect_ratio == "SD1.5 4:3 landscape 682x512":
            width, height = 682, 512
        elif aspect_ratio == "SD1.5 2:1 cinema 1024x512":
            width, height = 1024, 512
            
        if swap_dimensions == "On":
            return(height, width,batch_size,)
        else:
            return(width, height,batch_size,)        


