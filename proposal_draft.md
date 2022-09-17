# DATA 606 Capstone in Data Science (Final Project)

## Author's : 
## Koushik Kumar Reddy Ajjuguttu (AR32779)
## Rama Charan Teja Polanki (DZ83376)

## Project Title:  SYNTHETIC FACE GENERATION

#### _What is your issue of interest?_

Synthetic Face Generation, is gaining a lot of attraction in current days.
> "The coolest idea in the last 20 years" - quoted by Yann LeCun

 Synthetic face generation has many applications like data augmentation for machine learning models, usage in anime or cartoons, creating social media influencers etc. The technology behind this is GANs which is short for Generative Adversarial Networks.
Many firms and R&Ds started working on GANs extensively in recent days. Facebook is extensively working on this to use new faces in the metaverse. An artificially generated Instagram influencer named Miquela Sousa got over a million followers on Instagram before it was announced that she wasn't real.

 >"Until my conversation with Nikola, it seemed like an indisputable fact that Miquela wasn’t real" - quoted by a reporter from "The Cut"
 
 The success stories of GANs reflects on the impact they create in society.
 
#### _Why is this issue important to you and/or others?_

 In data science, it is very common to face issues like, the dataset is not big enough, the dataset is not diverse enough, amount of data present for one label dominates amount of data present for another. We personally faced this issue while creating a model for attendence system by face recognition. Face synthesis can be used as a data augmentation technique in such cases to create more data. Microsoft created a complete dataset with synthetic faces. When tesed on different models, the performance was much better than models trained using normal dataset on test data. Microsoft says this is because of the diversity added in the dataset.

 >"We demonstrate that it is possible to perform face-related computer vision in the wild using synthetic data alone." -quoted by Microsoft

 Content creators can use this technique when they want images of so many people(in cases like metaverse) or when they have to use a face for some sensitive issue that could be uncomfortable for the person whose face is displayed. The same model can be used on anime images and reduce valuable efforts of anime character designers and artists to create new anime characters. This technique can also be used to create avatars.
 
#### _What questions do you have in your mind and would like to answer?_

As explained above, synthetic face generation is a research topic that can be used in so many aspects. Our research finds out and stores the key features to be present in a face and create new faces by keeping the key features constant and changing other features of a face. The actions that the model will be handling are:

- Generate a new face
- Distinguish whether a face is real or synthetic

As we are fairly new to GANs, we personally have many questions in mind. 

Some of them are:
- What are the key performance indicators of the model?
- Can we give some input parameters to the model so that we can get a particular type of face? (like a face of particular ethnicity)
- Will the generated faces really be human indistinguishable?
- Will the generated faces be computer indistinguishable?(i.e., Can we build a model other than discriminator which is trained along with generator to distinguish between synthetic and real faces)
- Are the generated faces usable in other models?
- Can we induce a specific feature like smile into the faces by tweaking an input parameter?
- Is it possible to generalize the model in such a way that we can input an image and the model can generate images in the context of input image?  
 

#### _Where do you get the data to analyze and help answer your questions?_

We obtained the dataset from the source below:-

http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html

It is called the celebA dataset and contains over 200,000 face images along with different tags.
The data is from a trusted source which is Multimedia lab from "The Chinese University of Hong Kong".
The data contains over 38 different attributes namely, 
- 5_o_Clock_Shadow
- Arched_Eyebrows
- Attractive
- Bags_Under_Eyes
- Bald
- Bangs
- Big_Lips
- Big_Nose
- Black_Hair
- Blond_Hair
- Blurry
- Brown_Hair
- Bushy_Eyebrows
- Chubby
- Double_Chin
- Eyeglasses
- Goatee
- Gray_Hair
- Heavy_Makeup
- High_Cheekbones
- Male
- Mouth_Slightly_Open
- Mustache
- Narrow_Eyes
- No_Beard
- Oval_Face
- Pale_Skin
- Pointy_Nose
- Receding_Hairline
- Rosy_Cheeks
- Sideburns
- Smiling
- Straight_Hair
- Wavy_Hair
- Wearing_Earrings
- Wearing_Hat
- Wearing_Lipstick
- Wearing_Necklace

#### _What questions do you have in your mind and would like to answer?_

Here, the unit of analysis is the location

#### _What variables/measures do you plan to use in your analysis?_

The train data will contain face images as input data. 
The aim will be to make the images indistinguishible by a discriminator.

#### _What kinds of techniques/models do you plan to use?_

We will be using a GAN model.
It contains a number of 2d convolutions.
Additionally, we will be using image processing techniques for preprocessing.
A block digram of how the model looks is shown below:-
![Sample GAN](https://miro.medium.com/max/1050/1*XKanAdkjQbg1eDDMF2-4ow.png)

#### _How do you plan to develop/apply ML and how do you evaluate performance of models?_

We are planning to make use of google colaboratory which provides GPU and keras library to create convolution networks.  
Unlike other networks, GANs are very difficult to evaluate as we are just producing new images which cannot be compared to any other. 
Some qualitative techniques for evaluating GAN generator models are listed below:-
- Nearest Neighbors.
- Rapid Scene Categorization.
- Rating and Preference Judgment.
- Evaluating Mode Drop and Mode Collapse.
- Investigating and Visualizing the Internals of Networks

Although which method to use should be decided through deep analysis after the model creation according to the face quality that the model is producing.

#### _What outcomes do you intend to achieve?_

The project aims to create a model which can create faces which are indistinguishable by  humans or machines. Through this project we intend to gain more insights about Machine learning tools, requirement analysis, more insights into convolution neural networks, etc.
