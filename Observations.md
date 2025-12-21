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

### Resolution
The images in the dataset donot store dpi (dots per inch) in their metadata. I was unable to find the resolution.

###





















