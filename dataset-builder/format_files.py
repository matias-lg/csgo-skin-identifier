# TODO:
# 1. Resize images to 300x300
# 2. Rename files with a counter, each file will have the label as the folder it is in
# 3. Create a CSV file with the filename and label
import cv2
import os

if __name__ == "__main__":
   dataset_dir = os.path.join(os.getcwd(), "dataset")
   output_dir = os.path.join(os.getcwd(), "dataset2")
   img_id = 0
   labels: list[tuple[str,str]] = []

   for idx, dir in enumerate(os.listdir(dataset_dir)):
      if idx % 5 == 0:
         print(f"Processing {idx} of {len(os.listdir(dataset_dir))} directories")

      label = dir
      for img in os.listdir(os.path.join(dataset_dir, dir)):
         img_path = os.path.join(dataset_dir, dir, img)
         img = cv2.imread(img_path)
         img = cv2.resize(img, (300, 300))
         cv2.imwrite(os.path.join(output_dir, "images", f"{img_id}.jpg"), img)
         labels.append((f"{img_id}.jpg", label))
         img_id += 1
   
   with open(os.path.join(os.getcwd(), output_dir, "labels.csv"), "w") as f:
      f.write("filename,label\n")
      for label in labels:
         f.write(f"{label[0]},{label[1]}\n")