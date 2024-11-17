# **DinnerTonight Bio Generator Application.**

## Project Overview

DinnerTonight is a platform designed to create personalized bios based on user preferences. The Bio Generator Application allows users to input their traits, interests, and career choices to generate a tailored bio that reflects their personality. This project leverages an existing AI/ML model to craft appealing and unique bios based on the input categories.


## Appendix
- [Features.](#features)
- [Tech Stack.](#tech-stack) 
- [Installation.](#installation)
- [Usage.](#usage) 
- [Deployment.](#deployment) 
- [Project Structure](#project-structure)


### Features
1. Users can select from predefined categories like:
    - Career/Profession (e.g., Software Engineer, Artist)
    - Personality Traits (e.g., Creative, Adventurous)
    - Interests (e.g., Music, Traveling)
    - Relationship Goals (e.g., Casual, Long-term)
2. The app generates a personalized bio based on user selections using an AI model.
3. User-friendly interface with responsive design.
4. Hosted on a free cloud platform for public access.

### Tech Stack

1. Frontend: HTML, CSS, JavaScript
2. Backend: Python (Flask)
3. AI Model: OpenAI GPT-3.5 (or a similar text-generation model from Hugging Face)
4. Hosting: Render.com / Vercel / PythonAnywhere  

### Installation

#### Prerequisites
1. Python 3.10+
2. API Key for OpenAI(if using GPT-3.5) or access to a pre-trained Hugging Face model

#### Steps
1. Clone the repository:
    - git clone https://github.com/Rohini2202/dinnertonight-bio-generator.git
    - cd dinnertonight-bio-generator

2. Install dependencies:
	pip install -r requirements.txt

3. Set up your API key:
     - Create a .env file and add your OpenAI API key:
          - OPENAI_API_KEY=your_api_key_here

4. Run the application:
	python app.py

5. Open your browser and visit:
	http://127.0.0.1:5000

### Usage

1. Open the web application.
2. Select your preferences from the drop-down menus (Career, Personality, Interests, Relationship Goals).
3. Click Generate Bio.
4. View the personalized bio displayed on the screen.

### Deployment 

The app is hosted on a cloud platform for easy public access. You can deploy your version using:

1. Render.com: Suitable for Flask applications.
2. Vercel: Ideal for serverless deployments.
3. PythonAnywhere: Simple hosting for Python apps.

#### Deployment Instruction (Render.com):

1. Push your project to GitHub.
2. Create a new Web Service on Render.com and connect your GitHub repository.
3. Set the build command: pip install -r requirements.txt
4. Set the start command: python app.py
5. Deploy the application and get the live link.

### Project Structure

dinnertonight-bio-generator/

├── app.py               # Flask backend

├── templates/

│   └── index.html       # Frontend HTML

├── static/

│   ├── styles.css       # CSS for styling

│   └── script.js        # JavaScript for frontend logic

├── requirements.txt     # Python dependencies

├── README.md            # Project documentation

└── .env                 # API keys (not included in repo)


### Contact

For any questions or suppot, please contact:
- Name: Rohini Athaluri
- Email: athalurirohini@gmail.com
