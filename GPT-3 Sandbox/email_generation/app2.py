import streamlit as st
from model_training_service import Code

def app():
        
    # Creating an object of prediction service
    pred = Code()

    api_key = st.sidebar.text_input("OpenAI API Key:", type="password")

    # Using the streamlit cache 
    @st.cache
    def process_prompt(input):
        return pred.model_prediction(input=input, api_key=api_key)
    
    if api_key:
            
        # Setting up the Title
        st.title("🕹️ GPT-3 Sandbox")

        st.write(f"""
        ## Made with ❤️ for 🤖 by Kairos Data Labs
        """)
        st.write("_This Sandbox will help you create & deploy OpenAI API powered app with a few lines of Python_")
        
        st.write("---")

        st.write(f"""
        ### 🎨 How to create an example application
        - To create an app with a basic flow, you can use our default template for [Email Generation App](https://github.com/Shubhamsaboo/kairos_gpt3/tree/main/GPT-3%20Sandbox/email_generation)
        - This template has a flow that will work well for a couple of basic use-cases and you can use it just by replacing the default [training prompt](https://github.com/Shubhamsaboo/kairos_gpt3/blob/main/GPT-3%20Sandbox/email_generation/training_data.py) with your application specifc prompt
        - To test the application, provide a one-line task description in the -> **Input** text box
        - You would then get an **Output** -> that should give you a good feeling of how to structure your application specifc tasks
        
        ### 🙌 Customize your application & contribute 
        - If you want to play with the code and [contribute](https://github.com/Shubhamsaboo/kairos_gpt3/blob/main/CONTRIBUTE.md) your own application templates, please do! Sharing the knowledge with the GPT-3 community is the key mission of this sandbox ❤️
        - To customize the UI of the web-applicaiton, please refer to the [Streamlit](https://docs.streamlit.io) 📖
        """)

        st.write(f"""---""")

        st.image("./ai.png", use_column_width=True)

        input = st.text_input('Input:')

        if st.button('Submit'):
            st.write('**Output**')
            st.write(f"""---""")
            with st.spinner(text='In progress'):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 API Key Not Found!")
        st.info("💡 Copy paste your OpenAI API key that you can find in User -> API Keys section once you log in to the OpenAI API Playground")