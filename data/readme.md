# Prepare your data  

raw data đặt theo cấu trúc sau

```
raw/<case_name>
|-- images
    |-- 000.png        # target image for each view
    |-- 001.png
    ...
|-- dataShot.json     # thông tin unity ( nếu có )
```  

mục tiêu 

```
processed/<case_name>
|-- images
    |-- 000.png        # target image for each view
    |-- 001.png
    ...
|-- transforms.json     # camera pose
```  

## Option

Cut ảnh 
 
`python -m utils.cut_images`

