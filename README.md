# B-NeRF
NeRF with brightness

## Setup  
1. Environtment
```shell
conda create -n b_nerf python
conda activate b_nerf
pip install -r requirements.txt
```  
## Data
Download from here  
- [NeRF Data](https://drive.google.com/drive/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1)

Prepare your data [Tutorial here](https://github.com/congdinhchi/B-NeRF/tree/main/data)

Finally, your data need save in `processed` with structure:
```
processed/<case_name>
|-- images
    |-- 000.png        # target image for each view
    |-- 001.png
    ...
|-- transforms.json     # camera pose
```  
## Run

`python -m scripts.run`  

*args*
    - `--case ./processed/<case_name>`
    - `--continue_training  ./processed/<case_name>/record/<name_record>`

    


