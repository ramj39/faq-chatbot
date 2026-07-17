Industrial Plating Solutions - FAQ Chatbot
==========================================

Overview:
---------
This project contains a simple FAQ chatbot built with Streamlit.
It uses two JSON files:
- faq.json: Stores common questions and answers.
- intent_filter.json: Defines keyword groups for intent detection.

Files:
------
- index.html        : Company homepage (static site)
- faq.html          : FAQ landing page (gateway to chatbot)
- faq_app.py        : Streamlit chatbot application
- faq.json          : FAQ question-answer pairs
- intent_filter.json: Intent classification keywords
- requirements.txt  : Python dependencies
- README.txt        : Project documentation

How to Run Locally:
-------------------
1. Install dependencies:
   pip install -r requirements.txt

2. Run the chatbot:
   streamlit run faq_app.py

3. Open in browser:
   http://localhost:8501

Deployment:
-----------
- Upload index.html and faq.html to GitHub Pages for the company site.
- Deploy faq_app.py, faq.json, intent_filter.json, and requirements.txt on Streamlit Cloud.
- Link the FAQ landing page (faq.html) to the Streamlit app URL.

Contact:
--------
Industrial Plating Solutions Pvt Ltd
Phone: +91 98765 43210
Email: info@fictitiousplating.com