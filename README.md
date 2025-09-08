# FinalYearProject-DetectingFakeReviewsThroughBERTLLaMAAndGAN-
## Data collection 
The process begins by collecting comment data from various websites, allowing for a comprehensive dataset.

## Methodology

The methodology begins with collecting comment data from various websites, including Amazon and TaoBao, to create a comprehensive dataset. The collected comments cover a range of products, from portable chargers to skincare items, many of which are controversial and contain advertisements. This dataset is analyzed to distinguish between bot-generated comments, advertisements, and genuine user feedback.

A BERT language model is trained on this dataset to evaluate the authenticity of each comment by assigning an authenticity score. In parallel, a generative AI model is developed to produce comments that mimic authentic human interactions.

Using a feedback loop, the system evaluates generated comments, identifying those with low authenticity scores. This helps the AI learn to produce more realistic comments over time. The core of this approach is a Generative Adversarial Network (GAN) framework that simultaneously improves the performance of the BERT classifier and the generative AI.

The front end of the system is developed as an Android app using Android Studio, providing a user-friendly interface. The backend is implemented with Kotlin, managing user interactions such as submitting comments for authenticity classification or generating human-like comments based on input keywords. Communication between the app and the server is facilitated by Retrofit.

The server, built with Flask and hosted locally, processes requests from multiple clients, including the Android app and a Telegram bot. This architecture supports scalable deployment and seamless interaction between components.

## System architecture
<img width="965" height="472" alt="GAN_archi" src="https://github.com/user-attachments/assets/ab6520af-0048-4002-960d-c2eee9efbbf1" />

## Android app architecture
<img width="792" height="437" alt="app_archi" src="https://github.com/user-attachments/assets/a3e0e620-62bb-44c3-bc96-92778e49d7c6" />

## App Interface
<img width="263" height="606" alt="AppBertwithdirection" src="https://github.com/user-attachments/assets/1005ead5-1f67-445a-b889-bd72f7afa7f0" />
<img width="253" height="557" alt="AppLlamawithdirection" src="https://github.com/user-attachments/assets/0078c774-2b04-4ee8-98ab-bd20a67390a3" />

## TG App Interface
<img width="1152" height="862" alt="Whole_TG_screenshot" src="https://github.com/user-attachments/assets/b526f980-e199-442b-a240-d6ea09549ac3" />

## Difficulties
One of the major challenges in building this app is creating a user-friendly and intuitive UI poses another significant difficulty, as it requires careful design and testing to ensure that the app is both visually appealing for users.


