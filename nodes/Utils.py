import os

# FONT_PATH= os.path.abspath(os.path.join(os.path.dirname(__file__),'../assets/王汉宗颜楷体繁.ttf'))

import matplotlib.font_manager as fm

def get_font_files(directory):
    font_files = {}

    # 从指定目录加载字体
    for file in os.listdir(directory):
        if file.endswith('.ttf') or file.endswith('.otf'):
            font_name = os.path.splitext(file)[0]
            font_path = os.path.join(directory, file)
            font_files[font_name] = os.path.abspath(font_path)

    # 尝试获取系统字体
    try:
        font_paths = fm.findSystemFonts()
        for path in font_paths:
            try:
                font_prop = fm.FontProperties(fname=path)
                font_name = font_prop.get_name()
                font_files[font_name] = path
            except Exception as e:
                print(f"Error processing font {path}: {e}")
    except Exception as e:
        print(f"Error finding system fonts: {e}")

    return font_files

r_directory = os.path.join(os.path.dirname(__file__), '../assets/')

font_files = get_font_files(r_directory)
# print(font_files)


class ColorInput:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { 
             
                    "color":("TCOLOR",), 
                             },
                }
    
    RETURN_TYPES = ("STRING",)
    # RETURN_NAMES = ("WIDTH","HEIGHT","X","Y",)

    FUNCTION = "run"

    CATEGORY = "♾️Mixlab/utils"

    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,False,)

    def run(self,color):
        return (color,)



class FontInput:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { 
             
                    "font": (list(font_files.keys()),),
                             },
                }
    
    RETURN_TYPES = ("STRING",)
    # RETURN_NAMES = ("WIDTH","HEIGHT","X","Y",)

    FUNCTION = "run"

    CATEGORY = "♾️Mixlab/utils"

    INPUT_IS_LIST = False
    OUTPUT_IS_LIST = (False,False,)

    def run(self,font):

        return (font_files[font],)