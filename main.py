import streamlit as st
from langchain_helper import get_few_shot_db_chain
import time

def main():
    st.title("Urban Threads T Shirts: Database Q&A with Smart AI 🤖👕")
    st.sidebar.title("Instructions")
    st.sidebar.write("Please ask questions related to the inventory and t-shirts of the following brands:")
    st.sidebar.write("- Nike")
    st.sidebar.write("- Adidas")
    st.sidebar.write("- Levi's")
    st.sidebar.write("- Van Heusen")
    
    question = st.text_input("Enter your question here:")
    
    if st.button("Ask"):
        if question:
            
            with st.spinner('Fetching answer...'):
                time.sleep(2)
                response = get_answer(question)
                if response:
                    st.header("Answer:")
                    st.write(response)
                else:
                    st.warning("No answer found for the question. Please try another question.")
    if st.button("About Me"):
        st.markdown(
            """
            ## About Me
            Hi there! I am a smart assistant designed to help you with questions about the inventory and t-shirts of popular brands like Nike, Adidas, Levi's, and Van Heusen.
            
            I work by converting your natural language questions into complex SQL queries to fetch the relevant information from our database. My goal is to provide accurate and helpful answers to your queries. If you have any questions or encounter any issues, please feel free to ask!
            """
        )
    st.markdown("---")
    st.markdown("*If there's any issue, I might be still learning! 🤖*")

def get_answer(question):
    try:
        chain = get_few_shot_db_chain()
        return chain.run(question)
    except Exception as e:
        st.error("Sorry, I'm not able to process that. My master is still training me!")
        return None

if __name__ == "__main__":
    main()
