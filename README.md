
# Fashion detection API

A flask API made using YOLO V3, trained on the deepfashion2 dataset.


## Run Locally

First clone the given git repo. 

```bash
  git clone https://github.com/prabalp/fashionAPI.git
  cd .\fashionAPI\
```
Download weights from the [Google Drive folder](https://drive.google.com/drive/folders/1mfglV2oayPXkE5pgItprjKuU03iW1hDK?usp=sharing), and save it in the fashionAPI folder.

Create a virtual enviroment using pip or conda.

```bash
 conda create -n fashionapi python=3.6 anaconda
```
Activate the conda enviroment.

```bash
  conda activate fashionapi
```
Now move to the project directory and install all the required packages.

```bash
  pip install -r requirements.txt
```
Now host the flask api in your local host 

```bash
  python app.py
```
After the api is up and running use postman to test it




 
## API Reference

#### Returns the tags 

```http
  POST /detections
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Picture URL` | `PATH` | Returns the tags in json format|





  
## Authors

- [@prabalp](https://github.com/prabalp)
- [@shubham-333](https://github.com/shubham-333)

  
## Further development 

- API returning images with boxs and labels

- API ready to handle videos

  
