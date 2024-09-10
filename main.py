# # #   #from langchain_openai import ChatOpenAI
# # # from langchain_core.prompts import ChatPromptTemplate
# # # from langchain_core.output_parsers import StrOutputParser
# # # from langchain_community.llms import Ollama
# # # import streamlit as st
# # # import os
# # # from dotenv import load_dotenv

# # # #load_dotenv()

# # # #os.environ["LANGCHAIN_TRACING_V2"]="true"
# # # #os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# # # ## Prompt Template

# # # prompt=ChatPromptTemplate.from_messages(
# # #     [
# # #         ("system","You are a helpful assistant. Please response to the user queries"),
# # #         ("user","Question:{question}")
# # #     ]
# # # )
# # # ## streamlit framework

# # # st.title('Langchain Demo With llama3.1 API')
# # # input_text=st.text_input("Search the topic u want")

# # # # ollama LLAma2 LLm 
# # # llm=Ollama(model="llama3.1")
# # # output_parser=StrOutputParser()
# # # chain=prompt|llm|output_parser

# # # if input_text:
# # #     st.write(chain.invoke({"question":input_text}))



# # from langchain_core.prompts import ChatPromptTemplate
# # from langchain_core.output_parsers import StrOutputParser
# # from langchain_community.llms import Ollama
# # import streamlit as st
# # import os
# # from dotenv import load_dotenv

# # # Load environment variables
# # # load_dotenv()

# # # os.environ["LANGCHAIN_TRACING_V2"] = "true"
# # # os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# # # Streamlit UI elements for tone and context selection
# # st.title('Marketing Campaign Chatbot')

# # tone = st.selectbox(
# #     "Select Tone",
# #     ["Formal", "Casual", "Funny"]
# # )

# # context = st.selectbox(
# #     "Select Context",
# #     ["Product Launch", "Event Awareness", "Event Promotion"]
# # )

# # input_text = st.text_input("Enter your query:")

# # # Update the prompt template based on the selected tone and context
# # prompt = ChatPromptTemplate.from_messages(
# #     [
# #         ("system", f"You are a helpful assistant that provides {tone.lower()} responses for {context.lower()}."),
# #         ("user", "Question: {question}")
# #     ]
# # )

# # # Instantiate the language model and output parser
# # llm = Ollama(model="llama3.1")
# # output_parser = StrOutputParser()
# # chain = prompt | llm | output_parser

# # # If the user inputs a query, generate a response
# # if input_text:
# #     st.write(chain.invoke({"question": input_text}))





# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama
# import streamlit as st
# import os
# from dotenv import load_dotenv

# # Load environment variables (if needed)
# # load_dotenv()

# # os.environ["LANGCHAIN_TRACING_V2"] = "true"
# # os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# # Streamlit UI elements for tone, context, and length selection
# st.title('Advanced Marketing Campaign Chatbot')

# tone = st.selectbox(
#     "Select Tone",
#     ["Formal", "Casual", "Funny", "Serious", "Irreverent", "Enthusiastic", "Matter-of-fact"]
# )

# context = st.selectbox(
#     "Select Context",
#     ["Product Launch", "Event Awareness", "Event Promotion", "Seasonal Campaign", "Brand Awarness", "User Testimonials"]
# )

# text_length = st.radio(
#     "Select Desired Response Length",
#     ["Small: under 50 words", "Medium: 100 words", "Long: 200 words", "Very Long: above 500 Words"]
# )

# # User input
# input_text = st.text_input("Enter your query:")

# # Keep track of chat history
# if 'chat_history' not in st.session_state:
#     st.session_state.chat_history = []

# # Define response length rules
# if "Small" in text_length:
#     length_instruction = "Please keep the response under 50 words."
# elif "Medium" in text_length:
#     length_instruction = "Please keep the response 100 words."
# elif "Long" in text_length:
#     length_instruction = "Please make the response 200 words."
# else:
#     length_instruction = "Please make the response 500 words."

# # Update the prompt template with tone, context, and length
# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", f" You are Marketing creative Assistance/expert. You have to create the marketing campaign content in line with the instructions given by the user. The content must be in {tone.lower()} tone. The content must be {length_instruction} of length.If you don’t have the information just say so.Be concise."),
#         ("user", "Question: {question}")
#     ]
# )

# # Instantiate the language model and output parser
# llm = Ollama(model="llama3.1")
# output_parser = StrOutputParser()

# # Chatbot chain with history
# if input_text:
#     # Append user input to chat history
#     st.session_state.chat_history.append(("user", input_text))
    
#     # Build the full chat history into the prompt
#     chat_input = " ".join([f"{role}: {text}" for role, text in st.session_state.chat_history])

#     # Generate the response from the chatbot
#     chain = ChatPromptTemplate.from_messages(
#         [("system", f"You are a helpful assistant that responds in a {tone.lower()} tone and helps with {context.lower()} situations. {length_instruction}"),
#          ("user", chat_input)]
#     ) | llm | output_parser
    
#     response = chain.invoke({"question": input_text})
    
#     # Append the chatbot's response to the chat history
#     st.session_state.chat_history.append(("assistant", response))

#     # Display the chat history
#     for role, text in st.session_state.chat_history:
#         if role == "user":
#             st.write(f"*You:* {text}")
#         else:
#             st.write(f"*Assistant:* {text}")



from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables (if needed)
# load_dotenv()

# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Streamlit UI elements for tone, context, and length selection
st.title('Advanced Marketing Campaign Chatbot')

tone = st.selectbox(
    "Select Tone",
    ["Formal", "Casual", "Funny", "Serious", "Irreverent", "Enthusiastic", "Matter-of-fact"]
)

context = st.selectbox(
    "Select Context",
    ["Product Launch", "Event Awareness", "Event Promotion", "Seasonal Campaign", "Brand Awareness", "User Testimonials"]
)

text_length = st.radio(
    "Select Desired Response Length",
    ["Small: under 50 words", "Medium: 100 words", "Long: 200 words", "Very Long: above 500 Words"]
)

# User input
input_text = st.text_input("Enter your query:")

# Keep track of chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Define response length rules
if "Small" in text_length:
    length_instruction = "Please keep the response under 50 words."
elif "Medium" in text_length:
    length_instruction = "Please keep the response 100 words."
elif "Long" in text_length:
    length_instruction = "Please make the response 200 words."
else:
    length_instruction = "Please make the response 500 words."

# Update the prompt template with tone, context, and length
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", f"You are a Marketing creative assistant/expert. You have to create the marketing campaign content in line with the instructions given by the user. The content must be in a {tone.lower()} tone. The content must be {length_instruction}. If you don’t have the information, just say so. Be concise."),
        ("user", "Question: {question}")
    ]
)

# Instantiate the language model and output parser
llm = Ollama(model="llama3.1")
output_parser = StrOutputParser()

# Chatbot chain with history
if input_text:
    # Append user input to chat history
    st.session_state.chat_history.append(("user", input_text))
    
    # Build the full chat history into the prompt
    chat_input = " ".join([f"{role}: {text}" for role, text in st.session_state.chat_history])

    # Generate the response from the chatbot
    chain = ChatPromptTemplate.from_messages(
        [("system", f"You are a helpful assistant that responds in a {tone.lower()} tone and helps with {context.lower()} situations. {length_instruction}"),
         ("user", chat_input)]
    ) | llm | output_parser
    
    response = chain.invoke({"question": input_text})
    
    # Append the chatbot's response to the chat history
    st.session_state.chat_history.append(("assistant", response))

    # Display the chat history with visible differences
    for role, text in st.session_state.chat_history:
        if role == "user":
            st.write(f"*You:* {text}")
        else:
            st.write(f"*Assistant:* {text}")
        st.markdown("---")  # Add a separator after each response to distinguish them

# Move the input field down below responses
input_text = st.text_input("Enter your next query:")