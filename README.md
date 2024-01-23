# YoloV8_ComputerVision_Aiming_RainbowSix

### Introduction
See this Link for final result! :[https://www.youtube.com/shorts/lpwBsj0j_OY　](https://youtube.com/shorts/lpwBsj0j_OY?si=xgmBO4OIdy3xXzdP)
#### Purpose of the Project
The intersection of gaming and artificial intelligence presents a rich ground for innovation and exploration. This project aims to leverage the power of YOLO v8, an advanced deep learning model, for a unique application in the world of gaming – specifically, in Rainbow Six Siege. The core idea is to train the YOLO v8 model to identify and aim at enemy heads using computer vision techniques. This endeavor is not only a technical challenge but also serves educational and research purposes in the field of computer vision. Additionally, it offers an intriguing glimpse into the capabilities of AI in gaming scenarios, showcasing the potential for AI to interact with games in real-time without hacking or altering the game's memory or mechanics.

### Technical Overview

This project employs a sophisticated blend of technologies, prominently featuring YOLO v8 for real-time object detection. YOLO, an acronym for 'You Only Look Once', is renowned for its efficiency and accuracy in detecting objects in images. Version 8 of this deep learning model brings enhanced performance, making it ideal for the high-speed requirements of a dynamic gaming environment like Rainbow Six Siege.

**Key Technologies and Tools:**
- **YOLO v8:** The latest iteration of the YOLO series, known for its real-time object detection capabilities, playing a crucial role in identifying enemy characters in the game.
- **Python:** The primary programming language used for scripting the model training and the aiming bot.
- **OpenCV:** An open-source computer vision library used for image and video processing, crucial for interpreting game visuals.
- **Rainbowflow Dataset:** A specialized dataset tailored for Rainbow Six Siege, providing a wide range of in-game images for effective model training.

### Dataset Description

**Rainbowflow Dataset Overview**

For a machine learning model to perform effectively, especially in a complex and dynamic environment like Rainbow Six Siege, it requires a robust and relevant dataset. This is where the Rainbowflow dataset plays a pivotal role. Specially tailored for Rainbow Six Siege, the dataset comprises a wide range of in-game images that capture various aspects of the game environment, including different characters, lighting conditions, and backgrounds. This diversity is crucial for training the YOLO v8 model to accurately recognize and target enemy heads in varied in-game scenarios.

Key features of the Rainbowflow dataset include:
- **Diverse In-Game Scenarios:** Images encompassing a variety of maps, character skins, and gameplay situations, providing a comprehensive learning base for the model.
- **High-Resolution Images:** Ensuring detailed and clear visual data, which is vital for the precision required in head detection.
- **Annotated Data:** Each image in the dataset comes with pre-marked annotations, indicating the location of enemy heads, crucial for supervised learning.


### Model Training

#### Training Process

The training of the YOLO v8 model for head detection in Rainbow Six Siege was a meticulous process, involving several steps to ensure optimal performance. The model was trained using the Rainbowflow dataset, which provides a diverse range of in-game images, crucial for the model to learn and adapt to various scenarios encountered in the game.
![train_batch0](https://github.com/bob020416/YoloV8_ComputerVision_Aiming_RainbowSix/assets/82202284/796ceccd-4c8f-46c6-aa32-0ca4b1d7e3e4)

**Key Steps in the Training Process:**
1. **Data Preprocessing:** Before feeding the images into the model, they were preprocessed to align with the input requirements of YOLO v8. This included resizing images, normalizing pixel values, and converting annotations into a format readable by the model.
2. **Model Configuration:** The YOLO v8 model was configured with specific parameters to suit the task. This included setting the size of the detection layers, the learning rate, and the batch size, among other hyperparameters.
3. **Training and Validation:** The model underwent a series of training epochs, where it learned to identify and target enemy heads. A portion of the dataset was reserved for validation to monitor the model's performance and avoid overfitting.
4. **Performance Tuning:** After initial training rounds, the model was fine-tuned. Adjustments were made to the learning rate and other parameters based on the validation results to improve accuracy and reduce false positives.

#### Accuracy and Performance Metrics
![results](https://github.com/bob020416/YoloV8_ComputerVision_Aiming_RainbowSix/assets/82202284/7f805f39-6ad7-48ac-aaad-f96f5588ba18)
![confusion_matrix_normalized](https://github.com/bob020416/YoloV8_ComputerVision_Aiming_RainbowSix/assets/82202284/1ecb5026-8533-41d6-be45-2e001427ed45)
![labels](https://github.com/bob020416/YoloV8_ComputerVision_Aiming_RainbowSix/assets/82202284/cdc26f40-4cba-4fae-9fbf-85e9e2d7a740)

To evaluate the effectiveness of the model, various performance metrics were employed, focusing primarily on accuracy, precision, and recall. These metrics provided insights into how well the model could detect and accurately target enemy heads in different game scenarios.

- **Accuracy Results:** The model achieved a high accuracy rate, indicating its proficiency in correctly identifying enemy heads in most situations.
- **Precision and Recall:** Precision metrics demonstrated the model's ability to minimize false positives, while recall metrics indicated its success in identifying true positives.

### Aiming Bot Development

The creation of the aiming bot is a pivotal aspect of this project, integrating the trained YOLO v8 model into a real-time gaming environment. The bot's primary function is to automate aiming by detecting enemy heads in the game and guiding the player's aim towards them accurately and swiftly.

#### Script Functionality

1. **Integration with Rainbow Six Siege:** The bot operates by analyzing the game's visuals in real time. It captures screen frames and processes them through the trained YOLO v8 model to detect enemy positions.
2. **Aiming Mechanism:** Upon detecting an enemy head, the bot calculates the necessary cursor movement and automatically adjusts the aim. This process is designed to be as smooth and rapid as possible, emulating human-like aiming movements.

#### Current Challenges

Despite achieving significant success in head detection and automated aiming, there are still challenges that need addressing:

1. **Mouse Motion Issues:** The bot sometimes exhibits erratic or unnatural mouse movements. This is a key area for improvement, as smoother cursor transitions would make the bot's actions more human-like and less detectable.
2. **Scaling Problems:** The bot occasionally struggles with accurately scaling its movements based on different screen resolutions and in-game distances. Refining the scaling algorithm is essential for consistent performance across various gaming setups.



### Results and Demonstrations

The culmination of this project is best showcased through a video demonstration that highlights the capabilities of the trained YOLO v8 model and the developed aiming bot within Rainbow Six Siege. 

#### Video Demonstration


See this Link:[https://www.youtube.com/shorts/lpwBsj0j_OY　](https://youtube.com/shorts/lpwBsj0j_OY?si=xgmBO4OIdy3xXzdP)

1. **Demonstration of Accuracy and Speed:** The video illustrates the model's ability to quickly and accurately detect enemy heads. This is crucial for evaluating the real-time effectiveness of the bot in a gaming scenario.
2. **Showcasing Bot Functionality:** Viewers can observe how the bot interprets the game's visuals, processes them, and accurately adjusts the aim towards the detected enemy. It provides a clear understanding of how the bot operates in live game situations.
3. **Highlighting Current Limitations:** The video also exposes areas where the bot can be further improved, such as the occasional erratic mouse movements and scaling issues. These points are critical for future development and refinement.
