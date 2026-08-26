# Module 09: Projects & Capstones

> 🏗️ **Python Mastery** · Module 09 — Apply what you've learned through hands-on projects

This module contains mini-projects and capstone challenges that let you apply concepts from across the course. Each project builds real-world applications and reinforces multiple modules simultaneously.

## 📚 Module Structure

### Part 1: Mini-Projects (Modules 01-08)
Focused projects applying core Python skills

### Part 2: Data Science Projects (Modules 10-12)
Projects using NumPy, Pandas, and Matplotlib

### Part 3: ML/DL Projects (Modules 13-15)
Machine learning and deep learning applications

### Part 4: AI Engineering Capstones (Modules 16-18)
Complete systems combining NLP, LLMs, and MLOps

---

## 🎯 Part 1: Python Fundamentals Projects

### Project 1.1: Contact Management System
**Applies:** Modules 01-04 (Basics, Control Flow, Functions, Data Structures)

Build a CLI contact manager with:
- Add/edit/delete contacts (name, email, phone)
- Search by name or email
- Data persistence (JSON file)
- Input validation

**Skills:** dictionaries, functions, file I/O, user input validation

---

### Project 1.2: Personal Finance Tracker
**Applies:** Modules 01-05 (+ Intermediate Python)

Track income and expenses with:
- Add transactions with date, category, amount
- Monthly summaries by category
- Date range filtering
- Export to CSV
- Data visualization (bar chart of spending by category)

**Skills:** datetime, JSON, CSV, data structures, comprehensions

---

### Project 1.3: Text-Based Adventure Game
**Applies:** Modules 01-08 (+ OOP)

Create an interactive story game with:
- Room navigation system
- Inventory management
- Combat mechanics
- Save/load game state
- OOP design (Player, Room, Item, Enemy classes)

**Skills:** classes, inheritance, file handling, control flow

---

## 🔢 Part 2: Data Science Projects

### Project 2.1: Weather Data Analysis
**Applies:** Modules 10-12 (NumPy, Pandas, Matplotlib)

Analyze historical weather data:
- Load and clean weather CSV data
- Calculate monthly/yearly statistics
- Identify trends and anomalies
- Create visualizations (temperature trends, precipitation patterns)
- Statistical analysis (correlations, moving averages)

**Skills:** pandas DataFrames, aggregation, groupby, time series, plotting

**Dataset:** Use public weather data (NOAA, OpenWeather historical)

---

### Project 2.2: Sales Dashboard
**Applies:** Modules 10-12

Build an interactive sales analysis dashboard:
- Load sales transactions from CSV
- Product performance analysis
- Time-based trends (daily, weekly, monthly)
- Customer segmentation
- Multi-plot dashboard with subplots

**Skills:** pandas analysis, matplotlib subplots, data aggregation

---

### Project 2.3: Stock Market Analysis
**Applies:** Modules 10-12

Analyze stock price data:
- Fetch historical stock data (yfinance library)
- Calculate technical indicators (moving averages, RSI)
- Compare multiple stocks
- Visualize with candlestick charts
- Portfolio performance tracking

**Skills:** pandas, financial data, advanced plotting, calculations

---

## 🤖 Part 3: Machine Learning Projects

### Project 3.1: House Price Predictor
**Applies:** Module 13 (Machine Learning)

Build a regression model:
- Load and explore housing dataset
- Feature engineering (categorical encoding, scaling)
- Train multiple models (Linear, Ridge, Random Forest)
- Cross-validation and hyperparameter tuning
- Model comparison and selection
- Predict on new data

**Skills:** scikit-learn, regression, preprocessing, model evaluation

**Dataset:** Kaggle Housing Prices or similar

---

### Project 3.2: Email Spam Classifier
**Applies:** Modules 13, 16 (ML + NLP)

Text classification system:
- Preprocess email text data
- TF-IDF vectorization
- Train classifiers (Naive Bayes, Logistic Regression, SVM)
- Evaluate with precision/recall/F1
- Handle class imbalance
- Build prediction pipeline

**Skills:** NLP preprocessing, text classification, imbalanced data

---

### Project 3.3: Image Classifier with Transfer Learning
**Applies:** Modules 14-15 (Deep Learning, Computer Vision)

CNN image classification:
- Use a pretrained model (ResNet, EfficientNet)
- Fine-tune on custom dataset
- Data augmentation
- Training loop with validation
- Save/load model
- Real-time prediction on new images

**Skills:** PyTorch/TensorFlow, transfer learning, CNNs, model training

**Dataset:** CIFAR-10, custom pet breeds, plant diseases, etc.

---

### Project 3.4: Customer Segmentation
**Applies:** Module 13

Unsupervised learning project:
- Load customer transaction data
- Feature engineering (RFM analysis)
- K-means clustering
- Cluster interpretation and profiling
- Visualize clusters with PCA
- Business recommendations

**Skills:** clustering, dimensionality reduction, EDA

---

## 🚀 Part 4: AI Engineering Capstones

### Capstone 4.1: RAG Document Q&A System
**Applies:** Modules 16-17 (NLP, LLMs)

Build a retrieval-augmented generation system:
- Ingest and chunk documents
- Create embeddings with sentence-transformers
- Store in vector database (ChromaDB, FAISS)
- Retrieve relevant context for queries
- Generate answers with Claude API
- Implement citation tracking
- Web UI with Streamlit/Gradio

**Skills:** embeddings, vector search, LLM APIs, prompt engineering

---

### Capstone 4.2: Production ML Pipeline
**Applies:** Modules 13, 18 (ML, MLOps)

End-to-end ML system:
- Train a model with experiment tracking (MLflow)
- Create FastAPI serving endpoint
- Containerize with Docker
- CI/CD pipeline (GitHub Actions)
- Monitoring dashboard (drift detection, performance metrics)
- Automated retraining trigger
- Load testing and performance optimization

**Skills:** MLflow, FastAPI, Docker, CI/CD, monitoring

---

### Capstone 4.3: Chatbot with Memory
**Applies:** Modules 17-18 (LLMs, MLOps)

Conversational AI system:
- Multi-turn conversation with Claude API
- Conversation memory (short-term + long-term)
- Function calling for tool use
- User authentication and session management
- Conversation analytics
- Deployment-ready architecture
- Cost tracking and optimization

**Skills:** LLM APIs, function calling, session state, production design

---

### Capstone 4.4: Sentiment Analysis Platform
**Applies:** Modules 10-18 (Full Stack)

Complete sentiment analysis system:
- Web scraping (Twitter/Reddit API or similar)
- Real-time sentiment classification
- Time series analysis of sentiment trends
- Interactive dashboard
- Batch processing pipeline
- Model versioning and A/B testing
- Alerting for sentiment shifts

**Skills:** APIs, ML pipeline, visualization, MLOps, system design

---

## 📝 Project Guidelines

### Working Through Projects

1. **Read the requirements** carefully
2. **Plan before coding** - sketch your data flow and architecture
3. **Start simple** - get a minimal version working first
4. **Iterate** - add features incrementally
5. **Test frequently** - verify each component as you build
6. **Document** - add README, comments, docstrings

### Submission Format (for self-assessment)

Each project should include:
- `README.md` - overview, features, setup instructions, usage
- Source code with clear structure
- `requirements.txt` - all dependencies
- Sample data or instructions to obtain it
- Example outputs (screenshots, saved results)
- (For capstones) Architecture diagram

### Time Estimates

- **Mini-projects (1.1-1.3):** 4-8 hours each
- **Data Science projects (2.1-2.3):** 6-12 hours each
- **ML projects (3.1-3.4):** 8-16 hours each
- **Capstones (4.1-4.4):** 20-40 hours each

### Recommended Approach

- **Complete 1 mini-project** after finishing Module 08
- **Complete 1 data science project** after Module 12
- **Complete 1-2 ML projects** after Module 15
- **Choose 1 capstone** after Module 18 to showcase your full skillset

---

## 🎯 Learning Outcomes

After completing these projects, you will be able to:
- Build complete applications from requirements to deployment
- Integrate multiple technologies and libraries
- Design data pipelines and ML workflows
- Write production-quality, maintainable code
- Debug complex multi-component systems
- Make architectural decisions with tradeoff analysis
- Deploy and monitor real-world AI applications

---

## 💡 Extension Ideas

Want to go further? Try these enhancements:

- Add web UI with Flask/FastAPI/Streamlit
- Deploy to cloud (AWS, GCP, Azure, Hugging Face Spaces)
- Add authentication and user management
- Scale with distributed processing (Dask, Ray)
- Implement caching for performance
- Add comprehensive logging and observability
- Build mobile app interface
- Create API documentation with Swagger

---

**Ready to build?** Start with a mini-project and work your way up to the capstones. Each completed project is a portfolio piece that demonstrates your Python and AI engineering skills.

📁 **Coming Soon:** Detailed starter code, hints, and reference implementations for each project.
