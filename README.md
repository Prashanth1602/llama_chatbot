# TechieTina - AI Assistant

A Streamlit-based AI chatbot with Firebase authentication and PostgreSQL database integration.

## Features

- Firebase Authentication
- PostgreSQL Database Integration
- Chat History Storage
- User Authentication UI
- Streamlit-based Interface

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - `DATABASE_URL` - PostgreSQL database URL
   - Firebase credentials (FIREBASE_*)
   - `GROQ_API_KEY` - For LLM API access

## Deployment

The application is deployed on Render with:
- Firebase Authentication
- PostgreSQL Database
- Docker containerization

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string
- `FIREBASE_TYPE`: service_account
- `FIREBASE_PROJECT_ID`: Your Firebase project ID
- `FIREBASE_PRIVATE_KEY_ID`: Your Firebase private key ID
- `FIREBASE_PRIVATE_KEY`: Your Firebase private key
- `FIREBASE_CLIENT_EMAIL`: Your Firebase client email
- `FIREBASE_CLIENT_ID`: Your Firebase client ID
- `FIREBASE_AUTH_URI`: https://accounts.google.com/o/oauth2/auth
- `FIREBASE_TOKEN_URI`: https://oauth2.googleapis.com/token
- `FIREBASE_AUTH_PROVIDER_X509_CERT_URL`: https://www.googleapis.com/oauth2/v1/certs
- `FIREBASE_CLIENT_X509_CERT_URL`: Your Firebase client cert URL
- `GROQ_API_KEY`: Your Groq API key
