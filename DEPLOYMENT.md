# 🚀 Quick Deployment Guide

## For Your DevLab Linux Server

### 1. **Clone the Repository**
```bash
# On your devlab server
git clone <your-repository-url>
cd claude_agent_system
```

### 2. **One-Command Installation**
```bash
chmod +x install.sh
./install.sh
```

### 3. **Start the System**
```bash
source venv/bin/activate
python main.py
```

### 4. **Access the Dashboard**
- Open browser to: `http://your-server-ip:5000`
- Or if local: `http://localhost:5000`

## 🎯 **What You Get**

✅ **Complete Web-Based System** - No CLI needed!
✅ **3 Worker Agents** - Ready to execute tasks
✅ **Beautiful Dashboard** - Real-time monitoring and control
✅ **Persistent Storage** - SQLite database for all tasks
✅ **Simulation Mode** - Works with or without Claude Code
✅ **Production Ready** - Logging, error handling, graceful shutdown

## 🔧 **System Features**

### **Web Dashboard**
- Start/stop the entire system
- Submit individual tasks or complete workflows
- Monitor real-time progress
- View detailed task execution logs
- System health monitoring

### **Task Management**
- Priority-based task scheduling
- Automatic retries with error handling
- Task dependencies and workflows
- Persistent task history

### **Multi-Agent Architecture**
- Master orchestrator coordinating everything
- Multiple worker agents for parallel execution
- Intelligent adviser monitoring system health
- Real-time WebSocket updates

## 📊 **Usage Examples**

### **Simple Task**
1. Click "New Task" 
2. Description: "Create a REST API"
3. Commands:
   ```
   Create a Flask REST API with user authentication
   Add CRUD operations for data management
   Include comprehensive unit tests
   Generate API documentation
   ```

### **Development Workflow**
1. Click "Create Workflow"
2. Project: "E-commerce Platform"
3. Features:
   ```
   User authentication system
   Product catalog management
   Shopping cart functionality
   Payment processing integration
   Admin dashboard
   ```

## 🛠 **Configuration**

Edit `config.yaml` to customize:
- Number of workers
- Task priorities and retries
- System health monitoring intervals
- Workspace and database locations

## 📈 **Monitoring**

The dashboard provides:
- Real-time system status
- Task execution progress
- Worker performance metrics
- System health alerts
- Detailed execution logs

## 🔄 **Running as a Service** (Optional)

```bash
# Install as systemd service
sudo cp claude-agents.service /etc/systemd/system/
sudo systemctl enable claude-agents
sudo systemctl start claude-agents

# Check status
sudo systemctl status claude-agents
```

## 🎉 **You're Ready!**

The system is now running with a beautiful web interface that gives you complete control over your multi-agent development automation platform. No more command line - everything is done through the intuitive web dashboard!

**🌐 Access your dashboard at: http://your-server:5000**