# SmartFulfill AI

**An AI-powered multi-agent system for intelligent e-commerce order processing and automation.**

SmartFulfill AI aims to simplify and automate e-commerce order processing through specialized AI agents that collaborate to validate orders, check inventory, detect potential fraud, calculate pricing, and coordinate shipping.

The project uses Microsoft's **Semantic Kernel** as its AI orchestration layer, with support for **Google Gemini** and **Groq** as AI model providers.

## 🎯 Project Objectives

- Automate repetitive e-commerce order processing tasks.
- Build specialized AI agents for individual business responsibilities.
- Enable agents to interact with tools and shared order data.
- Improve order validation and processing efficiency.
- Design a modular and scalable architecture with support for multiple AI providers.

## 🤖 Planned AI Agents

| Agent | Responsibility |
|---|---|
| Address Verification Agent | Validate customer delivery addresses. |
| Inventory Agent | Check product availability and stock. |
| Fraud Detection Agent | Identify suspicious orders and potential fraud. |
| Pricing Agent | Calculate order pricing and applicable adjustments. |
| Shipping Agent | Evaluate shipping options and coordinate delivery. |

## 🛠️ Technology Stack

**AI & Backend**
- Python
- FastAPI
- Microsoft Semantic Kernel
- Google Gemini API
- Groq API

**Database**
- MongoDB
- PyMongo

**Frontend**
- React
- Vite
- Tailwind CSS

**DevOps & Cloud**
- Docker
- Docker Compose
- Terraform
- AWS
- GitHub Actions

## 🏗️ Architecture Overview

The system is designed around a multi-agent architecture in which specialized agents handle different stages of order processing.

A shared order state allows agents to access relevant order information and coordinate their decisions.

Semantic Kernel provides the orchestration and AI integration layer, while external tools and backend services handle deterministic business operations.

## 🚧 Development Status

This project is currently under active development.

Current progress:
- [x] Initial project structure
- [x] Python virtual environment setup
- [x] Frontend project initialization
- [x] Initial dependency configuration
- [x] Groq API connectivity through Semantic Kernel
- [ ] Gemini API connectivity verification
- [ ] AI function/tool-calling implementation
- [ ] Specialized agent development
- [ ] Shared order state implementation
- [ ] Backend API development
- [ ] Frontend integration
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] AWS deployment

## 🔐 Environment Configuration

Create a `.env` file in the project root and configure your credentials:

```env
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=smartfulfill_db
PORT=8000
ENVIRONMENT=development
```

Never commit your actual API keys or secrets to GitHub.

## 🚀 Project Vision

The long-term goal is to develop a reliable, modular, and scalable AI-powered order processing platform that demonstrates practical applications of multi-agent systems, AI orchestration, backend engineering, and DevOps practices.

---

**SmartFulfill AI — Making E-commerce Order Processing Smarter, Faster, and More Intelligent.**
