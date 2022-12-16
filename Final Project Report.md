<h1> Project Title: SYNTHETIC FACE GENERATION <h1>
  
  <h3> By: Koushik Kumar Reddy Ajjuguttu (AR32779) &
Rama Charan Teja Polanki (DZ83376) </h3>

  

_**PROJECT INTRODUCTION:**_ 
  Synthetic face generation, as the title implies, pertains to synthetic generated faces employing machine learning data models, that have a diverse range of practical applications in today's world. Large projects can now be accomplished using generative networks and high computational power and modern applications. This model is also used in our project to generate trained images for real-time applications. So, why do we require these synthetically generated face images? Simply put, more data will be generated for use in research and development tasks. Some of the applications include: creating gaming characters, Instagram influencers, government agencies privacy and security, airport security screenings, fake imposter detections, and so on. 



_**PROJECT OBJECTIVE:**_ 
The objective of this project is to create a data model which can synthesize images of faces which it has never seen. The technology behind this is GANs which is short for Generative Adversarial Networks. Many firms and R&Ds started working on GANs extensively in recent days. 


_**WHY IS IT IMPORTANT:**_ 
It is very common in data science to encounter issues such as the dataset being insufficiently large or diverse, or the amount of data present for one label dominating the amount of data present for another. This was an issue we encountered while developing a face recognition model for an attendance system. In such cases, face synthesis can be used as a data augmentation technique to generate additional data. Microsoft built an entire dataset of synthetic faces. When different models were tested, their performance was far superior to models trained on normal datasets on test data. Microsoft claims this is due to the increased diversity in the dataset.

  
  
_**DATA COLLECTION:**_   
• We obtained the dataset from "http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html".  
• It is called the celebA dataset and contains over 200,000 face images along with different tags.  
• The data is from a trusted source which is Multimedia lab from The Chinese University of Hong Kong.  
• The data contains faces with over 38 different attributes:-   
  
   • 5_o_Clock_Shadow.  
   • Arched_Eyebrows.  
   • Attractive.  
   • Bags_Under_Eyes.  
   • Bald.  
   • Bangs   
   • Big_Lips.  
   • Big_Nose.  
   • Black_Hair.  
   • Blond_Hair.  
   • Blurry.  
   • Brown_Hair.  
   • Bushy_Eyebrows.  
   • Chubby.  
   • Double_Chin.  
   • Eyeglasses.  
   • Goatee.  
   • Gray_Hair.  
   • Heavy_Makeup.  
   • High_Cheekbones.  
   • Male.  
   • Mouth_Slightly_Open.  
   • Mustache.  
   • Narrow_Eyes.  
   • No_Beard.  
   • Oval_Face.  
   • Pale_Skin.  
   • Pointy_Nose.  
   • Receding_Hairline.  
   • Rosy_Cheeks.  
   • Sideburns.  
   • Smiling.  
   • Straight_Hair.  
   • Wavy_Hair     
   • Wearing_Earrings.  
   • Wearing_Hat.  
   • Wearing_Lipstick.  
   • Wearing_Necklace.  

  
  _**TEAM RESPONSIBILITY:**_ 
  
  We had divided our work and assigned each task ourselves so that it becomes easier to work together as a team to finish the planned tasks on time.

 #### Koushik Kumar Reddy Ajjuguttu (AR32779)

• Documentation 

• Data EDA 

• Testing, Training of GAN Model 

#### Rama Charan Teja Polanki (DZ83376)

• Data EDA 

• Implementation of GAN Model 

• Presentation 
  
  
  _**MACHINE LEARNING MODEL: GAN (Generative Adversarial Network):**_ 
  
 <img width="510" alt="image" src="https://user-images.githubusercontent.com/77987988/207760514-fb852f46-d564-40ff-bcd6-226cf7b28c22.png"> 
  
  Figure: Block Diagram of the GAN Architecture.   
 
  
  _**GAN DESCRIPTION:**_  
  
• The model we are using is called Generative adversarial networks.    
• It contains a generator and a discriminator as shown in the block diagram.    
• The generator takes an input and generates an image as an output.    
• The discriminator takes an image as an input and gives true or false as output.    
• Here true means it is a real image and false means it is a synthetic image.    
• Both the generator and the discriminator are 2D convolution neural networks.    
  
  
 _**MODEL ARCHITECTURE - GENERATOR:**_
  
<img width="579" alt="Screenshot 2022-12-14 at 10 07 39 PM" src="https://user-images.githubusercontent.com/77987988/207763611-2c6f8f25-b283-4259-ad8a-e44b1f2184d1.png">
  
Figure: Implemented Generator Architure.
  
  
• The generator takes few inputs and acts similar to a decoder to generate the image     
• So we start with a 1D dense layer.  
• We slowly increase the size of the dense layer.  
• Reshape the dense layer to 2D.  
• Apply smaller convolutions.  
• Apply bigger convolutions finally to achieve an image of size expected.  
  
  
  
  _**MODEL ARCHITECTURE - DISCRIMINATOR:**_

  <img width="571" alt="Screenshot 2022-12-14 at 10 07 21 PM" src="https://user-images.githubusercontent.com/77987988/207763472-2736a502-5f7a-430e-9d55-51d2f25d3abb.png">
  
Figure: Implemented Discriminator Architure.
  
  
• The discriminator starts with taking an image as an input.   
• Then the layers follow like a normal image classification layers.   
• We apply convolutions to get the resultant output size smaller and smaller We increase the number of kernels slowly.   
• Finally flatten all the neurons.   
• Then apply dense layers until we get one output neuron. 
  
  
  _**IMPLEMENTATION - Tech stack used:**_
  
We used the following technologies to implement code for the GAN model:    
  
• Python      
• Google colab.      
• Keras.       
• Opencv.       
• Tensorflow.       
• Numpy.        
• Scikit learn      
  
  _**RESULTS:**_   
  
  The output images that we generated through the trained GAN model are shown below:   
  
  <img width="338" alt="image" src="https://user-images.githubusercontent.com/77987988/207764940-1c310b17-91ef-4547-915f-c4709aa79970.png">
  
Figure: GAN Processed Synthetic Images.             
  
  
  _**FUTURE SCOPE:**_
  
• As more hardware is available, more epochs can be performed to better convergence.    
• More types of images could be added to get diverse faces.      
• Model could be generalized to produce not just images but also other things like hand written digits, anime images etc using transfer learning.     
• Model can be modified to give facial features as input and the resultant face contains those features.     
  
