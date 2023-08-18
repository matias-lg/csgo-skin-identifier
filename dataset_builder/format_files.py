import cv2
import os

if __name__ == "__main__":
   downloaded_dir = os.path.join(os.getcwd(), "downloaded_images")
   output_dir = os.path.join(os.getcwd(), "dataset")
   if not os.path.exists(output_dir):
      os.mkdir(output_dir)
      os.mkdir(os.path.join(output_dir, "images"))

   img_id = 0
   labels: list[tuple[str,str]] = []

   for idx, dir in enumerate(os.listdir(downloaded_dir)):
      if idx % 5 == 0:
         print(f"Processing {idx} of {len(os.listdir(downloaded_dir))} directories")

      label = dir
      for img in os.listdir(os.path.join(downloaded_dir, dir)):
         img_path = os.path.join(downloaded_dir, dir, img)
         img = cv2.imread(img_path)
         img = cv2.resize(img, (300, 300))
         cv2.imwrite(os.path.join(output_dir, "images", f"{img_id}.jpg"), img)
         labels.append((f"{img_id}.jpg", label))
         img_id += 1
   
   with open(os.path.join(os.getcwd(), output_dir, "labels.csv"), "w") as f:
      f.write("filename,label\n")
      for label in labels:
         f.write(f"{label[0]},{label[1]}\n")