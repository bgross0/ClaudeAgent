# Claude Code Agentic Development System

🤖 **A fully-featured, production-ready multi-agent orchestration platform that transforms Claude Code into an enterprise-grade development automation system.**

## 🌟 Features

### ✨ **Core Capabilities**
- **Multi-Agent Architecture**: Master-worker pattern with intelligent task distribution
- **Real-time Web Dashboard**: Beautiful, responsive interface for system monitoring and control
- **Persistent Task Management**: SQLite-based storage with task history and state management
- **Claude Code Integration**: Seamless integration with fallback simulation mode
- **System Health Monitoring**: Intelligent adviser agent with alerts and recommendations

### 🚀 **Key Benefits**
- **Zero-Config Startup**: Works out-of-the-box with sensible defaults
- **Simulation Mode**: Full functionality even without Claude Code installed
- **Production Ready**: Database persistence, logging, error handling, and graceful shutdown
- **Web-Based Control**: No CLI required - everything through the beautiful web interface
- **Scalable Design**: Add more workers as needed for increased throughput

## 🎯 **Quick Start**

### **1. Clone and Install**
```bash
git clone <your-repo-url>
cd claude_agent_system
chmod +x install.sh
./install.sh
```

### **2. Start the System**
```bash
source venv/bin/activate
python main.py
```

### **3. Access the Dashboard**
Open your browser to: **http://localhost:5000**

That's it! The system is now running with:
- ✅ 3 worker agents ready to execute tasks
- ✅ Intelligent system monitoring
- ✅ Beautiful web dashboard for control
- ✅ Persistent task storage
- ✅ Real-time status updates

## 📊 **Dashboard Overview**

The web dashboard provides complete system control:

### **System Overview**
- Real-time system status and health metrics
- Claude Code availability detection
- Active worker count and performance stats

### **Task Management**
- Submit individual tasks with custom commands
- Create complete development workflows
- View task history and execution details
- Real-time progress tracking

### **System Controls**
- Start/stop the entire system
- View live system logs
- Monitor worker performance
- System health alerts

## 💡 **Usage Examples**

### **Simple Task Submission**
1. Click "New Task" in the dashboard
2. Enter description: "Create a Python web scraper"
3. Add commands:
   ```
   Create a Python script that scrapes news headlines
   Add error handling and rate limiting
   Include unit tests
   Generate documentation
   ```
4. Set priority and submit

### **Development Workflow**
1. Click "Create Workflow"
2. Project name: "Blog API"
3. Features:
   ```
   User authentication system
   CRUD operations for blog posts
   Comment system
   Admin dashboard
   API documentation
   ```
4. The system creates and executes multiple coordinated tasks

### **Monitoring & Control**
- **Real-time Updates**: Dashboard updates every 5 seconds
- **Task Details**: Click any task to see execution details
- **System Logs**: View detailed execution logs
- **Performance Metrics**: Track success rates and execution times

## 🛠 **System Architecture**

### **Components**
- **Master Orchestrator**: Central system coordinator
- **Worker Agents**: Execute tasks using Claude Code or simulation
- **Adviser Agent**: System health monitoring and optimization
- **Task Queue**: Priority-based task scheduling with persistence
- **Web Interface**: Real-time dashboard with WebSocket updates

### **Data Flow**
1. Tasks submitted via web interface
2. Stored in SQLite database
3. Queued by priority for worker assignment
4. Workers execute using Claude Code (or simulation)
5. Results stored and displayed in real-time
6. System health continuously monitored

## 🔧 **Configuration**

Edit `config.yaml` to customize:

```yaml
system:
  num_workers: 5          # Increase for more throughput
  workspace_dir: "./workspace"
  log_level: "DEBUG"      # More detailed logging

tasks:
  default_priority: 5
  max_retries: 3

adviser:
  check_interval: 30      # Health checks every 30 seconds
```

## 📈 **Production Deployment**

### **As a Service**
```bash
# Copy service file
sudo cp claude-agents.service /etc/systemd/system/

# Enable and start
sudo systemctl enable claude-agents
sudo systemctl start claude-agents

# Check status
sudo systemctl status claude-agents
```

### **Process Management**
```bash
# View logs
sudo journalctl -u claude-agents -f

# Restart service
sudo systemctl restart claude-agents
```

## 🔍 **System Monitoring**

### **Built-in Metrics**
- Worker utilization and performance
- Task success/failure rates
- System resource usage
- Execution time analytics

### **Health Checks**
- Automatic detection of stuck tasks
- Worker health monitoring
- System performance alerts
- Failure rate monitoring

## 🚀 **Advanced Features**

### **Task Dependencies**
Tasks can specify dependencies for complex workflows:
```python
task_ids = orchestrator.submit_development_workflow(
    "e-commerce-site",
    ["user-auth", "product-catalog", "shopping-cart", "payment-processing"]
)
```

### **Priority Scheduling**
- High Priority (1): Critical tasks
- Normal Priority (5): Standard tasks  
- Low Priority (9): Background tasks

### **Error Handling**
- Automatic task retries with exponential backoff
- Detailed error logging and reporting
- Graceful degradation and recovery

## 🛡 **Security Features**

### **Optional Sandboxing**
```yaml
security:
  sandbox_mode: true
  allowed_commands: ["git", "npm", "python"]
  restricted_paths: ["/etc", "/var"]
```

### **Process Isolation**
- Each task runs in isolated workspace
- Resource limits and timeouts
- Safe command execution

## 📁 **File Structure**
```
claude_agent_system/
├── main.py              # Main application
├── config.yaml          # Configuration
├── requirements.txt     # Python dependencies
├── install.sh          # Installation script
├── templates/
│   └── dashboard.html   # Web dashboard
├── workspace/          # Task execution area
├── logs/              # System logs
└── claude_agents.db   # Task database
```

## 🔧 **Development**

### **Adding Custom Agents**
Extend the `WorkerAgent` class for specialized functionality:

```python
class CustomAgent(WorkerAgent):
    def execute_specialized_task(self, task):
        # Custom task execution logic
        pass
```

### **Custom Task Types**
Define specialized task types with custom execution logic:

```python
@dataclass
class DeploymentTask(Task):
    target_environment: str
    rollback_plan: str
```

## 🐛 **Troubleshooting**

### **Common Issues**
1. **Port 5000 in use**: Change port in `main.py`
2. **Permission errors**: Run `chmod -R 755 workspace`
3. **Database locked**: Stop all instances before restart

### **Debug Mode**
```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
python main.py
```

### **Simulation Mode**
The system automatically detects Claude Code availability and falls back to simulation mode for testing and development.

## 📞 **Support**

- **Issues**: Report bugs and feature requests
- **Documentation**: Comprehensive inline documentation
- **Examples**: Working examples included

## 📄 **License**

MIT License - Use freely for personal and commercial projects.

---

**🎉 Ready to revolutionize your development workflow? Start with Claude Code Agentic System today!**