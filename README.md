
  
<div align="center">
  <img src="https://github.com/user-attachments/assets/37a1b48e-3ebe-4dca-b9ec-763fc94e2fd8"
" alt="gt">
</div>

## Core Architecture Components
  
<div align="center">
  <img src="https://github.com/user-attachments/assets/f2af3c6a-bebb-4411-a319-f375937aa27d"
" alt="gt">
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/89f024b0-53f0-4b0b-bbe5-53d4b93ea3b3"
" alt="gt">
</div>


# 🎮 Ft_transcendence

A modern online gaming platform built with Django and React, featuring real-time multiplayer games, chat system, and comprehensive user management.

## 🏗️ Architecture

This project implements a microservices architecture using Docker containers with the following services: [1](#1-0) 

### Core Services
- **Backend**: Django REST API with WebSocket support
- **Frontend**: React SPA with Vite
- **Database**: PostgreSQL with Adminer interface
- **Cache**: Redis for sessions and real-time features
- **Security**: Nginx reverse proxy with SSL + HashiCorp Vault
- **Monitoring**: ELK Stack (Elasticsearch, Logstash, Kibana)
- **Development**: MailHog for email testing, Swagger for API docs

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Make (optional, for convenience commands)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Salah-HT/Ft_transcendence.git
cd Ft_transcendence
```

2. **Environment Setup**
```bash
cp .env.example .env
# Configure your environment variables
```

3. **Build and Run**
```bash
make build
# or
docker-compose up --build -d
``` [2](#1-1) 

### Available Commands
- `make build` - Build and start all services
- `make down` - Stop all services
- `make clean` - Clean Docker system
- `make fclean` - Complete cleanup (⚠️ deletes all data)


## 🛠️ Tech Stack

### Backend [3](#1-2) 

- **Framework**: Django 5.1.5 + Django REST Framework
- **Database**: PostgreSQL
- **Real-time**: Django Channels + Redis
- **Authentication**: JWT + OAuth 42 School
- **Security**: HashiCorp Vault for secrets management
- **API Documentation**: Swagger/OpenAPI

### Frontend [4](#1-3) 

- **Framework**: React 18 + Vite
- **Styling**: Tailwind CSS + Ant Design
- **Routing**: React Router DOM
- **Charts**: Chart.js + Recharts
- **State Management**: React Context

## 📁 Project Structure
```

```bash
Ft_transcendence/
├── Backend/
│   └── backend/
│       ├── authen/          # Authentication app
│       ├── game/            # Game management
│       ├── chat/            # Real-time chat
│       └── backend/         # Django settings
├── Frontend/
│   └── src/
│       ├── pages/           # Main pages
│       ├── components/      # Reusable components
│       ├── contexts/        # React contexts
│       └── services/        # API services
├── security/
│   └── nginx-server/        # Nginx + SSL config
├── database/                # PostgreSQL setup
└── docker-compose.yml       # Services orchestration
```


## 🎯 Features

### 🔐 Authentication & Security [5](#1-4) 

- **Multi-factor Authentication** (2FA)
- **OAuth Integration** with 42 School
- **Secure Password Reset** with time-limited tokens
- **Session Management** with Redis
- **HashiCorp Vault** for secrets

### 🎮 Gaming System [6](#1-5) 

- **Real-time Multiplayer** games
- **Tournament System**
- **Player Statistics** tracking
- **Game Invitations** between friends
- **Matchmaking** system

### 💬 Real-time Chat [7](#1-6) 

- **WebSocket-based** messaging
- **Direct Messages** between users
- **Group Chat** rooms
- **Friend System** with blocking capabilities
- **Real-time Notifications**

### 👤 User Management
- **Extended User Profiles** with avatars
- **Friend System** with requests/invitations
- **Online Status** tracking
- **Game Statistics** and leaderboards

## 🔧 Development

### Backend Development [8](#1-7) 

The Django backend uses ASGI for WebSocket support and includes comprehensive CORS configuration for frontend integration.

### Frontend Development [9](#1-8) 

React application with protected routes, authentication layouts, and comprehensive error handling.

## 📊 Monitoring & Logging

- **ELK Stack** for centralized logging
- **Kibana Dashboard** for log visualization
- **Health Checks** for all services
- **Adminer** for database management

## 🔒 Security Features

- **HTTPS/SSL** termination at Nginx
- **CORS** properly configured
- **CSRF** protection enabled
- **Secure Headers** (HSTS, etc.)
- **Secrets Management** with Vault
- **Input Validation** and sanitization

## 🌐 Service Ports

| Service | Port | Description |
|---------|------|-------------|
| Frontend | 5173 | React development server |
| Backend | 8000 | Django API |
| Database | 5432 | PostgreSQL |
| Redis | 6379 | Cache & sessions |
| Nginx | 80/443 | Reverse proxy |
| Adminer | 8082 | Database admin |
| Swagger | 8081 | API documentation |
| MailHog | 8025 | Email testing |
| Kibana | 5601 | Log visualization |
| Vault | 8200 | Secrets management |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of the 42 School curriculum.

---

**Built with ❤️ by the 42 School community**







