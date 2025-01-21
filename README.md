# VitalEdge Troll

**Troll** is the experimental interface within the VitalEdge ecosystem designed for exploring, testing, and validating new ML/LLM workflows, analytics, and data processes. Troll enables developers and data scientists to prototype and refine innovative algorithms and pipelines on experimental datasets or shadow APIs, ensuring they are production-ready before formal deployment.

---

## Key Features

### 1. **Experimental Analytics and Workflows**
- Test experimental data processing pipelines.
- Prototype LangChain workflows and alternative LLM/ML integrations.
- Explore shadow APIs and experimental queries for Datalake (LONGLAKE).

### 2. **Direct Integration with LONGLAKE**
- Query experimental views, tables, and endpoints in LONGLAKE.
- Perform advanced SQL queries through shadow APIs for analytics.

### 3. **Flexible ML/LLM Experimentation**
- Experiment with alternative ML models (e.g., PyTorch/TensorFlow workflows).
- Prototype and validate LangChain and RAG workflows.
- Test new LLM configurations, fine-tuning, and embeddings strategies.

### 4. **Developer-Friendly Environment**
- Modular, extensible architecture for new experimental features.
- Supports rapid prototyping and iterative experimentation.

---

## Project Structure

```plaintext
vitaledge-troll/
├── app/
│   ├── components/               # Gradio UI components
│   ├── services/                 # Interaction with APIs and external services
│   ├── utils/                    # Utility scripts (e.g., database connections)
│   ├── templates/                # Templates for Gradio components
│   ├── config.py                 # Configuration settings for Troll
│   └── main.py                   # Entry point for the Troll application
├── docs/                         # Documentation for Troll development
├── requirements.in               # Base dependencies
├── requirements.txt              # Pinned dependencies
└── README.md                     # Project documentation
```

---

## Installation and Setup

### Prerequisites
- **Python 3.9 or higher**
- **PostgreSQL** for accessing LONGLAKE
- **Datalake API** available at `http://127.0.0.1:8000`

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vitaledge/vitaledge-troll.git
   cd vitaledge-troll
   ```

2. **Set Up Environment**:
   Use [conda](https://docs.conda.io/en/latest/) or `venv`:
   ```bash
   conda create -n vitaledge-troll python=3.9 -y
   conda activate vitaledge-troll
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Configuration**:
   Create a `.env` file with your environment variables:
   ```bash
   cp .env.example .env
   ```

5. **Run the Application**:
   ```bash
   python app/main.py
   ```

---

## Usage

### Access the Troll UI
Once the application is running, open your browser and navigate to:
```plaintext
http://127.0.0.1:7860
```

Explore experimental ML/LLM workflows, interact with LONGLAKE queries, and test prototype pipelines.

---

## Contribution Guide

Contributions are welcome! Follow these steps:
1. Fork the repository and clone your fork.
2. Create a new feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes and push to your fork.
4. Create a pull request describing your changes.

---

## Roadmap

- **Support for LoRA/PEFT fine-tuning experiments.**
- **Integration of advanced LangChain workflows.**
- **UI improvements for better modularity and usability.**

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or support, contact [VitalEdge Team](mailto:samseatt@gmail.com).
