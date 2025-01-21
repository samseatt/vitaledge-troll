# Architecture Specification Document

## VitalEdge Troll: Architecture Specification

### **1. Overview**
**VitalEdge Troll** is an experimental admin UI for developing and testing advanced ML, LLM, and analytics workflows within the **VitalEdge ecosystem**. Troll supports pre-production testing, experimentation, and validation of models and APIs, enabling developers to iterate on shadow systems and experimental constructs without affecting production services. Troll interacts with both the **VitalEdge Datalake API** and the experimental **LONGLAKE API** for seamless and isolated experimentation.

---

### **2. Objectives**
- **Facilitate experimentation:** Provide a UI for testing and validating ML/LLM pipelines and experimental analytics.
- **Shadow testing:** Support shadow APIs (LONGLAKE) for rapid iteration without production interference.
- **Interoperability:** Ensure compatibility with VitalEdge Datalake and other services within the ecosystem.
- **Modularity:** Allow easy addition of new experimental workflows and APIs.

---

### **3. Key Features**
1. **Two-Level Tab System**: Organized navigation with top-level sections and nested subtabs.
   - **Top-Level Tabs**:
     - RAG Operations
     - ML Workflows
     - Experimental Analytics
     - Utility Tools
   - **Subtabs** under each section for specific functionalities.

2. **Integration with APIs**:
   - Interact with VitalEdge Datalake through RESTful APIs.
   - Extend support to LONGLAKE APIs for shadow and experimental workflows.

3. **Experimental Sandbox**:
   - Modular support for trying out new workflows and configurations.
   - Seamless toggling between production and experimental API endpoints.

4. **Dynamic Data Interaction**:
   - Query and display data from LONGLAKE and Datalake.
   - Facilitate fine-tuning and testing of ML/LLM models with dynamic inputs.

5. **Logging and Monitoring**:
   - Built-in mechanisms to log API responses and user interactions for debugging.
   - Monitoring tools for identifying bottlenecks in experimental workflows.

---

### **4. System Design**

#### **4.1 High-Level Architecture**
Troll adopts a modular architecture to support flexible and extensible workflows:

- **Frontend**: Gradio-based UI for interactive and dynamic operations.
- **Backend Services**:
  - **VitalEdge Datalake API**: Provides structured data access.
  - **LONGLAKE API**: Supports experimental tables, views, and endpoints for testing.
- **Core Components**:
  - Experimental RAG workflows (custom prompts, embeddings, retrieval configurations).
  - ML experimentation (fine-tuning, inference, hyperparameter tuning).
  - Dynamic analytics queries (e.g., SQL exploration via APIs).

---

#### **4.2 Component Overview**
**Frontend**:
- **Framework**: Gradio
- **Features**:
  - Top-level tabs for clear navigation.
  - Subtabs for specific workflows and tools.

**Backend**:
- **Services**:
  - **API Integrations**:
    - **Datalake API**: Production-grade API for formal data operations.
    - **LONGLAKE API**: Shadow API for experimental operations.
  - **Utility Services**:
    - Logging
    - API request lifecycle management
    - Exception handling and debugging

**Core Modules**:
- **RAG Workflows**:
  - Experimental orchestration workflows with dynamic prompt building.
- **ML Workflows**:
  - Inference and fine-tuning interfaces.
- **Analytics Queries**:
  - API-driven SQL queries.
  - Dynamic data visualization.

---

### **5. Detailed Design**

#### **5.1 Frontend**
- **Navigation**:
  - Top-level Tabs:
    - RAG Operations: Covers embeddings, retrieval, and generation workflows.
    - ML Workflows: Interfaces for training, inference, and fine-tuning ML models.
    - Experimental Analytics: SQL queries, exploratory views.
    - Utility Tools: Placeholder for miscellaneous utilities.
  - Subtabs:
    - Organized under each section for fine-grained functionality.

- **Data Input and Output**:
  - Input Fields: Dynamic dropdowns, text fields, file uploads.
  - Output Displays: Tables, Markdown, and dynamic visualizations.

#### **5.2 Backend**
- **Service Layer**:
  - **DatalakeService**:
    - Provides endpoints for querying subjects, studies, and variants from VitalEdge Datalake.
  - **LONGLAKEService**:
    - Supports experimental queries and endpoints.
  - **RAGService**:
    - Handles orchestration of RAG workflows, including embedding generation and vector searches.
  - **MLService**:
    - Interfaces for ML model training and inference.

- **Database Layer**:
  - Interacts only via APIs.
  - Shadow queries handled through LONGLAKE.

#### **5.3 Utilities**
- **Config Management**:
  - `.env` file for managing environment-specific settings.
  - Centralized `config.py` for easy configuration.
- **Logging**:
  - API requests and responses logged for debugging.
  - Interactive logs displayed in the UI.

---

### **6. Workflow Examples**

#### **6.1 RAG Workflow Example**
1. User selects a query string and dataset.
2. Troll sends the query to LONGLAKE API for embedding generation.
3. Embeddings are sent to a vector DB for retrieval.
4. Retrieved documents are combined and sent to an LLM API for final response.
5. Results are displayed dynamically in Troll’s UI.

#### **6.2 SQL Query Example**
1. User inputs a SQL query through the Experimental Analytics tab.
2. The query is forwarded to LONGLAKE’s shadow API.
3. Results are displayed in a table format.

---

### **7. Future Expansions**
- **AutoML Support**:
  - Integrate AutoML pipelines for automated hyperparameter tuning.
- **Advanced Visualization**:
  - Add interactive charts and heatmaps for analytics workflows.
- **Live Monitoring**:
  - Display live metrics for APIs and workflows.
- **User Roles**:
  - Add role-based access control for managing experimental features.

---

### **8. Security and Governance**
- **Access Control**:
  - Secure APIs with authentication and authorization mechanisms.
  - Limit access to experimental endpoints.
- **Audit Logging**:
  - Record all operations performed in Troll for traceability.
- **Data Isolation**:
  - Ensure experimental data remains isolated from production.

---

### **9. Conclusion**
VitalEdge Troll provides a robust framework for pre-production experimentation and testing within the VitalEdge ecosystem. By leveraging LONGLAKE as a shadow API, Troll ensures flexibility and innovation without compromising production integrity. Its modular architecture and extensible design make it a pivotal tool for iterating on next-generation AI and analytics workflows.

