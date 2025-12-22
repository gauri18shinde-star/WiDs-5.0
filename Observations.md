# Week 1 Plant Disease Classification 

## Class distribution
Image Count : 54305

Class Count : 38 

Max images : 5507

Min images : 152

If the data was divided equally, each class would have 2.63% data.

3 largest classes account for around 30% of the entire data.

25 classes < 2.63% of data.

<img width="630" height="437" alt="image" src="https://github.com/user-attachments/assets/2ac5eba1-9b10-4ea2-a149-1f68385f2f3e" />
<img width="639" height="407" alt="image" src="https://github.com/user-attachments/assets/2a2614da-103b-4896-ba21-2aa8bb2865df" />

## Image properties 
### Image Size
All images have the same size: (256, 256)

<img width="437" height="342" alt="image" src="https://github.com/user-attachments/assets/7f5aac97-6c63-4254-8d02-f0717d0a256f" />

Initially, the presence of only one dot seemed really confusing!
I had to run another program to verify the consistent image sizes.


### Resolution
The images in the dataset donot store dpi (dots per inch) in their metadata. I was unable to find the resolution.


## Image quality
### Blurry images
I checked for blurry images by converting them into grayscale, then checking brightness gradient by the Laplacian function.
I ran this code several times while varying the threshold value.

These are some really blurry images: 

![tomato yellow leaf curl cd37cbce-e141-40a5-8af6-8fa6790c7ed3___UF GRC_YLCV_Lab 02128](https://github.com/user-attachments/assets/dae7c409-9979-4554-beff-4efb5987dc2f)
![Citrus_greening f82235df-3322-45b4-8c8e-3b49497027ac___UF Citrus_HLB_Lab 1160](https://github.com/user-attachments/assets/119fdb63-e6a7-4af8-9b80-c6c2229b0e60)
![Citrus_greening 2a06d19e-3f66-4960-8d82-1e54687e2487___UF Citrus_HLB_Lab 1305](https://github.com/user-attachments/assets/97471b5b-936f-47f3-91e9-bab12b08f755)

Corn leaves are huge, and due to the fixed image size, they are not photographed fully.
Due to absence of leaf - background interface, the images are more easily flagged as blurred.
This did not happen in diseased corn leaves because of the disease patches present.

![blurry_corn_cbf3bab4-8c89-4025-b844-9bd9a120bcfb___R S_HL 8339 copy](https://github.com/user-attachments/assets/ea63bcbb-99a1-48e8-af93-84d53e59f88a)
![blurry_corn_641fd2fc-a98e-44c7-bac6-5e626aad8747___R S_HL 8140 copy](https://github.com/user-attachments/assets/bff317e5-9f46-4325-827d-56bb2c2d12f9)
![blurry_corn_37fa5c5c-0c0b-4f9e-b3fa-f9fac95639a7___R S_HL 8191 copy](https://github.com/user-attachments/assets/e07d85b7-999d-458b-9ab9-9e1012693077)


### Brightness and Contrast
Across the classes,

<img width="1102" height="362" alt="image" src="https://github.com/user-attachments/assets/89bbe6c8-469e-4ba9-aed4-62aa35da6dc8" />
<img width="1088" height="358" alt="image" src="https://github.com/user-attachments/assets/bef1acd0-f41f-4644-836e-c0132351a9a2" />


Corn with common rust has the lowest brightness and the highest contrast. This is because of the blacked out background present in all the images of the dataset.

<img width="190" height="191" alt="image" src="https://github.com/user-attachments/assets/3234b724-0f23-4b45-b152-5176962130a5" />


Conversely, healthy corn has the highest value. I think this is caused by increased brightness to higlight the leaf details along with the absence of dull background, shadows and dark disease patches.

<img width="191" height="193" alt="image" src="https://github.com/user-attachments/assets/9daf12a0-1b71-4b8c-a17f-5a275877e4d3" />

Squash with powdery mildew has a low contrast value and moderately high brigtness. The low contrast could you be caused by the huge number of homogeneous white dots.

<img width="191" height="190" alt="image" src="https://github.com/user-attachments/assets/850cb0a8-ca0c-4e39-92b0-4ce87121576a" />

Tomato with Target Spot has points clustered around a brightness value. I think this is because of uniform lighting, background, leaf size, color and orientation.

<img width="804" height="539" alt="image" src="https://github.com/user-attachments/assets/abb6032c-9003-4d03-8fd0-491aceed4d91" />

<img width="427" height="342" alt="image" src="https://github.com/user-attachments/assets/2d05119b-d82f-4a9f-ada2-31dc515c46fd" />

In contrast, potato with late blight has more distribution in its brightness values. It has varying background and the leaves are in different orientations and stages of disease.

<img width="800" height="534" alt="image" src="https://github.com/user-attachments/assets/75c50ccb-92f9-483a-bf33-172a5b78b548" />

<img width="429" height="342" alt="image" src="https://github.com/user-attachments/assets/a75be20a-15d8-47e3-af94-3d73e9ccd47a" />

Healthy blueberry leaves reflect light, so the brightness values were all skewed to the higher side.

<img width="798" height="528" alt="image" src="https://github.com/user-attachments/assets/469fdf8c-8ae0-4009-9c40-715f70aa5dca" />

<img width="421" height="340" alt="image" src="https://github.com/user-attachments/assets/7f1326aa-3dec-4d23-a596-3d70dd536cbd" />

Tomato leaves absorb light, and along with dark patches caused by early blight, the brightness values are to the lower sides.

<img width="805" height="540" alt="image" src="https://github.com/user-attachments/assets/d70e616b-135a-4219-ab0f-82b430a94e6f" />

<img width="422" height="343" alt="image" src="https://github.com/user-attachments/assets/7ac8e461-c422-4f7f-bfbc-7e0bac548d18" />

The healthy tomato class was really interesting. Either the leaves are very smooth or have lots of ridges and bumps. There is no in between. This causes a quantum jump in the contrast values.

<img width="801" height="556" alt="image" src="https://github.com/user-attachments/assets/b32098d9-4925-483f-b16a-24ccf4339165" />

<img width="419" height="340" alt="image" src="https://github.com/user-attachments/assets/db5461fb-2b2c-4f0a-b8d0-405f0eccea04" />


## Visual similairity
I plotted a heat map to measure similairity using the cosine similairity function.

<img width="1400" height="1200" alt="similairity" src="https://github.com/user-attachments/assets/d96bde3e-4b5f-4fb8-95b5-ea280c9a3e42" />

Grape with Black measles and Grape with Black rot look the most similair.

<img width="193" height="194" alt="Black measles grape" src="https://github.com/user-attachments/assets/14b69cfc-905b-4af0-8c67-b4475ad0edb4" />

<img width="191" height="193" alt="Black rot Grape" src="https://github.com/user-attachments/assets/5cc7af01-05b5-40dd-81f9-bd4fe8c285c6" />

Tomato with Early blight and Tomato with Target spot come second.

<img width="191" height="191" alt="Tomato Early Blight" src="https://github.com/user-attachments/assets/987c2473-1c1a-47f0-acd6-d0ca01b480cf" />


<img width="192" height="194" alt="Tomato Target spot" src="https://github.com/user-attachments/assets/039b3def-6503-49b4-8253-816ffd5d5f42" />

Orange with Haunglongbing and Corn with Northern Leaf Blight look least similair

<img width="193" height="192" alt="Orange Haunglongbing" src="https://github.com/user-attachments/assets/327bf8e8-ae02-41e0-8d58-9904d12adfd6" />

<img width="192" height="190" alt="Corn Northern Leaf Blight" src="https://github.com/user-attachments/assets/5681ba3d-e789-45d7-846a-3a227491915b" />


















