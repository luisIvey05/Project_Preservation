# Project Preservation: 3D Reconstruction from Video Imagery 
<h4>
<a href="#intro"> Introduction/Motivation </a> | 
<a href="#pipe">Pipeline</a> |
<a href="#quick">Quick Start</a> |
<a href="#res">Results</a> |
<a href = "#ref">References</a>
</h4>

Project Preservation is a website that preserves artifacts at risk of disappearing. We built a high-quality 3D model reconstruction pipeline with photogrammetry and deep learning techniques that use crowdsourced images and videos to create reconstructed models. After reconstructing the artifact, we can upload it to our virtual "museum" website so others can view them or download them for further research. Our team focused on the model reconstruction feature for this project. We did our experiments on an iPhone. However, we hope to expand to other devices in future work. <p id="intro"> </p>

## Introduction/Motivation
Photogrammetry is the science behind acquiring real-world measurements from images that capture physical objects or terrain features [1]. The fundamental principle used in photogrammetry is triangulation. By taking photographs of an object from at least two different locations, a coordinate system can then be derived to measure the distance of how far that object is from the photograph. Photogrammetry methods can be extended for a complete process of 3D geometry to reconstruct an object or scene. The process includes taking pictures with RGB-D cameras, such as Microsoft Kinect or Intel's RealSense Cameras, and connecting the images to form a 3D model [2]-[4]. The construction of a 3D model from a set of images can be seen in many industries today, especially in archaeology. 

Photogrammetry's 3D reconstruction revolutionizes archaeology by replacing archaic and slow site mapping methods with faster and newer technologies. The transition to photogrammetry techniques has come at a crucial time where recent weather patterns, rising sea levels, man-made destruction, and frequently occurring wildfires have induced the disappearance of ancient ruins [5]. Events like the fire that broke out in the Norte-Dame cathedral show the need for 3D reconstruction technology to be accessible. Luckily, a person who mapped the cathedral years ago with LiDAR equipment lent his 3D model for the restoration of the cathedral [6]. However, other cases, such as those in the middle east, where militants destroyed many ancient sites, were not so lucky [7].

The classical approach to 3D reconstruction aims to use a multiview stereo vision procedure to recover the lost depth dimension from the 2D images. Alternatively, for better results, scene depth is captured using LiDAR sensors. The reconstruction process involves feature extraction, image matching, structure motion/multiview stereo, depth estimation, dense point cloud, meshing, and texturing. This technique has been extensively investigated, which has inspired many open-sourced libraries to compile various existing algorithms (in an efficient manner). One of those libraries is Open3D [8] which speeds up production time, has an optimized backend that supports parallelization, has been used in several published research projects, and can create a 3D reconstruction of a scene or object. Open3D scene reconstruction system takes in RGB and depth images which then follow three crucial steps to output a mesh model of the scene. The first step builds the geometric surfaces using a few sequenced images. The second step consists of globally aligning fragments to obtain fragment poses and runs a camera calibration function. The final step outputs a mesh model of the scene by integrating the RGB-D images. However, the need for depth images, a calibrated camera, acquiring a camera's intrinsic values, a large number of views, and an expensive offline reconstruction process does not make this technology accessible for any standard camera to be used in preserving artifacts. A data-driven approach is instead used to help alleviate the need for expensive and complicated capturing sensors.  

A data-driven approach to acquiring monocular depth estimation has achieved impressive per-pixel depth approximation using CNNs [9]-[11]. A typical encoder-decoder architecture is found in the most recent work for depth estimation. To improve the quality of depth estimation, transfer learning techniques, such as using a pre-trained network for image classification for the encoder, enables rich feature depth extraction [12]. Sharper depth estimation is produced by choosing a pre-trained encoder that does not rapidly downsample an input image and keeps a reasonable amount of spatial coherency. The typical loss function for depth estimation usually uses a combination of point-wise L2 loss, image gradient of the depth, and structural similarity (SSIM) [13]. However, for 3D reconstruction, a qualitative depth estimation result is not optimal, and a rigorous quantitative estimation is needed. Therefore, the use of an inverse Huber loss [14] is needed. More accurate depth estimation is needed for 3D reconstruction during the rigid alignment process of point clouds. Therefore, combining monocular depth estimation with a traditional 3D reconstruction system allows for a more convenient way of preserving artifacts. 

Classical approaches to 3D reconstruction require many meticulous steps and expensive equipment to reconstruct subjects. Combining data-driven methods with classical techniques helps ease the process of digitally preserving ancient artifacts and structures. Preserving artifacts would be as simple as recording a video of the subject, estimating depth with deep learning, and feeding the RGB-D sequence of images through a 3D reconstruction system.   
<p id="pipe"> </p>

## Pipeline

![](https://raw.github.com/luisIvey05/Project_Preservation/tree/main/images/pipeline.png)


<p id="res"> </p>

## Requirements
```
Python 3.9.15
Open3D 0.16.1
OpenCV 4.6.0
NumPy 1.23.3
``` 
<p id="res"> </p>

## Results

<p id="quick"> </p>

## Quick Start

<p id="ref"> </p>

## References
[1] Aber, J. S., Marzolff, I., & Ries, J. B. (2010, May 14). _Photogrammetry_. Small-Format Aerial Photography.<br />
[2] R. A. Newcombe, S. J. Lovegrove, and A. J. Davison, “DTAM: Dense tracking and mapping in real-time,” in ICCV, 2011. 2 <br />
[3] J. Engel, T. Sch ¨ops, and D. Cremers, “LSD-SLAM: Large-scale direct monocular slam,” in ECCV, 2014. 2 <br />
[4] G. Klein and D. Murray, “Parallel tracking and mapping for small ar workspaces,” in ISMAR, 2007. 2 <br />
[5] Zaffos, J. (n.d.). _Why the Earth Must Be Mapped_. Anthropology and geography.<br />
[6] M. Lou and B. Griggs, “Four years ago, an art historian used lasers to digitally map Notre Dame Cathedral. his work could help save it,”  _CNN_, 17-Apr-2019. <br />
[7] A. Curry, “Here are the ancient sites Isis has damaged and destroyed,”  _History_, 03-May-2021. <br />
[8] Zhou, Qian-Yi, Jaesik Park, and Vladlen Koltun. "Open3D: A modern library for 3D data processing." arXiv preprint arXiv:1801.09847 (2018). <br />
[9] D. Eigen, C. Puhrsch, and R. Fergus. Depth map prediction from a single image using a multi-scale deep network. In NIPS, 2014. <br />
[10] B. Li, C. Shen, Y. Dai, A. van den Hengel, and M. He. Depth and surface normal estimation from monocular images us- ing regression on deep features and hierarchical crfs. 2015 IEEE Conference on Computer Vision and Pattern Recogni- tion (CVPR), pages 1119–1127, 2015. <br />
[11] I. Laina, C. Rupprecht, V. Belagiannis, F. Tombari, and
N. Navab. Deeper depth prediction with fully convolutional residual networks. 2016 Fourth International Conference on 3D Vision (3DV), pages 239–248, 2016 <br />
[12] Alhashim, I., & Wonka, P. (2018). High Quality Monocular Depth Estimation via Transfer Learning. _arXiv_. <br />
[13] J. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli.
Image quality assessment: from error visibility to structural similarity. IEEE Transactions on Image Processing, 13:600– 612, 2004 <br />
[14] Nekrasov, V., Dharmasiri, T., Spek, A., Drummond, T., Shen, C., & Reid, I. (2018). Real-Time Joint Semantic Segmentation and Depth Estimation Using Asymmetric Annotations. _arXiv_.
