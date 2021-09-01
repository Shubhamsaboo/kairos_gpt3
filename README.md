<h2 align="center"> 🕹️ GPT-3 Sandbox </h2>

<h3 align="center">🧠 Powered by <ins>Kairos Data Labs</ins><sup><a  href="https://www.linkedin.com/company/kairos-data-labs">[?]</a></sup> </h3>


> 🏁: **You need access to the OpenAI API Key to play with this Sandbox**: If you dont have the access to the API, please apply [here](https://beta.openai.com/) ✌️


## 👾 Create & deploy GPT-3 powered apps
* This sandbox is an open-source 🔧to enable anyone turn their GPT-3 app ideas into reality with just a few lines of Python code
* It is built on top of Streamlit that enables you to quickly create & deploy web applications
* Streamlit takes care of hosting the endpoint and acts as a frontend interface for the web application

## 🎈 Try out our Sandbox Application
```bash
https://share.streamlit.io/shubhamsaboo/gpt3_sandbox/gpt_app.py
```

## 💥 Bringing up GPT-3 Sandbox Locally
🍴 Clone the `kairos_gpt3` repository using the following command

```bash
git clone https://github.com/Shubhamsaboo/kairos_gpt3.git
```

You need to have python 3.7+ installed, and then you can create a python virtual environment using [pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) or [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment) depending on your python setup. 

After installing and activating the virtual environment (The commands will differ for windows and linux installations which is clearly specified in the respective documentations), you can `cd` into the `email_generation` folder:

```bash
cd 'GPT-3 Sandbox'
cd email_generation
```

From `/email_generation` folder, you can run the following command to install the required dependencies

```bash
pip install -r requirements.txt
```

After installing the required dependencies, you can bring up the main application to validate that its working in your local enviroment. To bring up the application, you can run the following command from the `email_generation` folder.

```bash
streamlit run gpt_app.py
```


## 🎨 How to create an example application
* To create an app with a basic flow, you can use our default template for [Email Generation App](https://github.com/Shubhamsaboo/kairos_gpt3/tree/master/GPT-3%20Sandbox/email_generation)
* This template has a flow that will work well for a couple of basic use-cases and you can use it just by replacing the default [training prompt](https://github.com/Shubhamsaboo/kairos_gpt3/blob/master/GPT-3%20Sandbox/email_generation/training_data.py) with your application specifc prompt
* To test the application, provide a one-line task description in the -> **Input** text box
* You would then get an **Output** -> that should give you a good feeling of how to structure your application specifc tasks


## 🙌 Customize your application & contribute 
* If you want to play with the code and [contribute](https://github.com/Shubhamsaboo/kairos_gpt3/blob/master/CONTRIBUTE.md) your own application templates, please do! Sharing the knowledge with the GPT-3 community is the key mission of this sandbox ❤️
* To customize the UI of the web-applicaiton, please refer to the [Streamlit](https://docs.streamlit.io) 📖


##  🐾 **About the Sandbox**
* This is an open-source 🔧 and it is alive thanks to the awesome GPT-3 community. If you'd like to contribute, please check [Collaboration Guidelines](https://github.com/Shubhamsaboo/kairos_gpt3/blob/master/CONTRIBUTE.md)
* If you are curious about what _exactly_ went behind this sandbox, check out the [source code](https://github.com/Shubhamsaboo/kairos_gpt3)
* We are still working on it and we'd ❤️ to hear from you! If you have ideas how to improve the Sandbox, let us know [here](sandra@kairosdatalabs.com)


## 🔗 Connect With Us
* We are [Shubham](https://www.linkedin.com/in/shubhamsaboo/) and [Sandra](https://www.linkedin.com/in/sandrakublik/), co-founders of [Kairos Data Labs](https://www.linkedin.com/company/kairos-data-labs) 
* We are super excited to have you here. Our mission is to make the [GPT-3 Sandbox](https://github.com/Shubhamsaboo/kairos_gpt3) accessbile and usable to everyone who wants to build applications with OpenAI's GPT-3 ❤️ 
* Come by 🤗 [the forum](https://github.com/Shubhamsaboo/kairos_gpt3) if you'd like to ask questions, post an awesome app, or just say Hi!


## 📖 Reference Resources
For your reference we have created an array of applications to take inspiration from and come up with new ideas that can be useful for the community in General 

* [GPT-3 Applications](https://shubhamsaboo111.medium.com/) 
* [Video Tutorials/examples](https://www.youtube.com/channel/UCjG6QzmabZrBEeGh3vi-wDQ)
