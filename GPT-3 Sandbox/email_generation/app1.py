import streamlit as st


def app():
    # Setting up the Title
    st.title("Welcome :wave:")
    st.write(f"""
        ### Made with ❤️ by [**Kairos Data Labs**](https://www.linkedin.com/company/kairos-data-labs)
        """)
    intro = f"""
    ---
    ### **🎈 Getting Started**
    - Thank you for being a part of this Open-Source **GPT-3 Sandbox** 🙌
    - To get started, 1. go to **GPT-3 Sandbox** on the left side bar-> 2. Paste your **OpenAI API key**

    ### **👾 Create & deploy GPT-3 powered apps**
    - This sandbox is an open-source 🔧to enable anyone turn their GPT-3 app ideas into reality with just a few lines of Python code
    - It is built on top of Streamlit that enables you to quickly create & deploy web applications 
    - Streamlit takes care of hosting the endpoint and acts as a frontend interface for the web app
    """

    #st.header("🧠 Powered by Kairos Data Labs") 🎈 🐾 🏆

    st.write(intro)
    
    st.write(f"""
        ###  🐾 **About the Sandbox**
        - This is an open-source 🔧 and it is alive thanks to the awesome GPT-3 community. If you'd like to contribute, please check [Collaboration Guidelines](https://github.com/Shubhamsaboo/kairos_gpt3/blob/main/CONTRIBUTE.md)
        - If you are curious about what _exactly_ went behind this sandbox, check out the [source code](https://github.com/Shubhamsaboo/kairos_gpt3)
        - We are still working on it and we'd ❤️ to hear from you! If you have ideas how to improve the Sandbox, let us know [here](sandra@kairosdatalabs.com)
        """)

    st.write(f"""
            ---
            ### 🔗 **Connect With Us**
            - We are [Shubham](https://www.linkedin.com/in/shubhamsaboo/) and [Sandra](https://www.linkedin.com/in/sandrakublik/), co-founders of [Kairos Data Labs](https://www.linkedin.com/company/kairos-data-labs) 
            - We are super excited to have you here. Our mission is to make the [GPT-3 Sandbox](https://github.com/Shubhamsaboo/kairos_gpt3) accessbile and usable to everyone who wants to build applications with OpenAI's GPT-3 ❤️ 
            - Come by 🤗 [the forum](https://github.com/Shubhamsaboo/kairos_gpt3) if you'd like to ask questions, post an awesome app, or just say Hi!
        """)
