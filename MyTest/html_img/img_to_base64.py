import base64
from pathlib import Path



def img_2_bs(img_full_path):
    with open(img_full_path, 'rb') as f:
        file_ext = Path(img_full_path).suffix.lower().lstrip('.')
        base64_str = base64.b64encode(f.read()).decode('utf-8')
        mime_types = {
            'png': 'image/png',
            'jpg': 'image/jpeg',
            'jpeg': 'image/jpeg',
            'gif': 'image/gif',
            'webp': 'image/webp'
        }
        mime_type = mime_types.get(file_ext, 'application/octet-stream')
        # data_uri = f"background-image: url('data:{mime_type};base64,{base64_str}');"
        data_uri = f"data:{mime_type};base64,{base64_str}"
        print(data_uri)
if __name__ == '__main__':
    img_2_bs(r"D:\Local\JS\底部.png")