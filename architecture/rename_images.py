import os
import re
import sys
import shutil
from bs4 import BeautifulSoup

_report_path = "./architecture/.report"

def rename_images(report_path):
    images_path = os.path.join(report_path, "images")
    views_path = os.path.join(report_path, "views")

    if not os.path.exists(views_path):
        print("Views folder '" + views_path + "' not found. Check report path.")
        return

    for filename in os.listdir(views_path):
        if filename.endswith(".html"):
            with open(os.path.join(views_path, filename), 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')
                
                view_name = soup.title.string.strip() if soup.title else None
                view_id = filename.replace(".html", "")

                if view_name:
                    clean_name = re.sub(r'[/\\?%*:|"<> ]', '_', view_name)
                    old_image = os.path.join(images_path, f"{view_id}.png")
                    new_image = os.path.join(images_path, f"{clean_name}.png")

                    if os.path.exists(old_image):
                        print(f"Copying {view_id} -> {clean_name}")
                        shutil.copy(old_image, new_image)
                        #print(f"Renaming {view_id} -> {clean_name}")
                        #os.rename(old_image, new_image)

if __name__ == "__main__":
    report_path = _report_path if len(sys.argv) == 1 else sys.argv[1]
    rename_images(report_path)
