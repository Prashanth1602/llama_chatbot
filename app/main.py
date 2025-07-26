import streamlit as st
from chatbot import get_response
from auth import login, signup, login_required
from models import get_db, ChatHistory, User, delete_chat_history

# Set page configuration
st.set_page_config(
    page_title="TechieTina - AI Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Add custom CSS for styling
st.markdown("""
    <style>
        .stTextInput label {
            color: #1E88E5;
        }
        .stButton button {
            background-color: #1E88E5;
            color: white;
        }
        .stButton button:hover {
            background-color: #1565C0;
        }
        .st-expander {
            background-color: #f8f9fa;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .st-expander:hover {
            background-color: #e9ecef;
        }
        .delete-button {
            background-color: #dc3545;
            color: white;
            padding: 5px 10px;
            border-radius: 5px;
            cursor: pointer;
        }
        .delete-button:hover {
            background-color: #c82333;
        }
        .stCheckbox label {
            color: #1E88E5;
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="TechieTina - AI Assistant", page_icon=":robot_face:", layout="centered")

if not st.session_state.get("user"):
    st.title("TechieTina - AI Assistant")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            user = login(email, password)
            if user:
                st.session_state["user"] = user
                st.rerun()
            else:
                st.error("Invalid credentials. Please try again.")

    with tab2:
        new_email = st.text_input("New Email")
        new_password = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            user = signup(new_email, new_password)
            if user:
                st.session_state["user"] = user
                st.rerun()
            else:
                st.error("Error creating account. Please try again.")

else:
    st.title("TechieTina - AI Assistant")
    st.write("Welcome, {}!".format(st.session_state["user"].email))
    
    question = st.text_input("What's Your Question:", "")
    
    if st.button("Get Answer"):
        if question:
            with st.spinner("Thinking..."):
                response = get_response(question)
                st.markdown(response)
                
                # Save chat history
                db = next(get_db())
                try:
                    # Check if user exists, if not create new user
                    user = db.query(User).filter_by(id=st.session_state["user"].uid).first()
                    if not user:
                        user = User(
                            id=st.session_state["user"].uid,
                            email=st.session_state["user"].email
                        )
                        db.add(user)
                        db.commit()

                    # Save chat
                    chat = ChatHistory(
                        user_id=st.session_state["user"].uid,
                        question=question,
                        response=response
                    )
                    db.add(chat)
                    db.commit()
                    st.success("Chat saved successfully!")
                except Exception as e:
                    st.error(f"Error saving chat: {str(e)}")
                    db.rollback()
        else:
            st.error("Please enter a question before clicking the button.")
    
    if st.checkbox("Show Previous Chats"):
        db = next(get_db())
        try:
            chats = db.query(ChatHistory).filter_by(user_id=st.session_state["user"].uid).all()
            if chats:
                for chat in chats:
                    with st.expander(f"Chat from {chat.created_at}"):
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            st.markdown("""
                                <div style='color: #1E88E5; font-weight: bold;'>Question:</div>
                                <div style='margin-left: 20px;'>{}</div>
                                <div style='color: #1E88E5; font-weight: bold;'>Response:</div>
                                <div style='margin-left: 20px;'>{}</div>
                            """.format(chat.question, chat.response), unsafe_allow_html=True)
                        with col2:
                            if st.button("🗑️ Delete", key=f"delete_{chat.id}", help="Delete this chat"):
                                delete_chat_history(chat.id)
                                st.experimental_rerun()
            else:
                st.info("No previous chats found.")
        except Exception as e:
            st.error(f"Error fetching previous chats: {str(e)}")